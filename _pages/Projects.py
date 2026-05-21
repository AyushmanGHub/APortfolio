import streamlit as st


st.markdown("""
    <style>
    button[title="View fullscreen"] {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("# 🧠 Projects")
st.markdown("")
st.markdown("""
    <hr style="
    border: 0;
    height: 2px;
    background: linear-gradient(to right, #ff5858, #f09819);
    ">
    """, unsafe_allow_html=True)
st.markdown("")
st.markdown("")
###################################################################################################

col_working, _ = st.columns([3,1])

# ========================= Project: Causality Detection =========================
with col_working:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/causality_detection.webp", use_container_width=True, caption="Causality Detection in High-Dimensional Time Series")

    with upper_col2:
        st.markdown("### Causality Detection in High-Dimensional Time Series")
        st.markdown("📅 **May 2026 - Present**")

        github_link = "https://github.com/AyushmanGHub/Causality_Detection_in_High-Dimensional_Time_Series"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Repository Coming Soon</button>
            </a>
        </div>
        """

        st.markdown(github_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
    Working on a research-oriented project focused on causality detection in high-dimensional time series using a model-free framework based on **Information Imbalance of distance ranks**. 
    The project explores how causal relationships can be identified in complex dynamical systems without relying on explicit parametric assumptions or intervention-based experiments.

    The core idea is to determine whether the current state of one system improves the prediction of another system’s future behavior. 
    By measuring the gain in predictive information obtained from combining system states, the framework quantifies directional causal influence through an **Imbalance Gain** metric.

    The project involves generating and analyzing synthetic dynamical systems, performing statistical validation experiments, and evaluating the robustness of the method against false causal detections. 
    The methodology is particularly suited for nonlinear, high-dimensional, and noisy real-world systems where traditional causality methods often fail.

    Current work includes simulation-based experiments, distance-rank computations, causality validation pipelines, and exploratory applications toward complex sequential datasets.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Causal Inference",
        "High-Dimensional Time Series",
        "Information Imbalance",
        "Dynamical Systems",
        "Statistical Validation",
        "Time Series Analysis"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)




###################################################################################################


col_LectureAI, col_AML = st.columns(2)

# ========================= Project: LectureAI =========================
with col_LectureAI:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/lectureai_assistant.webp", use_container_width=True, caption="LectureAI – Personal Lecture Assistant")

    with upper_col2:
        st.markdown("### LectureAI – Personal Lecture Assistant")
        st.markdown("📅 **April 2026**")

        github_link = "https://github.com/AyushmanGHub/LectureAI_-_Personal_Lecture_Assistant"
        presentation_link = "https://drive.google.com/file/d/1u1wAqwSmVSgPhswqXsiqB6ui08an-yf8/view?usp=sharing"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        presentation_html = f"""
        <div style='display: inline-block;'>
            <a href="{presentation_link}" target="_blank">
                <button style='background-color:#e63946; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Presentation</button>
            </a>
        </div>
        """

        st.markdown(github_html + presentation_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
    An Agentic-AI powered learning assistant designed to transform traditional lecture videos into interactive educational experiences. 
    The system processes lecture content and provides AI-powered features such as contextual question answering, automated summaries, mind maps, and MCQ-based assessments.

    The project integrates LangGraph orchestration with Retrieval-Augmented Generation (RAG) pipelines to create structured and searchable learning content. 
    It demonstrates how intelligent AI systems can improve student engagement, personalized learning, and information accessibility through automation and conversational interaction.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "LangGraph",
        "RAG",
        "Agentic AI",
        "LLMs",
        "Flask",
        "FAISS",
        "API Integration"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)

# ========================= Project: Applied Machine Learning - Full System Design =========================
with col_AML:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/aml.webp", use_container_width=True, caption="Applied Machine Learning (AML) – Projects")

    with upper_col2:
        st.markdown("### Applied Machine Learning - Full System Design")
        st.markdown("📅 **January 2026 - April 2026**")

        github_link = "https://github.com/AyushmanGHub/Applied_Machine_Learning"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        st.markdown(github_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
    Collection of Applied Machine Learning projects focused on building reproducible and end-to-end ML systems. 
    The work covered the complete machine learning workflow including preprocessing, model training, evaluation, experiment tracking, deployment, and testing.

    The project included implementations of spam classification systems, transfer learning models, and Flask-based deployment pipelines using modern MLOps practices. 
    It demonstrates practical experience in scalable ML workflows, model versioning, experiment management and production-ready machine learning systems.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Machine Learning",
        "DVC",
        "MLflow",
        "Flask",
        "Docker",
        "Transformers",
        "CNN"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)
st.markdown("---")
###################################################################################################

col_ZScore, col_Minvar = st.columns(2)

# ========================= Project: Z-Score Alpha =========================
with col_ZScore:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/zscorealpha.webp", use_container_width=True, caption="Z-Score Alpha – Statistical Arbitrage Strategy")

    with upper_col2:
        st.markdown("### Z-Score Alpha – Statistical Arbitrage Strategy")
        st.markdown("📅 **February 2026 - March 2026**")

        github_link = "https://github.com/AyushmanGHub/Z-Score_Alpha-Statistical_Arbitrage_Strategy"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        st.markdown(github_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
    Quantitative trading research project focused on statistical arbitrage using Z-score based signals derived from financial time series data. 
    The project aims to identify short-term mean-reversion opportunities by standardizing price deviations from historical behavior and generating trading signals based on statistical thresholds.

    The workflow includes financial time-series preprocessing, signal generation, and backtesting pipelines to evaluate strategy performance under different market conditions. 
    It demonstrates how statistical methods and reproducible data workflows can be applied to systematic trading and quantitative market research.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Quantitative Finance",
        "Statistical Arbitrage",
        "Z-Score Analysis",
        "Time Series Analysis",
        "Financial Data Processing",
        "Backtesting"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)

# ========================= Project: Minimum Variance Portfolio Optimization =========================
with col_Minvar:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/minvar.webp", use_container_width=True, caption="Minimum Variance Portfolio Optimization")

    with upper_col2:
        st.markdown("### Minimum Variance Portfolio Optimization")
        st.markdown("📅 **January 2026 - February 2026**")

        github_link = "https://github.com/AyushmanGHub/Minimum_Variance_Portfolio_Optimization"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        st.markdown(github_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
    Quantitative finance project focused on constructing optimal investment portfolios using the Minimum Variance Portfolio (MVP) framework. 
    The project analyzes historical asset returns to estimate covariance structures and determine portfolio weights that minimize overall portfolio risk.

    The workflow includes financial data collection, return computation, covariance estimation, and portfolio optimization techniques for risk-aware asset allocation. 
    It demonstrates how statistical modeling and optimization methods can be applied to portfolio construction and quantitative risk management.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Portfolio Optimization",
        "Quantitative Finance",
        "Covariance Estimation",
        "Time Series Analysis",
        "Risk Management",
        "Financial Data Analysis"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)

st.markdown("---")


####################################################################################################
col_Website, col_PortfolioApp = st.columns(2)

# ========================= Project: Portfolio Website =========================
with col_Website:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/mainwebsite.webp", use_container_width=True, caption="Ayushman Anupam – Portfolio Website")

    with upper_col2:
        st.markdown("### Ayushman Anupam - Portfolio Website")
        st.markdown("📅 **August 2024 - Present(Updating as Needed)**")

        github_link = "https://github.com/AyushmanGHub/AyushmanGhub.github.io"
        website_link = "https://ayushmanghub.github.io/"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        website_html = f"""
        <div style='display: inline-block;'>
            <a href="{website_link}" target="_blank">
                <button style='background-color:#2563eb; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Live Website</button>
            </a>
        </div>
        """

        st.markdown(github_html + website_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
    My personal portfolio website to showcase key projects, technical skills and Brief Introduction. The website serves as a centralized platform for briefly presenting projects, resume details, technical achievements.

    Built using React and Parcel with responsive UI components and structured project sections covering machine learning, quantitative modeling, and AI systems. It demonstrates modern frontend development practices, responsive design principles, and organized presentation of technical work.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "React",
        "JavaScript",
        "HTML",
        "CSS",
        "Parcel",
        "Responsive Web Design"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)


# ========================= Project: Streamlit Portfolio App =========================
with col_PortfolioApp:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/portfolio_agentic.webp", use_container_width=True, caption="Streamlit Portfolio Website with Agentic AI Assistant")

    with upper_col2:
        st.markdown("### Streamlit Portfolio App with ResAgent")
        st.markdown("📅 **June 2025 - Present(Updating as Needed)**")

        github_link = "https://github.com/AyushmanGHub/APortfolio"
        portfolio_link = "https://ayushmanportfolio.streamlit.app/"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        portfolio_html = f"""
        <div style='display: inline-block;'>
            <a href="{portfolio_link}" target="_blank">
                <button style='background-color:#2563eb; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Portfolio App</button>
            </a>
        </div>
        """

        st.markdown(github_html + portfolio_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
    Fully responsive Streamlit-based portfolio application integrated with an Agentic AI assistant called ResAgent. 
    The platform goes beyond traditional portfolio websites by enabling interactive conversations, AI-powered query answering, and dynamic project exploration.

    The system integrates large language models, external APIs, and responsive frontend components to create an intelligent and interactive portfolio experience. 
    It demonstrates practical applications of AI agents, LLM integration, and conversational systems within modern portfolio platforms.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Streamlit",
        "LLMs",
        "Agentic AI",
        "Gemini API",
        "HTML/CSS",
        "JavaScript"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)

st.markdown("---")

####################################################################################################

col_ADA, col_Empty = st.columns(2)

# ========================= Project: Applied Data Analytics =========================
with col_ADA:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/ada.webp", use_container_width=True, caption="Applied Data Analytics – Real World Data Analysis")

    with upper_col2:
        st.markdown("### Applied Data Analytics (ADA) – Projects")
        st.markdown("📅 **August 2025 - November 2025**")

        github_link = "https://github.com/AyushmanGHub/Applied-Data-Analytics_-ADA-_projects"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        st.markdown(github_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
    Collection of applied data analytics projects focused on exploring real-world datasets using statistical analysis, machine learning techniques, and data visualization.

    The work demonstrates complete analytics workflows including data preprocessing, exploratory data analysis (EDA), model development, and interpretation of analytical results.

    Through multiple case studies, the project highlights practical applications of analytics techniques for extracting insights and supporting data-driven decision making.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Data Analytics",
        "EDA",
        "Statistical Analysis",
        "Machine Learning",
        "Data Visualization",
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)


# ========================= Empty Column =========================
with col_Empty:
    st.markdown("")

st.markdown("---")
###################################################################################################
col_GNNAnamoly, col_CNNaudioClassification = st.columns(2)

# ========================= Project: Graph-Based Network Threat Detection =========================
with col_GNNAnamoly:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/gcn_threat.webp", use_container_width=True, caption="Graph-Based Network Threat Detection using GCN")

    with upper_col2:
        st.markdown("### Graph-Based Network Threat Detection using GCN")
        st.markdown("📅 **September 2025 - October 2025**")

        github_link = "https://github.com/AyushmanGHub/Graph_-_Based-Network_Threat_Detection"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        st.markdown(github_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
    A graph-based deep learning system for detecting malicious network activity using Graph Convolutional Networks (GCNs). 
    The project models network traffic as relational graph data where IP addresses are represented as nodes and communication patterns are represented as edges.

    The workflow includes preprocessing NetFlow traffic data, graph construction, feature extraction, and graph-level threat classification using GCN architectures. 
    It demonstrates how graph neural networks can capture structural communication patterns and improve network intrusion detection performance.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Graph Neural Networks",
        "GCN",
        "Network Analysis",
        "Deep Learning",
        "Cybersecurity",
        "Data Preprocessing"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)


# ========================= Project: SpectroCNN =========================
with col_CNNaudioClassification:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/spectrocnn.webp", use_container_width=True, caption="SpectroCNN – Audio Classification with CNN")

    with upper_col2:
        st.markdown("### SpectroCNN – Audio Classification with CNN")
        st.markdown("📅 **October 2025 - November 2025**")

        github_link = "https://github.com/AyushmanGHub/SpectroCNN_-_Audio_Classification_with_CNN"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        st.markdown(github_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
    Deep learning framework for environmental sound classification using Convolutional Neural Networks (CNNs) and Mel spectrogram representations. 
    The project transforms raw audio signals into structured time-frequency visualizations to enable effective audio pattern recognition.

    The workflow includes audio preprocessing, spectrogram generation, dataset balancing, exploratory analysis, and CNN-based model training for multi-class sound classification. 
    It demonstrates how deep learning techniques can be applied to audio understanding and automated acoustic event recognition.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "CNN",
        "Audio Processing",
        "Mel Spectrograms",
        "Deep Learning",
        "Signal Processing",
        "Data Preprocessing"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)

st.markdown("---")
####################################################################################################

col_fildler, col_dwelling = st.columns(2)

# ========================= Project: Spectral Graph Partitioning =========================
with col_fildler:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/spectral_partitioning.webp", use_container_width=True, caption="Graph Partitioning")

    with upper_col2:
        st.markdown("### Spectral Graph Partitioning using Fiedler's Method")
        st.markdown("📅 **March 2025 - April 2025**")

        github_link = "https://github.com/AyushmanGHub/Fiedlers-Spectral-Graph-Partitioning-Paper"
        pdf_link = "https://drive.google.com/file/d/1JJtpv_99XfyESqNQr_QpuK5iCuthB9SW"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        pdf_html = f"""
        <div style='display: inline-block;'>
            <a href="{pdf_link}" target="_blank">
                <button style='background-color:#e63946; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Report Paper</button>
            </a>
        </div>
        """

        st.markdown(github_html + pdf_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
    Graph theory project focused on Fiedler's Theory of Spectral Graph Partitioning for dividing graphs into balanced and connected subgraphs. 
    The project explores how spectral properties of graph Laplacian matrices can be used to minimize cut edges while maintaining graph connectivity.

    The workflow includes graph Laplacian construction, computation of the Fiedler value and vector, and partition-based network analysis using spectral methods. 
    It demonstrates practical applications of linear algebra and graph theory in network partitioning and complex system analysis.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Graph Theory",
        "Spectral Graph Partitioning",
        "Network Analysis",
        "Linear Algebra",
        "Python",
        "LaTeX"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)


# ========================= Project: Amsterdam Housing Prices =========================
with col_dwelling:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/amsterdam_housing.webp", use_container_width=True, caption="Amsterdam Housing Prices")

    with upper_col2:
        st.markdown("### Data to Dwelling - Amsterdam Housing Prices")
        st.markdown("📅 **October 2024**")

        github_link = "https://github.com/AyushmanGHub/From-Data-to-Dwellings-Decoding-Amsterdam-s-Housing-Prices"
        shiny_link = "https://gkrujk-ayur-ayushman.shinyapps.io/Decoding-Amsterdam-House-Prices-App/"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        shiny_html = f"""
        <div style='display: inline-block;'>
            <a href="{shiny_link}" target="_blank">
                <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>RShiny App</button>
            </a>
        </div>
        """

        st.markdown(github_html + shiny_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
    Housing market analytics project focused on analyzing and predicting Amsterdam housing prices using property and geographic features. 
    The project investigates how factors such as property area, room count, and location influence housing prices within the Amsterdam real estate market.

    The workflow includes exploratory data analysis, correlation analysis, visualization, and interactive dashboard development using RShiny. 
    It demonstrates practical applications of statistical analysis and interactive data visualization for real estate market analytics.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "R",
        "RShiny",
        "EDA",
        "Visualization",
        "Statistics",
        "Real Estate Analytics"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)

st.markdown("---")

################################################################################################################################################ two columns for side-by-side display

col_CreditRisk, col_HeartRisk = st.columns(2)

# ========================= Project: CreditRisk =========================
with col_CreditRisk:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/credit_risk.webp", use_container_width=True, caption="CreditRisk")

    with upper_col2:
        st.markdown("### CreditRisk - Predicting Borrower Reliability")
        st.markdown("📅 **February 2025**")

        github_link = "https://github.com/AyushmanGHub/CreditRisk-Predicting-Borrower-Reliability"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        st.markdown(github_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
    Machine learning project focused on predicting customer credit default risk using binary classification models. 
    The project analyzes customer financial and behavioral data to identify borrowers at high risk of default and support risk-aware lending decisions.

    The workflow includes data preprocessing, feature engineering, model training, evaluation, and feature importance analysis using multiple classification techniques. 
    It demonstrates practical applications of predictive analytics and machine learning in financial risk assessment and credit scoring.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Machine Learning",
        "Binary Classification",
        "Logistic Regression",
        "Random Forest",
        "Feature Selection",
        "Model Evaluation"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)


# ========================= Project: Heartbeat Sentinel =========================
with col_HeartRisk:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/heartbeat_sentinel.webp", use_container_width=True, caption="Heartbeat Sentinel")

    with upper_col2:
        st.markdown("### Heartbeat Sentinel - Predicting Heart Failure")
        st.markdown("📅 **November 2024**")

        github_link = "https://github.com/AyushmanGHub/Heartbeat-Sentinel_Decoding-and-Predicting-Heart-Failure"
        website_link = "https://heartbeatsentineldecodingandpredictingheartfailure.streamlit.app/"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        website_html = f"""
        <div style='display: inline-block;'>
            <a href="{website_link}" target="_blank">
                <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Streamlit App</button>
            </a>
        </div>
        """

        st.markdown(github_html + website_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
    Machine learning project focused on predicting heart failure risk using machine learning classification models. 
    The project analyzes patient health indicators and medical attributes to support early risk identification and preventive healthcare decisions.

    The workflow includes data preprocessing, feature selection, model optimization, evaluation, and deployment through an interactive Streamlit application. 
    It demonstrates practical applications of machine learning and predictive analytics in healthcare risk assessment systems.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Random Forest",
        "XGBoost",
        "Streamlit",
        "Healthcare Analytics",
        "Feature Engineering",
        "Model Evaluation"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)

st.markdown("---")
################################################################################################################################################