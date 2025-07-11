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
    st.success("🚀 Agentic AI Intern | AlgoLab - Internship")
    st.write("*May 2025 - Present* | *India - Remote*")
    st.markdown("""
    During my current internship at AlgoLab, I'm actively contributing to the exciting world of **Agentic AI**.  
    My work involves building autonomous AI systems capable of reasoning, planning, and automating complex tasks using modern frameworks like **RAG pipelines, Langgraph, advanced databases, and multi-agent systems**.  
    One of my most rewarding projects is developing a **personal Lecture Assistant** that leverages agent-based AI for intelligent academic support.
    """)
st.markdown("---")

# --- Mathematics Tutor ---
with st.container():
    st.info("📚 Mathematics Tutor | Gyan Education Center, Jamshedpur")
    st.write("*Apr 2021 - Apr 2025* | *Hybrid*")
    st.markdown("""
    Over these four years, I have worked as a part-time mathematics tutor, helping students from **Class 9 to Class 12**, as well as those preparing for competitive exams like **JEE Mains, JEE Advanced, and other entrance exams**.  
    I developed customized lesson plans, simplified complex mathematical concepts, and guided students to improve both their problem-solving skills and exam performance.
    """)
st.markdown("---")

# --- Data Scientist ---
with st.container():
    st.warning("📊 Data Scientist | COTHON SOLUTIONS - Internship")
    st.write("*Dec 2024 - Dec 2024* | *India - Remote*")
    st.markdown("""
    At COTHON Solutions, I had the opportunity to work on real-world **data science problems** in a business context.  
    My responsibilities included building predictive models for **churn prediction, credit risk scoring, customer segmentation, and recommendation systems**.  
    I utilized tools such as **Python, machine learning algorithms, and data visualization techniques** to transform raw data into valuable business insights and supported decision-making processes for clients.
    """)
st.markdown("---")

# --- Finance & Stock Market Internship ---
with st.container():
    st.error("💹 Finance & Stock Market Trainee | Capital Vision Investment")
    st.write("*Nov 2024 - Dec 2024* | *India - Remote*")
    st.markdown("""
    This internship allowed me to explore the world of **financial markets and investment management**.  
    I assisted in **portfolio management, risk assessment, and equity analysis**, while also gaining exposure to financial instruments like **mutual funds, NPS, fixed deposits, and tax-efficient investment strategies**.  
    This experience helped me build a solid foundation in both traditional and modern investment approaches.
    """)
st.markdown("---")
