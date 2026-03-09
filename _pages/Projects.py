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

# ========================= Project: Z-Score Alpha =========================
with col_working:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/zscorealpha.webp", use_container_width=True, caption="Z-Score Alpha – Statistical Arbitrage Strategy")

    with upper_col2:
        st.markdown("### Z-Score Alpha – Statistical Arbitrage Strategy")
        st.markdown("📅 **March 2026 - Present**")

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
    Developing a quantitative trading research project focused on statistical arbitrage using Z-score based signals derived from financial time series data. 
    The project aims to identify short-term mean-reversion opportunities by standardizing price deviations from historical behavior and generating trading signals based on statistical thresholds.

    The workflow includes data understanding, financial time-series preprocessing, signal generation, and backtesting of the strategy to evaluate performance under different market conditions. 
    The project emphasizes building a clean and reproducible data pipeline along with analytical tools for exploring statistical patterns in asset price movements.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Quantitative Finance",
        "Statistical Arbitrage",
        "Z-Score Analysis",
        "Time Series Analysis",
        "Data Cleaning",
        "Financial Data Processing"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)

st.markdown("---")



###################################################################################################

col9A, col9B = st.columns(2)

# ========================= Project: Minimum Variance Portfolio Optimization =========================
with col9A:
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
    Developed a quantitative finance project focused on constructing an optimal investment portfolio using the Minimum Variance Portfolio (MVP) framework. 
    The project analyzes historical asset returns to estimate the covariance structure between assets and determines portfolio weights that minimize overall portfolio risk. 
    It demonstrates how statistical methods and optimization techniques can be applied to portfolio construction and risk management in financial markets.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Portfolio Optimization",
        "Quantitative Finance",
        "Covariance Estimation",
        "Time Series Analysis",
        "Financial Data Analysis"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)

# ========================= Project 02: =========================
with col9B:
    st.markdown("")




st.markdown("---")

####################################################################################################

col8A, col8B = st.columns(2)

# ========================= Project 01: Applied Machine Learning =========================
with col8A:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/aml.webp", use_container_width=True, caption="Applied Machine Learning – End-to-End ML Workflow")

    with upper_col2:
        st.markdown("### Applied Machine Learning (AML) – Projects")
        st.markdown("📅 **January 2026 - Present**")

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
    Working on a series of practical assignments as part of the Applied Machine Learning course, focusing on building machine learning systems and learning the full ML workflow from model development to deployment.

    The project covers model building, experiment tracking, version control for data and models, web deployment, and containerization to simulate real-world machine learning pipelines.

    Key components include:
    - Spam detection model development  
    - Data and model versioning using DVC  
    - Model deployment through a Flask web application  
    - Containerization using Docker for reproducible ML systems
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Machine Learning",
        "DVC",
        "MLflow",
        "Flask",
        "Docker",
        "Model Deployment",
        "Experiment Tracking",
        "Git"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)


# ========================= Project 02: Applied Data Analytics =========================
with col8B:
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
    Developed a collection of applied data analytics projects focused on exploring real-world datasets using statistical analysis, machine learning techniques, and data visualization.

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

st.markdown("---")




###################################################################################################

col7A, col7B = st.columns(2)

# ========================= Project 01: QuantPulse =========================
with col7A:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/quantpulse.webp", use_container_width=True, caption="QuantPulse – Short-term Portfolio Optimizer")

    with upper_col2:
        st.markdown("### QuantPulse – Short-term Portfolio Optimizer")
        st.markdown("📅 **October 2025 - November 2025**")

        github_link = "https://github.com/AyushmanGHub/QuantPulse_Short-term-Portfolio-Optimizer"
        report_link = "https://drive.google.com/file/d/11VfeVdgkm0hL-Hl-lv4j5xL7AOzKphhA/view?usp=sharing"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        report_html = f"""
        <div style='display: inline-block;'>
            <a href="{report_link}" target="_blank">
                <button style='background-color:#e63946; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Report Paper</button>
            </a>
        </div>
        """

        st.markdown(github_html + report_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
    Developed a quantitative finance project focused on short-term portfolio optimization using market data and predictive modeling techniques. 
    The system integrates financial data processing, return forecasting, and portfolio allocation strategies to identify optimal asset weightings for short-term investment horizons.

    The project includes automated workflows for data preparation, model-based signal generation, and performance evaluation to support systematic portfolio decision-making.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Quantitative Finance",
        "Portfolio Optimization",
        "Time Series Analysis",
        "Machine Learning",
        "Financial Data Processing",
        "Data Visualization"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)


