import streamlit as st

# Hide fullscreen button
st.markdown("""
<style>
button[title="View fullscreen"] {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

st.markdown("# 🤝 **Volunteering**")

# Top divider
st.markdown("""
<hr style="
border: 0;
height: 2px;
background: linear-gradient(to right, #ff5858, #f09819);
">
""", unsafe_allow_html=True)


# Helper to avoid repeat code
def render_experience(img_path, caption, org_html, org_about, role_title, role_bullets):
    col1, col2 = st.columns([1, 1])

    with col1:
        upper_left, upper_right = st.columns([1, 2])
        with upper_left:
            st.image(img_path, use_container_width=True, output_format="webp", caption=caption)
        with upper_right:
            st.markdown(org_html, unsafe_allow_html=True)
        st.markdown("##### About the Organization")
        st.markdown(org_about)

    with col2:
        st.markdown(role_title)
        st.markdown(role_bullets)

    st.markdown("---")


# ---- Experience 1 ----
render_experience(
    img_path="images/mali_kalyan.webp",
    caption="Mali (Malakar) Kalyan Samiti",
    org_html="""
        ### Mali (Malakar) Kalyan Samiti  
        #### Jamshedpur, Jharkhand  
        📅 **Dec 2020 - Present**
    """,
    org_about="""
        The Mali (Malakar) Kalyan Samiti is a registered community welfare organization based in Jamshedpur, Jharkhand, dedicated to social development, community engagement, and welfare initiatives. The organization is conducting a variety of programs such as cleanliness drives, blood donation camps, and other activities to promote social responsibility and community well-being.
    """,
    role_title="#### Active Member - Social Service Worker",
    role_bullets="""
    * Actively participating in cleanliness programs to promote environmental hygiene and raise awareness about public sanitation.  
    * Assisting in organizing blood donation camps, managing donor coordination, and encouraging voluntary blood donation.  
    * Contributing to multiple social welfare initiatives, supporting the organization's mission to uplift and serve the local community.
    """
)

# ---- Experience 2 ----
render_experience(
    img_path="images/gramin_muskan.webp",
    caption="Gramin Muskan Seva Sansthan",
    org_html="""
        ### Gramin Muskan Seva Sansthan  
        #### Jamshedpur, Jharkhand  
        📅 **May 2024 – June 2024**
    """,
    org_about="""
        Gramin Muskan Seva Sansthan is a registered community welfare NGO with branches across India. The organization is dedicated to supporting farmers, promoting rural development, and empowering communities through education, awareness programs, and government welfare initiatives.
    """,
    role_title="#### Volunteer - Social Service Worker",
    role_bullets="""
    * Conducted computer literacy sessions for students in rural areas, helping them develop basic digital skills and increase technology awareness.  
    * Assisted in organizing workshops and training programs for farmers to educate them about government schemes, modern agricultural techniques, and available support resources.  
    * Coordinated with government officials to facilitate the implementation of rural development projects, including solar-powered water pumps and solar street lighting.  
    * Participated in cleanliness and sanitation drives to promote hygiene and address key community issues.
    """
)

# ---- Experience 3 ----
render_experience(
    img_path="images/vbda.webp",
    caption="Voluntary Blood Donors Association",
    org_html="""
        ### Voluntary Blood Donors Association  
        #### Jharkhand  
        📅 **June 2023**
    """,
    org_about="""
        The Voluntary Blood Donors Association (VBDA) is a non-governmental organization based in Jharkhand, India, dedicated to promoting voluntary blood donation. The organization conducts regular blood donation camps, organizes workshops to spread awareness, and actively works to encourage safe and regular blood donation practices within the community.
    """,
    role_title="#### Volunteer",
    role_bullets="""
    * Volunteered at blood donation camps organized by the NGO, assisting with coordination, registration, and donor support.  
    * Participated in awareness programs across multiple educational institutes to promote the importance of voluntary blood donation and educate individuals on the process and benefits of donating blood.  
    * Engaged in bloodcare initiatives, focusing on creating a sustainable blood donation ecosystem by motivating first-time donors, following up with regular donors, and supporting emergency donation drives.
    """
)