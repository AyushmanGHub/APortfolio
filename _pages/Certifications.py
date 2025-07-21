import streamlit as st
#######################################################################

st.markdown("# 🏅 Certifications")
st.markdown("<hr style='border: 0; height: 2px; background: linear-gradient(to right, #ff5858, #f09819);'>", unsafe_allow_html=True)
st.markdown("")
st.markdown("")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Specialization: Risk Management")
    certificate_link = "https://www.coursera.org/account/accomplishments/specialization/092Q7MA12JU5"
    cert_html = f"""
    <div style='display: inline-block;'>
        <a href="{certificate_link}" target="_blank">
            <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Certificate</button>
        </a>
    </div>
    """
    st.markdown(cert_html, unsafe_allow_html=True)

    st.markdown("""
        **By:** New York Institute of Finance <br>
        A 4-course specialization teaching risk identification, measurement and mitigation frameworks across credit, market and operational risk domains with applied Excel projects.
    """, unsafe_allow_html=True)

with col2:
    st.markdown("#### Specialization: Preparatory Certificate in Finance and Financial Markets")
    github_link = "https://github.com/AyushmanGHub/Preparatory-Certificate-in-Finance-and-Financial-Markets"
    certificate_link = "https://www.coursera.org/account/accomplishments/specialization/HU4XXTZZTVRM"
    github_html = f"""
    <div style='display: inline-block; margin-right: 10px;'>
        <a href="{github_link}" target="_blank">
            <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
        </a>
    </div>
    """
    cert_html = f"""
    <div style='display: inline-block;'>
        <a href="{certificate_link}" target="_blank">
            <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Certificate</button>
        </a>
    </div>
    """
    st.markdown(github_html + cert_html, unsafe_allow_html=True)

    st.markdown("""
        **By:** Corporate Finance Institute <br>
        A 10-course preparatory program covering corporate finance, accounting, financial statement analysis, capital markets, banking, credit, risk management, and ESG fundamentals.
    """, unsafe_allow_html=True)

with col3:
    st.markdown("#### Specialization: Financial Markets")
    certificate_link = "https://www.coursera.org/account/accomplishments/certificate/E3HH2L1I5SNQ"
    cert_html = f"""
    <div style='display: inline-block;'>
        <a href="{certificate_link}" target="_blank">
            <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Certificate</button>
        </a>
    </div>
    """
    st.markdown(cert_html, unsafe_allow_html=True)

    st.markdown("""
        **By:** Yale University <br>
        Introductory course explaining how financial markets operate, covering risk management, behavioral finance, asset valuation, insurance, and market institutions with real-world examples.
    """, unsafe_allow_html=True)
st.markdown("---")
#######################################################################
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Specialization: PyTorch Ultimate 2024 - From Basics to Cutting-Edge")
    
    github_link = "https://github.com/AyushmanGHub/PyTorch-Ultimate-2024---From-Basics-to-Cutting-Edge-Specialization"
    certificate_link = "https://www.coursera.org/account/accomplishments/specialization/FNOET4QE7H6S"

    github_html = f"""
    <div style='display: inline-block; margin-right: 10px;'>
        <a href="{github_link}" target="_blank">
            <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
        </a>
    </div>
    """

    cert_html = f"""
    <div style='display: inline-block;'>
        <a href="{certificate_link}" target="_blank">
            <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Certificate</button>
        </a>
    </div>
    """

    st.markdown(github_html + cert_html, unsafe_allow_html=True)

    st.markdown("""
        **By:** Packt <br>
        Specialization mastering PyTorch through regression, CNNs, GANs, NLP, recommender systems and Transformer models, with hands‑on coding tasks and deployment techniques.
    """, unsafe_allow_html=True)

with col2:
    st.markdown("#### Specialization: TensorFlow Developer Professional Certificate")
    
    github_link = "https://github.com/AyushmanGHub/DeepLearning.AI-TensorFlow-Developer-Professional-Certificate"
    certificate_link = ""  # no cert link provided

    github_html = f"""
    <div style='display: inline-block; margin-right: 10px;'>
        <a href="{github_link}" target="_blank">
            <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
        </a>
    </div>
    """

    st.markdown(github_html, unsafe_allow_html=True)

    st.markdown("""
        **By:** DeepLearning.AI <br>
        Four-course professional program teaching TensorFlow for scalable AI apps: from basic neural networks and CNNs to NLP and time-series models with real-world Python projects.
    """, unsafe_allow_html=True)