# ========================= Project 02: StockSeer =========================
with col7B:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/stocksheer.webp", use_container_width=True, caption="StockSeer – Market Prediction System")

    with upper_col2:
        st.markdown("### StockSeer – See the market’s next move")
        st.markdown("📅 **August 2025 - September 2025**")

        github_link = "https://github.com/AyushmanGHub/-StockSeer-See-market-s-next-move"

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
        Developed an end-to-end system for automated stock market analysis and prediction on selected Indian stocks and indices. 
        The project integrates data collection, feature engineering, predictive modeling, and visualization into a unified pipeline for continuous market monitoring and analysis.

        **Key Features:**
        1. Automated data pipeline that updates historical market data, generates predictions, and detects missing prediction entries.  
        2. Incremental learning capability where the model is periodically fine-tuned as new actual market data becomes available.  
        3. Interactive visualizations providing full-range and zoomed-in market trend insights.
        """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Yahoo Finance API",
        "Time Series Analysis",
        "Machine Learning",
        "Financial Data Processing",
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)

st.markdown("---")

###################################################################################################
col6A, col6B = st.columns(2)


# ========================= Project 1:LectureAI =========================
with col6A:
    upper_col1, upper_col2 = st.columns([1, 2])
    
    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/lectureAI.webp", use_container_width=True, caption="Lecture-AI : Your personal AI tutor (Agentic-AI framework)")

    with upper_col2:
        st.markdown("### LectureAI – Your personal AI Tutor")
        st.markdown("📅 **May 2025 - July 2025**")

        github_link = "https://github.com/AyushmanGHub/LectureAI-Agentic-AI_freamework"  # Add your repo link

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
        As a part 2025 Summer Internship, I with my teammate developed "Lecture-AI" Agentic-AI framework that addresses the key drawbacks of traditional video-based 
        learning, such as linear information flow, limited interaction, etc.  This framework converts lecture videos into interactive learning experiences, providing a 
        personalized chatbot, mind map, notes, and other materials for enhanced engagement and effectiveness. 
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = ["LangGraph",
              "LangChain",  
              "Agentic AI","AI-Agents", "LLM API", "RAG", "Django"]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)


# ========================= Project 2: Corporate Rating using Bayesian & MCMC =========================
with col6B:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/mcmc.webp", use_container_width=True, caption="Corporate Rating Prediction using Bayesian & MCMC")

    with upper_col2:
        st.markdown("### Synthetic Data Generation & Corporate Rating Prediction")
        st.markdown("📅 **November 2025 - December 2025**")

        github_link = "https://github.com/AyushmanGHub/Synthetic-Data-Generation-and-Prediction-for-Corporate-rating-using-Bayesian-and-MCMC-techniques"
        report_link = "https://drive.google.com/file/d/1eRune85TmsE66F_FzjNj7_KPNSiULhvv/view?usp=sharing"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        report_html = f"""
        <div style='display: inline-block;'>
            <a href="{report_link}" target="_blank">
                <button style='background-color:#e63946; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Report Paper</button>
            </a>
        </div>
        """

        st.markdown(github_html + report_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
        Developed a probabilistic modeling project focused on predicting corporate credit ratings using Bayesian statistical methods. 
        The system integrates synthetic data generation with Bayesian inference to address the challenge of limited financial datasets. 
        Using Markov Chain Monte Carlo (MCMC) sampling, the model estimates posterior distributions of parameters and produces probabilistic predictions with uncertainty quantification.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [
        "Bayesian Statistics",
        "MCMC",
        "Synthetic Data Generation",
        "Financial Data Analysis",
        "Machine Learning",
        "Data Visualization"
    ]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)


st.markdown("---")
###################################################################################################

col5A, col5B = st.columns(2)


# ========================= Project 1: ResAgent Portfolio =========================
with col5A:
    upper_col1, upper_col2 = st.columns([1, 2])
    
    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/portfolio_agentic.webp", use_container_width=True, caption="Portfolio with ResAgent")

    with upper_col2:
        st.markdown("### Streamlit Portfolio Website with Agentic AI feature")
        st.markdown("📅 **June 2025**")

        github_link = "https://github.com/AyushmanGHub/APortfolio/tree/master"  # Add your repo link
        website_link = "https://ayushmanportfolio.streamlit.app/"  # Add your live website link

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
                <button style='background-color:#0077b5; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>View Website</button>
            </a>
        </div>
        """

        st.markdown(github_html + website_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
        Designed and developed a fully responsive Streamlit-based personal portfolio website integrated with an Agentic AI-powered assistant — **ResAgent**. 
        The assistant leverages LLMs to answer queries, fetch recent data, and provide interactive conversations within the portfolio.
        Included dynamic project pages, certification highlights, and AI-powered blog integration.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = ["Streamlit", "LangGraph", "Agentic AI", "HTML", "CSS", "LLM API"]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)




