import streamlit as st

st.title("💼 Experience")
st.markdown("### A quick glance at my professional journey!")

st.markdown("""
<hr style="
border: 0;
height: 2px;
background: linear-gradient(to right, #ff5858, #f09819);
">
""", unsafe_allow_html=True)


# --- Agentic AI Intern ---
with st.container():
    st.success("Agentic AI Intern | AlgoLab - Internship")
    st.write("*May 2025 - July 2025* | *India - Remote*")
    st.markdown("""
    During my internship at AlgoLab, I Worked on Agentic AI System to automate task.  
    Mainly I worked on smart Agentic-AI framework that converts lecture videos into interactive learning experiences, providing a personalized chatbot, mind map, notes, and other materials for enhanced engagement and effectiveness. This Agentic-AI tool enhances learning experiences and saves learners 30–50% of their time through personalized, automated academic support.
    """)
st.markdown("---")

# --- Mathematics Tutor ---
with st.container():
    st.info("Mathematics Tutor | Gyan Education Center, Jamshedpur")
    st.write("*Apr 2021 - Dec 2024* | *Hybrid*")
    st.markdown("""
    I worked as a part-time mathematics tutor, helping students from **Class 9 to Class 12**, as well as those preparing for competitive exams like **JEE Mains, JEE Advanced, and other entrance exams**.  
    """)
st.markdown("---")

# --- Data Scientist ---
with st.container():
    st.warning("Data Scientist | COTHON SOLUTIONS - Internship")
    st.write("*Dec 2024 - Dec 2024* | *India - Remote*")
    st.markdown("""
    At COTHON Solutions, I had worked on real-world **data science problems** in a business context.  
    My responsibilities included building predictive models for **churn prediction, credit risk scoring, customer segmentation, and recommendation systems**.  
    I utilized tools such as **Python, machine learning algorithms, and data visualization techniques** to transform raw data into valuable business insights and supported decision-making processes for clients.
    """)
st.markdown("---")

# --- Finance & Stock Market Internship ---
with st.container():
    st.error("Finance & Stock Market Trainee | Capital Vision Investment")
    st.write("*Nov 2024 - Dec 2024* | *India - Remote*")
    st.markdown("""
    This internship allowed me to explore the world of **financial markets and investment management**.  
    I assisted in **portfolio management, risk assessment, and equity analysis**, while also gaining exposure to financial instruments like **mutual funds, NPS, fixed deposits, and tax-efficient investment strategies**.  
    This experience helped me build a solid foundation in both traditional and modern investment approaches.
    """)
st.markdown("---")