st.markdown("---")
########################################################################

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Specialization: Master Microsoft Office 365 and Power Platform")
    
    github_link = "https://github.com/AyushmanGHub/Master-Microsoft-Office-365-and-Power-Platform"
    certificate_link = "https://www.coursera.org/account/accomplishments/specialization/EQBV3Y130YLW"

    github_html = f"""
    <div style='display: inline-block; margin-right: 10px;'>
        <a href="{github_link}" target="_blank">
            <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
        </a>
    </div>
    """

    cert_html = f"""
    <div style='display: inline-block;'>
        <a href="{certificate_link}" target="_blank">
            <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Certificate</button>
        </a>
    </div>
    """

    st.markdown(github_html + cert_html, unsafe_allow_html=True)
    
    st.markdown("""
        **By:** Microsoft <br>
        Specialization spanning 8 courses—covering advanced Word, Excel, PowerPoint, plus Power Platform tools (Power Apps, Power BI, Power Automate, Power Virtual Agents)—for building business solutions.
    """,
    unsafe_allow_html=True)
    
st.markdown("---")

##########################################################################

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Specialization: Machine Learning")
    
    certificate_link = "https://www.coursera.org/account/accomplishments/specialization/J9HTPYMFYSYD"
    cert_html = f"""
    <div style='display: inline-block;'>
        <a href="{certificate_link}" target="_blank">
            <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Certificate</button>
        </a>
    </div>
    """
    st.markdown(cert_html, unsafe_allow_html=True)

    st.markdown("""
        **By:** DeepLearning.AI & Stanford University <br>
        Foundational 3-course program taught by Andrew Ng covering supervised and unsupervised learning, decision trees, neural networks, recommender systems, and reinforcement learning.
    """, unsafe_allow_html=True)

st.markdown("---")
##########################################################################

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Course: Cloud Computing Fundamentals")
    
    badge_link = "https://www.credly.com/badges/42990cb9-04ac-42ed-9093-45745c320733/linked_in_profile"
    badge_html = f"""
    <div style='display: inline-block;'>
        <a href="{badge_link}" target="_blank">
            <button style='background-color:#f36f21; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Badge</button>
        </a>
    </div>
    """
    st.markdown(badge_html, unsafe_allow_html=True)

    st.markdown("""
        **By:** IBM <br>
        Introductory course on cloud computing models, deployment architectures, virtualization, storage, security, and key providers including AWS, Azure, and IBM Cloud.
    """, unsafe_allow_html=True)

st.markdown("---")
##############################################################################
col1, col2, col3 = st.columns(3)

# ================= Course 1: Python for Data Science =====================
with col1:
    st.markdown("#### Course: Python for Data Science")
    
    certificate_link = "https://courses.cognitiveclass.ai/certificates/570eda94251342af92f96512bf29cf54"
    
    cert_html = f"""
    <div style='display: inline-block;'>
        <a href="{certificate_link}" target="_blank">
            <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Certificate</button>
        </a>
    </div>
    """
    
    st.markdown(cert_html, unsafe_allow_html=True)

    st.markdown("""
        **By:** IBM Developer Skills Network <br>
        Introduction to Python programming with focus on data analysis, working with libraries like NumPy, Pandas, and visualization using Matplotlib.
    """, unsafe_allow_html=True)

# ================= Course 2: Data Visualization with Python =====================
with col2:
    st.markdown("#### Course: Data Visualization with Python")
    
    certificate_link = "https://courses.cognitiveclass.ai/certificates/ac9c90734df74fbc8fce2fdc4709116d"
    
    cert_html = f"""
    <div style='display: inline-block;'>
        <a href="{certificate_link}" target="_blank">
            <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Certificate</button>
        </a>
    </div>
    """
    
    st.markdown(cert_html, unsafe_allow_html=True)

    st.markdown("""
        **By:** IBM Developer Skills Network <br>
        Course on creating advanced data visualizations using Python libraries like Matplotlib, Seaborn, Folium, and dashboards for data storytelling.
    """, unsafe_allow_html=True)

# ================= Course 3: Data Analysis with Python =====================
with col3:
    st.markdown("#### Course: Data Analysis with Python")
    
    certificate_link = "https://courses.cognitiveclass.ai/certificates/fdefea79298e4f3c98372d054487132e"
    
    cert_html = f"""
    <div style='display: inline-block;'>
        <a href="{certificate_link}" target="_blank">
            <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Certificate</button>
        </a>
    </div>
    """
    
    st.markdown(cert_html, unsafe_allow_html=True)

    st.markdown("""
        **By:** IBM Developer Skills Network <br>
        Comprehensive course covering data manipulation, data cleaning, statistical analysis, regression, and hypothesis testing using Python and Pandas.
    """, unsafe_allow_html=True)

st.markdown("---")
###########################################################################

col1, col2, col3 = st.columns(3)

