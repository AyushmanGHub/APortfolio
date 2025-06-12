import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Contact Section Header
st.markdown("""
<h2 style='text-align: center; color: #00BFFF;'>📬 Contact Me</h2>
<p style='text-align: center; font-size:18px;'>Let's connect for collaborations, projects, or just a quick chat!</p>
""", unsafe_allow_html=True)



# Use Streamlit form to replicate your design
with st.form("contact_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name *", "")
    with col2:
        email = st.text_input("Email *", "")

    subject = st.text_input("Subject")
    message = st.text_area("Write your message...", height=200)

    submit_button = st.form_submit_button("Send Message")

    if submit_button:
        if name and email and message:
            try:
                # Compose email
                msg = MIMEMultipart()
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = EMAIL_ADDRESS  # Send it to yourself
                msg['Subject'] = subject if subject else "No Subject"
                
                body = f"""
You received a new message from your contact form:

Name: {name}
Email: {email}
Subject: {subject}
Message:
{message}
"""
                msg.attach(MIMEText(body, 'plain'))

                # Send email
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    server.send_message(msg)

                st.success("✅ Your message has been sent successfully!")
            except Exception as e:
                st.error(f"❌ Failed to send email: {e}")
        else:
            st.warning("⚠️ Please fill in all required fields (Name, Email, Message).")
# Custom Dark Minimal Styling
st.markdown("""
<style>
form {
  background: #121212;
  padding: 40px;
  border-radius: 10px;
  max-width: 800px;
  margin: 50px auto;
  font-family: 'Segoe UI', 'Roboto', sans-serif;
  color: #fff;
}

.row {
  display: flex;
  gap: 20px;
  margin-bottom: 25px;
}

.row-full {
  width: 100%;
  margin-bottom: 25px;
}

input[type="text"], input[type="email"], textarea {
  width: 100%;
  padding: 10px 5px;
  border: none;
  border-bottom: 2px solid #444;
  background: transparent;
  color: #fff;
  font-size: 16px;
  transition: border-color 0.3s;
}

input[type="text"]:focus, input[type="email"]:focus, textarea:focus {
  border-bottom: 2px solid #00BFFF;
  outline: none;
}

textarea {
  resize: vertical;
}

.submit-container {
  text-align: left;
}

button[type="submit"] {
  background: #00BFFF;
  color: #fff;
  padding: 12px 30px;
  border: none;
  border-radius: 25px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.3s ease;
}

button[type="submit"]:hover {
  background: #1E90FF;
}
</style>
""", unsafe_allow_html=True)

# Separator Line
st.markdown("""
<hr style="
border: 0;
height: 2px;
background: linear-gradient(to right, #ff5858, #f09819);
">
""" , unsafe_allow_html=True)


# Social Media Contact Links
st.markdown("""
<h3 style='text-align: center;'>🌐 Connect With Me</h3>

<div style='text-align: center;'>
    <a href='https://www.linkedin.com/in/ayushman-anupam' target='_blank'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'>
    </a>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <a href='https://github.com/AyushmanGHub' target='_blank'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'>
    </a>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <a href='mailto:ayushmantutu@gmail.com' target='_blank'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'>
    </a>
</div>

<br>

<div style='text-align: center; font-size: 18px;'>
<br>
🤝 <b>Let’s collaborate and grow together!</b><br>
I am passionate about <b>continuous learning</b>, <b>collaboration</b>, and applying <b>data science & AI</b> for real-world impact.
Whether you're interested in data-driven projects, machine learning applications, or simply exchanging ideas — feel free to reach out.<br><br>
💡 <i> Together, let's learn, build, and create impact.</i> 
</div>
""", unsafe_allow_html=True)



st.markdown("")
st.markdown("""
<hr style="
border: 0;
height: 2px;
background: linear-gradient(to right, #ff5858, #f09819);
">
""" , unsafe_allow_html=True)
