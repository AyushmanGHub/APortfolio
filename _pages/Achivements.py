import streamlit as st

st.title("Volunteering And Achievements")
tab1, tab2 = st.tabs(["SPYM", "NSS"])
with tab1:
    st.subheader("Socity for Promotion of Youth and Masses (SPYM)")
    st.write(
        "SPYM operates at both state and national levels, focusing on drug prevention and rehabilitation for children and youth, healthcare (reproductive and sexual health, HIV/AIDS), life-skills and education for street children, community development, and training and research."
    )
    st.markdown(
    """
    #### Volunteer at SPYM Darjeeling 2019-Present
    ## Role
    - Part of awareness in drug and alcohol abuse prevention in different educational institutions and societies in and around Darjeeling.
    - Organized a special workshop for workers and recovery clients on MS Office and the basics of a computer.
    - Developed and maintained their official website. (2020-2021)
    - Engaged in healthcare initiatives, focusing on sexual health, as well as HIV/AIDS prevention and awareness.
    """
)
with tab2:
    st.subheader("National Service Scheme (NSS)")
    st.write(
        "National Service Scheme (NSS) is a public service program under the Ministry of Youth Affairs and Sports of the Government of India. It was launched in Gandhiji's Centenary year, 1969, aimed at developing student's personality through community service."
    )
    st.markdown(
    """
    #### President of NSS Unit, Sikkim Manipal Institute of Technology (SMIT) 2022-2023
    ## Role
    - Organize monthly activities and awareness campaigns on various social issues.
    - Coordinate monthly health camps and promote basic hygiene awareness in different societies across Sikkim.
    - Establish operation strategies within the team to enhance club effectiveness.
    - Initiate eco-friendly projects such as tree planting drives and waste management awareness programs.
    - Coordinate with local NGOs and government bodies for collaborative community service projects.
    """
)

# Section: Achievements
st.markdown("# 🎯 Achievements")
st.markdown("---")
# Achievements data
achievements = [
    ("GATE 2024 (Statistics)", "AIR 271"),
    ("Indian Statistical Institute (ISI) MS QMS 2024 Entrance Exam", "Rank 1"),
    ("JEE Mains, 2020", "All India Rank - 4652"),
    ("JEE Advance, 2020", "All India Rank - 7658")
]


# Loop and print without boxes
for i, (exam, rank) in enumerate(achievements):
    color = "#1E88E5"
    text_html = f"""
    <div style='margin-bottom: 15px;'>
        <h5 style='margin: 0; padding: 0; color: {color};'>{exam}</h5>
        <p style='margin: 4px 0 0 0; font-size: 13px; color: #aaa;'><b>{rank}</b></p>
    </div>
    """
    st.markdown(text_html, unsafe_allow_html=True)