# ========================= Project 2: Spectral Graph Partitioning =========================
with col5B:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/spectral_partitioning.webp", use_container_width=True, caption="Graph Partitioning")

    with upper_col2:
        st.markdown("### Spectral Graph Partitioning using Fiedler's Method")
        st.markdown("📅 **April 2025**")

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
        `Mentor: Prof. Kavita Sutar Deshpande (Chennai Mathematical Institute)` <br>
        Developed a project on Fiedler's Theory of Spectral Graph Partitioning, a technique for dividing graphs into balanced and connected subgraphs.
        Implemented graph Laplacian matrix construction, computed the Fiedler value, and utilized the Fiedler vector for node partitioning, minimizing cut edges while maintaining graph balance.
    """, 
    unsafe_allow_html=True)

    st.markdown("##### Skills & Technologies Used")

    skills = ["Graph Theory", "Network Analysis", "LaTeX", "Linear Algebra"]
    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"
    st.markdown(badges_html, unsafe_allow_html=True)

st.markdown("---")
####################################################################################################################################################

# Create two columns for side-by-side display
col4A, col4B = st.columns(2)

# ========================= Project 1: CreditRisk (LEFT SIDE) =========================
with col4A:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/credit_risk.webp", use_container_width=True, caption="CreditRisk")

    with upper_col2:
        st.markdown("### CreditRisk - Predicting Borrower Reliability and Risk")
        st.markdown("📅 **Jan 2024**")

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
        Developed and implemented different binary classification models to identify customers at risk of credit default and assess the associated lending risk.
        Evaluated models achieving 0.97 accuracy, recall and precision of 0.89 and 0.79 for defaulters, and 0.98 and 0.99 for non-defaulters.
        Performed feature selection and compared feature importance across models to identify key factors associated with credit default.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = [ "Sklearn", "Classification Models", "Logistic Regression", "Random Forest", "Precision-Recall", "Feature Selection", "EDA"]
    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"
    st.markdown(badges_html, unsafe_allow_html=True)


# ========================= Project 2: Heartbeat Sentinel (RIGHT SIDE) =========================
with col4B:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/heartbeat_sentinel.webp", use_container_width=True, caption="Heartbeat Sentinel")

    with upper_col2:
        st.markdown("### Heartbeat Sentinel - Predicting Heart Failure")
        st.markdown("📅 **Nov 2024**")

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
        Developed, optimized and implemented Random Forest and XGBoost models to predict heart failure risk, achieving 90% accuracy.
        Deployed a Streamlit app to classify heart failure risk.
        Performed data preprocessing, feature selection, and model evaluation using accuracy, precision, recall, F1-score, and ROC-AUC.
        Analyzed results to identify key risk factors and early warning systems for heart disease.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = ["Streamlit", "Random Forest", "XGBoost", "ROC-AUC", "Model Evaluation", "Feature Selection"]
    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"
    st.markdown(badges_html, unsafe_allow_html=True)

st.markdown("---")

################################################################################################################################################ two columns for side-by-side display
col2A, col2B = st.columns(2)

# ========================= Project 1: NextBuy - E-commerce Recommendation =========================
with col2A:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/nextbuy_recommendation.webp", use_container_width=True, caption="E-Commerce Recommendation")

    with upper_col2:
        st.markdown("### NextBuy: Predicting Your Next Perfect Purchase")
        st.markdown("📅 **Jan 2025**")

        github_link = "https://github.com/AyushmanGHub/NextBuy-Predicting-your-next-perfect-purchase"

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
        Developed a comprehensive E-commerce Recommendation System integrating both **Content-Based Filtering** and **Collaborative Filtering** to enhance user experience.
        Achieved strong model performance, with **Precision and Recall of 0.61** for Content-Based Filtering and a **RMSE of 1.0551** and **Precision@10 of 0.9693** for Collaborative Filtering.
        Conducted extensive **data processing and exploratory data analysis (EDA)** to understand user-item interactions and product characteristics.
        Focused on improving user experience by providing relevant product suggestions, demonstrating practical application of machine learning in e-commerce.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = ["EDA", "Recommender Systems", "Collaborative Filtering", "Content-Based Filtering", "Precision@10", "Machine Learning"]
    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"
    st.markdown(badges_html, unsafe_allow_html=True)


# ========================= Project 2: Amsterdam Housing Prices (RIGHT SIDE) =========================
with col2B:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/amsterdam_housing.webp", use_container_width=True, caption="Amsterdam Housing Prices")

    with upper_col2:
        st.markdown("### Data to Dwelling - Decoding Amsterdam Housing Prices")
        st.markdown("📅 **Oct 2024**")

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
        `Mentor: Prof. Sourish Das (Chennai Mathematical Institute)` <br>
        Conducted comprehensive analysis and prediction of Amsterdam's housing price by examining key predictors such as property area, number of rooms, and geographic location.
        Performed Exploratory Data Analysis (EDA) to visualize trends and assess the impact of various features on housing prices, identifying strong correlations between area, room count, and price.
        Identified significant trends and correlations, providing insights into the factors influencing the Amsterdam real estate market.<br>
        Utilized R and developed RShiny for data analysis and potentially for creating an interactive application to visualize insights.
    """,
    unsafe_allow_html=True)

    st.markdown("##### Skills & Technologies Used")

    skills = ["R", "RShiny", "EDA", "Visualization", "Statistics", "Real Estate Analytics"]
    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"
    st.markdown(badges_html, unsafe_allow_html=True)