# ================= Course 1: DSA (Udemy) =====================
with col1:
    st.markdown("#### Course: Data Structures Algorithm DSA")
    
    certificate_link = "https://www.udemy.com/certificate/UC-43416d08-2126-4765-ab0e-fe3c43079e44/"
    
    cert_html = f"""
    <div style='display: inline-block;'>
        <a href="{certificate_link}" target="_blank">
            <button style='background-color:#a435f0; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Certificate</button>
        </a>
    </div>
    """
    
    st.markdown(cert_html, unsafe_allow_html=True)

    st.markdown("""
        **By:** Udemy <br>
        Comprehensive course on data structures and algorithms covering arrays, linked lists, stacks, queues, trees, graphs, searching, sorting, recursion, and problem solving.
    """, unsafe_allow_html=True)

# ================= Course 2: Crash Course on Python (Google) =====================
with col2:
    st.markdown("#### Course: Crash Course on Python")
    
    certificate_link = "https://www.coursera.org/account/accomplishments/verify/3EF9B9G3C6PU"
    
    cert_html = f"""
    <div style='display: inline-block;'>
        <a href="{certificate_link}" target="_blank">
            <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Certificate</button>
        </a>
    </div>
    """
    
    st.markdown(cert_html, unsafe_allow_html=True)

    st.markdown("""
        **By:** Google <br>
        Beginner-friendly Python course covering variables, functions, loops, strings, lists, dictionaries, error handling, object-oriented programming, and file operations.
    """, unsafe_allow_html=True)

st.markdown("---")
########################################################################
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Course: SQL Complete Bootcamp From Basics to Advanced")
    
    github_link = "https://github.com/AyushmanGHub/SQL-and-RDBMS"
    certificate_link = "http://udemy.com/certificate/UC-f31749b2-56a8-45ac-b068-fa762fe21603/"

    github_html = f"""
    <div style='display: inline-block; margin-right: 10px;'>
        <a href="{github_link}" target="_blank">
            <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
        </a>
    </div>
    """

    cert_html = f"""
    <div style='display: inline-block;'>
        <a href="{certificate_link}" target="_blank">
            <button style='background-color:#a435f0; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Certificate</button>
        </a>
    </div>
    """

    st.markdown(github_html + cert_html, unsafe_allow_html=True)

    st.markdown("""
        **By:** Udemy <br>
        Comprehensive SQL course covering relational databases, SQL queries, joins, aggregations, subqueries, indexes, transactions, stored procedures, and advanced query optimization.
    """, unsafe_allow_html=True)

st.markdown("---")
########################################################################
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Course: Young Professional Course")
    
    certificate_link = "https://www.linkedin.com/in/ayushman-anupam/details/certifications/1724612065578/single-media-viewer/?profileId=ACoAADMRVUgBVbNJxN5sizRuxBO81TJZtCKoK6Q"
    
    cert_html = f"""
    <div style='display: inline-block;'>
        <a href="{certificate_link}" target="_blank">
            <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Certificate</button>
        </a>
    </div>
    """
    
    st.markdown(cert_html, unsafe_allow_html=True)

    st.markdown("""
        **By:** TCS iON Career Edge <br>
        Professional development course covering business etiquette, communication skills, interview preparation, resume building, corporate ethics, and workplace readiness.
    """, unsafe_allow_html=True)

st.markdown("---")

################################################################################################################################################

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Specialization: Reinforcement Learning")
    
    github_link = "https://github.com/AyushmanGHub/Coursera_Reinforcement-Learning-Specialization"
    certificate_link = "https://www.coursera.org/account/accomplishments/specialization/9BR3UHYUV4HP"

    github_html = f"""
    <div style='display: inline-block; margin-right: 10px;'>
        <a href="{github_link}" target="_blank">
            <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
        </a>
    </div>
    """

    cert_html = f"""
    <div style='display: inline-block;'>
        <a href="{certificate_link}" target="_blank">
            <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Certificate</button>
        </a>
    </div>
    """

    st.markdown(github_html + cert_html, unsafe_allow_html=True)
    
    st.markdown("""
        **By:** University of Alberta <br>
        Specialization exploring foundational reinforcement learning concepts such as prediction, control, value functions, policy gradients, and function approximation using practical coding assignments.
    """,
    unsafe_allow_html=True)


with col2:
    st.markdown("#### Course: Game Theory")
    
    certificate_link = "https://www.coursera.org/account/accomplishments/verify/ED7J4U64XKYZ"
    
    cert_html = f"""
    <div style='display: inline-block;'>
        <a href="{certificate_link}" target="_blank">
            <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Certificate</button>
        </a>
    </div>
    """
    
    st.markdown(cert_html, unsafe_allow_html=True)

    st.markdown("""
        **By:** The University of British Columbia & Stanford University <br>
        Introductory course explaining strategic decision-making using game theory concepts such as Nash equilibrium, auctions, Bayesian games, bargaining, and mixed strategies.
    """, unsafe_allow_html=True)

    