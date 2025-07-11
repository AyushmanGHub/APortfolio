import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ---- Static CSS ----
st.markdown("""
<style>
.main > div {
    padding-top: 1rem;
}
.stForm {
    background: #121212;
    padding: 30px 25px;
    border-radius: 12px;
    max-width: 800px;
    margin: 20px auto;
    font-family: 'Segoe UI', 'Roboto', sans-serif;
    color: #fff;
    box-shadow: 0 0 15px rgba(0,0,0,0.5);
}
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: transparent !important;
    border: none !important;
    border-bottom: 2px solid #444 !important;
    border-radius: 0 !important;
    color: #fff !important;
    font-size: 16px;
    transition: border-color 0.3s ease;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-bottom: 2px solid #00BFFF !important;
    box-shadow: none !important;
}
.stFormSubmitButton > button {
    background: linear-gradient(90deg, #00BFFF, #1E90FF) !important;
    color: #fff !important;
    padding: 12px 30px;
    border: none !important;
    border-radius: 30px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    cursor: pointer;
    transition: transform 0.2s ease !important;
    width: 100% !important;
}
.stFormSubmitButton > button:hover {
    transform: scale(1.05) !important;
    border: none !important;
}
.social-links img {
    transition: transform 0.2s ease;
}
.social-links img:hover {
    transform: scale(1.1);
}
</style>
""", unsafe_allow_html=True)

# ---- Header ----
st.markdown("""
<h2 style='text-align: center; color: #00BFFF; margin-bottom: 5px;'>📬 Contact Me</h2>
<p style='text-align: center; font-size:18px; margin-bottom: 30px;'>Let's connect for collaborations, projects, or just a quick chat!</p>
""", unsafe_allow_html=True)

# ---- Contact Form ----
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

def compose_email_body(name, email, subject, message):
    return f"""
You received a new message from your contact form:

Name: {name}
Email: {email}
Subject: {subject}
Message:
{message}
"""

def get_email_credentials():
    try:
        return st.secrets["EMAIL_ADDRESS"], st.secrets["EMAIL_PASSWORD"]
    except:
        st.error("Email credentials not configured. Please set up EMAIL_ADDRESS and EMAIL_PASSWORD in secrets.")
        return None, None

with st.form("contact_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name *", placeholder="Enter your name")
    with col2:
        email = st.text_input("Email *", placeholder="Enter your email")
    
    subject = st.text_input("Subject", placeholder="Enter subject (optional)")
    message = st.text_area("Write your message...", height=140, placeholder="Enter your message here...")
    
    submit_button = st.form_submit_button("Send Message")

    if submit_button:
        if name and email and message:
            if "@" not in email or "." not in email:
                st.error("❌ Please enter a valid email address.")
            else:
                EMAIL_ADDRESS, EMAIL_PASSWORD = get_email_credentials()
                if EMAIL_ADDRESS and EMAIL_PASSWORD:
                    try:
                        with st.spinner("Sending your message..."):
                            msg = MIMEMultipart()
                            msg['From'] = EMAIL_ADDRESS
                            msg['To'] = EMAIL_ADDRESS
                            msg['Subject'] = subject if subject else "Contact Form Message"
                            msg.attach(MIMEText(compose_email_body(name, email, subject, message), 'plain'))

                            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                                server.starttls()
                                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                                server.send_message(msg)

                        st.success("✅ Your message has been sent successfully!")
                        st.balloons()
                    except smtplib.SMTPAuthenticationError:
                        st.error("❌ Email authentication failed. Please check your credentials.")
                    except smtplib.SMTPException as e:
                        st.error(f"❌ SMTP error occurred: {str(e)}")
                    except Exception as e:
                        st.error(f"❌ An unexpected error occurred: {str(e)}")
        else:
            st.warning("⚠️ Please fill in all required fields (Name, Email, Message).")

# ---- Separator ----
st.markdown("""
<hr style="border: 0; height: 2px; background: linear-gradient(to right, #ff5858, #f09819); margin: 20px 0;">
""", unsafe_allow_html=True)

# ---- Social Section (Original Icons) ----
st.markdown("""
<h3 style='text-align: center; margin-bottom: 20px;'>🌐 Connect With Me</h3>
<div style='text-align: center;' class='social-links'>
    <a href='https://www.linkedin.com/in/ayushman-anupam' target='_blank'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'>
    </a>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <a href='https://github.com/AyushmanGHub' target='_blank'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'>
    </a>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <a href='mailto:ayushmantutu@gmail.com'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'>
    </a>
</div>

<div style='text-align: center; font-size: 18px; margin-top: 30px;'>
    🤝 <b>Let's collaborate and grow together!</b><br><br>
    I am passionate about <b>continuous learning</b>, <b>collaboration</b>, and applying <b>data science & AI</b> for real-world impact.
    Whether you're interested in data-driven projects, machine learning applications, or simply exchanging ideas — feel free to reach out.<br><br>
    💡 <i>Together, let's learn, build, and create impact.</i> 
</div>
""", unsafe_allow_html=True)

# ---- Final Separator ----
st.markdown("""
<hr style="border: 0; height: 2px; background: linear-gradient(to right, #ff5858, #f09819); margin: 20px 0;">
""", unsafe_allow_html=True)