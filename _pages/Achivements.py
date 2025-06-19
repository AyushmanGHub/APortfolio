import streamlit as st


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