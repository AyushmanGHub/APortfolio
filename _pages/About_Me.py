import streamlit as st
import streamlit.components.v1 as components

st.markdown("""
    <style>
    button[title="View fullscreen"] {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)
st.title("👤 About Me")

# Divider line
st.markdown("""
<hr style="
border: 0;
height: 2px;
background: linear-gradient(to right, #ff5858, #f09819);
">
""" , unsafe_allow_html=True)
st.markdown("")
# 2 column layout
col1, col2 = st.columns([1, 1])

# Left Column: Image
# with col1:
#     st.image("images/ProfileImage.jpeg", use_column_width=True, output_format='auto')
with col1:
    # Divide col1 into 3 sub-columns
    sub_col1, sub_col2, sub_col3 = st.columns([1, 4, 1])

    # Place image inside center sub-column
    with sub_col2:
        st.image("images/ProfileImage.webp", width=370)


with col2:
    st.markdown("<h3 style='font-size: 50px;'>Hi, I'm Ayushman</h3>", unsafe_allow_html=True)

    components.html("""
        <div style="font-size:25px; font-weight:bold; color:#4CAF50; font-family:sans-serif; margin:0; padding:0;">
            <span id="typed-text"></span>
        </div>

        <script>
        const texts = ["Data Scientist", "Philomath"];
        let count = 0;
        let index = 0;
        let currentText = '';
        let letter = '';

        function type() {
            if (count === texts.length) {
                count = 0;
            }
            currentText = texts[count];
            letter = currentText.slice(0, ++index);

            document.getElementById('typed-text').textContent = letter;
            if (letter.length === currentText.length) {
                setTimeout(() => {
                    index = 0;
                    count++;
                    setTimeout(type, 500);
                }, 1000);
            } else {
                setTimeout(type, 100);
            }
        }

        type();
        </script>
    """, height=50)  # further reduced height for minimal gap


    st.markdown(
        "<div style='text-align: left; margin-left: 10px; margin-top:1px;'>"
        "<a href='https://www.linkedin.com/in/ayushman-anupam' style='margin-right:20px;'>"
        "<img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='45' height='36'>"
        "</a>"
        "<a href='https://github.com/AyushmanGHub' style='margin-right:20px;'>"
        "<img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='45' height='36'>"
        "</a>"
        "<a href='mailto:ayushmantutu@gmail.com' style='margin-right:20px;'>"
        "<img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='45' height='36'>"
        "</a>"
        "</div>"
        "<div style='text-align: left; margin-left: 10px; margin-top: 20px;'>"
        "<a href='https://drive.google.com/file/d/13fhhQG4FL9JnFIW3oZwbtJI0Yd4BzzF7/view?usp=drive_link' target='_blank'>"
        "<button style='"
        "background-color: #4CAF50;"
        "color: white;"
        "padding: 10px 32px;"
        "border: none;"
        "border-radius: 10px;"
        "font-size: 18px;"
        "cursor: pointer;"
        "box-shadow: 0 5px 10px rgba(0,0,0,0.25);"
        "transition: 0.3s;"
        "'>"
        "📄 My Resume"
        "</button>"
        "</a>"
        "</div>"
        ,
        unsafe_allow_html=True,
    )




st.markdown("---")

st.markdown("""
<div style="font-size: 18px; text-align: justify;">
Hi, I'm <b>Ayushman Anupam</b>, a Data Science student who loves working with data, solving real-world problems, and continuously exploring how mathematics, statistics, and AI can be used to make meaningful impact.

Coming from a Mathematics background has helped me develop deep interests in <b>Machine Learning, Graph Theory, Statistical Modeling, and Agentic AI</b>. I'm particularly excited about building intelligent systems that turn data into actionable insights.

Currently, I am exploring the world of finance, specifically the role of time series analysis in financial markets, equity, and related domains. ALong, with it I am Working on a Time-Series project to automates real-time stock market analysis and forecasting some Indian Stocks and Indexes by integrating data fetching, feature engineering, predictive modeling, and visualization.</div>
""", unsafe_allow_html=True)
