import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
st.set_page_config(
    page_title="Ayushman's Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="auto",
)
with st.sidebar:
    choose = option_menu(
        "Ayushman Anupam",
        [
            "ResAgent",
            "About Me",
            "Experience",
            "Education",
            "Projects",
            "Certifications",
            "Volunteering",
            "Blog",
            "Contact me",
        ],
        menu_icon="🎓",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0D1117"},
            "icon": {"color": "darkorange", "font-size": "20px"},
            "nav-link": {
                "font-size": "17px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#1F2937",
            },
            "nav-link-selected": {"background-color": "#A41117"},
        },
    )

    st.markdown(
        "<div style='text-align: center;'>"
        "<a href='https://www.linkedin.com/in/ayushman-anupam'>"
        "<img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'>"
        "</a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='https://github.com/AyushmanGHub'>"
        "<img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'>"
        "</a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='mailto:ayushmantutu@gmail.com'>"
        "<img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'>"
        "</a>"
        "</div>"
        "<div style='text-align: center; margin-top: 20px;'>"
        "<a href='https://drive.google.com/file/d/13fhhQG4FL9JnFIW3oZwbtJI0Yd4BzzF7/view?usp=drive_link' target='_blank'>"
        "<button style='background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px; cursor: pointer; box-shadow: 0 4px 8px rgba(0,0,0,0.2); transition: 0.3s;'>"
        "📄 My Resume"
        "</button>"
        "</a>"
        "</div>",
        unsafe_allow_html=True,
    )

# Mapping to module imports
pages = {
    "ResAgent": "_pages.ResAgent",
    "About Me": "_pages.About_Me",
    "Experience": "_pages.Experience",
    "Education": "_pages.Education",
    "Projects": "_pages.Projects",
    "Certifications": "_pages.Certifications",
    "Volunteering": "_pages.Volunteering",
    "Blog": "_pages.Blog",
    "Contact me": "_pages.Contact",
}

# Dynamically load the selected page
page_file = pages.get(choose)
if page_file:
    # Convert dot notation to path
    page_path = Path(page_file.replace(".", "/") + ".py")

    if page_path.exists():
        with open(page_path, encoding="utf-8") as file:
            exec(file.read())
    else:
        st.error(f"❌ Page not found: {page_path}")