st.markdown("---")

################################################################################################################################################


# Create two columns for side-by-side display
col1A, col1B = st.columns(2)
# ========================= Project 1: Chennai Temperature Forecasting (LEFT SIDE) =========================
with col1A:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/chennai_temp_forecast.webp", use_container_width=True, caption="Chennai Temperature Forecasting")

    with upper_col2:
        st.markdown("### Chennai Temperature & Precipitation Forecasting")
        st.markdown("📅 **Sept 2024**")

        github_link = "https://github.com/AyushmanGHub/Daily-Temperature-Prediction-of-Chennai"

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
        Developed and implemented a time-series model for weather forecasting including average, minimum, and maximum temperatures for Chennai, achieving RMSE values of 1.21, 1.31, and 1.84, respectively.
        Utilized MultiOutputRegressor with LGBMRegressor for model training and evaluated performance using metrics such as MAE, MAPE, and RMSE to ensure accuracy and reliability.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = ["Python", "Time-Series Forecasting", "LGBMRegressor", "MultiOutputRegressor", "EDA"]
    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"
    st.markdown(badges_html, unsafe_allow_html=True)


# ========================= Project 2: WASH Inequality Paper (RIGHT SIDE) =========================
with col1B:
    upper_col1, upper_col2 = st.columns([1, 2])

    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/wash_inequality.webp", use_container_width=True, caption="WASH Inequality")

    with upper_col2:
        st.markdown("### Availability, Accessibility & Inequality of WASH")
        st.markdown("📅 **Dec 2022**")

        github_link = "https://github.com/AyushmanGHub/Availability_Accessibility_and_Inequalities_of_WASH_in_Metro-Cities"
        paper_link = "https://drive.google.com/file/d/1pfVu68jwAGkJZDnyAtd4bdaJkukxAP7l/view?usp=drive_link"

        github_html = f"""
        <div style='display: inline-block; margin-right: 10px;'>
            <a href="{github_link}" target="_blank">
                <button style='background-color:#24292e; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>GitHub Repo</button>
            </a>
        </div>
        """

        paper_html = f"""
        <div style='display: inline-block;'>
            <a href="{paper_link}" target="_blank">
                <button style='background-color:#e63946; color:white; padding:7px 13px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>Paper</button>
            </a>
        </div>
        """

        st.markdown(github_html + paper_html, unsafe_allow_html=True)

    st.markdown("#### About the Project")
    st.markdown("""
        `Mentor: Prof. Rituparna Sen (Indian Statistical Institute)` <br>
        Conducted an in-depth analysis of inequality in access to Water, Sanitation, and Hygiene (WASH) services across six major Indian cities under the mentorship of Prof. Rituparna Sen, ISI Bangalore.
        Utilized Gini, Theil, and Atkinson indices to measure disparities and track improvements in WASH services.
    """,
    unsafe_allow_html=True)

    st.markdown("##### Skills & Technologies Used")

    skills = ["R", "Inequality Indices", "Statistics", "Data Analysis", "Latex", "PCA", "Linear Algebra"]
    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"
    st.markdown(badges_html, unsafe_allow_html=True)

