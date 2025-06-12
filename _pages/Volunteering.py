import streamlit as st

# Global style to hide fullscreen button
st.markdown("""
    <style>
    button[title="View fullscreen"] {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("# 🤝 **Volunteering**")

# Top Divider
st.markdown("""
<hr style="
border: 0;
height: 2px;
background: linear-gradient(to right, #ff5858, #f09819);
">
""" , unsafe_allow_html=True)
st.markdown("")
######################### Experience 1: Mali (Malakar) Kalyan Samiti #########################
col1, col2 = st.columns([1, 1])

# Left Column (Organization Info)
with col1:
    # Upper Part: Image + Name & Date
    upper_left, upper_right = st.columns([1, 2])
    with upper_left:
        st.image(r"images/mali_kalyan.png", use_container_width=True, caption="Mali (Malakar) Kalyan Samiti")

    with upper_right:
        st.markdown(""" 
            ## Mali (Malakar) Kalyan Samiti
            ### Jamshedpur, Jharkhand
            📅 **Dec 2020 - Present**
            """, unsafe_allow_html=True)

    # Lower Part: About the Organization
    st.markdown("#### About the Organization")
    st.markdown("""
        The Mali (Malakar) Kalyan Samiti is a registered community welfare organization based in Jamshedpur, Jharkhand, dedicated to social development, community engagement, and welfare initiatives. The organization is conducting a variety of programs such as cleanliness drives, blood donation camps, and other activities to promote social responsibility and community well-being.
    """)

# Right Column (Role & Work)
with col2:
    st.markdown("#### Active Member - Social Service Worker")
    st.markdown("""
    * Actively participating in cleanliness programs to promote environmental hygiene and raise awareness about public sanitation.
    * Assisting in organizing blood donation camps, managing donor coordination, and encouraging voluntary blood donation.
    * Contributing to multiple social welfare initiatives, supporting the organization's mission to uplift and serve the local community.
    """)

st.markdown("---")

######################### Experience 2: Gramin Muskan Seva Sansthan #########################
col1, col2 = st.columns([1, 1])

with col1:
    upper_left, upper_right = st.columns([1, 2])
    with upper_left:
        st.image(r"images/gramin_muskan.png", use_container_width=True, caption="Gramin Muskan Seva Sansthan")

    with upper_right:
        st.markdown(""" 
            ## Gramin Muskan Seva Sansthan
            ### Jamshedpur, Jharkhand
            📅 **May 2024 – June 2024**
            """, unsafe_allow_html=True)

    st.markdown("#### About the Organization")
    st.markdown("""
        Gramin Muskan Seva Sansthan is a registered community welfare NGO with branches across India. The organization is dedicated to supporting farmers, promoting rural development, and empowering communities through education, awareness programs, and government welfare initiatives.
    """)

with col2:
    st.markdown("#### Volunteer - Social Service Worker")
    st.markdown("""
    * Conducted computer literacy sessions for students in rural areas, helping them develop basic digital skills and increase technology awareness.
    * Assisted in organizing workshops and training programs for farmers to educate them about government schemes, modern agricultural techniques, and available support resources.
    * Coordinated with government officials to facilitate the implementation of rural development projects, including solar-powered water pumps and solar street lighting.
    * Participated in cleanliness and sanitation drives to promote hygiene and address key community issues.
    """)

st.markdown("---")

######################### Experience 3: Voluntary Blood Donors Association #########################
col1, col2 = st.columns([1, 1])

with col1:
    upper_left, upper_right = st.columns([1, 2])
    with upper_left:
        st.image(r"images/vbda.png", use_container_width=True, caption="Voluntary Blood Donors Association")

    with upper_right:
        st.markdown(""" 
            ## Voluntary Blood Donors Association
            ### Jharkhand
            📅 **June 2023**
            """, unsafe_allow_html=True)

    st.markdown("#### About the Organization")
    st.markdown("""
        The Voluntary Blood Donors Association (VBDA) is a non-governmental organization based in Jharkhand, India, dedicated to promoting voluntary blood donation. The organization conducts regular blood donation camps, organizes workshops to spread awareness, and actively works to encourage safe and regular blood donation practices within the community.
    """)

with col2:
    st.markdown("#### Volunteer")
    st.markdown("""
    * Volunteered at blood donation camps organized by the NGO, assisting with coordination, registration, and donor support.
    * Participated in awareness programs across multiple educational institutes to promote the importance of voluntary blood donation and educate individuals on the process and benefits of donating blood.
    * Engaged in bloodcare initiatives, focusing on creating a sustainable blood donation ecosystem by motivating first-time donors, following up with regular donors, and supporting emergency donation drives.
    """)

st.markdown("""
<hr style="
border: 0;
height: 2px;
background: linear-gradient(to right, #ff5858, #f09819);
">
""" , unsafe_allow_html=True)
