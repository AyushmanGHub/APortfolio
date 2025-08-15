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
col7A, col7B = st.columns([3,1])


# ========================= Currently working on project =========================
with col7A:
    upper_col1, upper_col2 = st.columns([1, 2])
    
    with upper_col1:
        st.markdown(" ")
        st.markdown(" ")
        st.image(r"images/timeseries.webp", use_container_width=True, caption="StockSeer – See the market’s next move before it happens.")

    with upper_col2:
        st.markdown("### StockSeer – See the market’s next move before it happens.")
        st.markdown("📅 **August 2025 - Present** 🚧 *(Ongoing Project)*")

        github_link = "https://github.com/AyushmanGHub/TimeSeries---Stock-Preciction"  # Add your repo link

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
       Developing a project that automates real-time stock market analysis some Indian Stocks and Indexes by integrating data fetching, feature engineering, 
       predictive modeling, and visualization. It continuously updates historical and prediction datasets, detects missing predictions, and generates advanced 
       lag-based features for improved forecasting. The system supports incremental learning, fine-tuning the model as new actual data arrives. Interactive plots 
       provide both full-range and zoomed-in market trend insights, enabling continuous and data-driven market monitoring.

       I will also be developing DJango or Streamlit App to show real time prediction through Interactive plot
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = ["Python", "TimeSeries", "API call", "Ensemble ML Models", "Finance"]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)
st.markdown("""
    <hr style="
    border: 0;
    height: 2px;
    background: linear-gradient(to right, #a9a9a9, #d3d3d3);
    ">
    """, unsafe_allow_html=True)


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
        learning, such as linear information flow, limited interaction, etc.  This framework converts lecture videos 
        into interactive learning experiences, providing a personalized chatbot, mind map, notes, and other materials for enhanced engagement and effectiveness. 
        This Agentic-AI tool is aims to enhance learning experience, helping learners save 30–50% of their time through personalized, automated academic support.
    """)

    st.markdown("##### Skills & Technologies Used")

    skills = ["Python", "LangGraph","LangChain", "Groq LLM", "Agentic AI","AI-Agents" ,"HTML", "CSS", "Groq API", "RAG", "Django", "Vectorstore"]

    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"

    st.markdown(badges_html, unsafe_allow_html=True)




# ========================= Project 2: =========================
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

    skills = ["Python", "Streamlit", "LangGraph", "Groq LLM", "Agentic AI", "HTML", "CSS", "Groq API", "RAG"]

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

    skills = ["Python", "Jupyter Notebook", "Graph Theory", "Network Analysis", "LaTeX", "Linear Algebra"]
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

    skills = ["Python", "Sklearn", "Classification Models", "Logistic Regression", "Random Forest", "Precision-Recall", "Feature Selection", "EDA"]
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

    skills = ["Python", "Streamlit", "Random Forest", "XGBoost", "ROC-AUC", "Model Evaluation", "Feature Selection", "EDA"]
    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"
    st.markdown(badges_html, unsafe_allow_html=True)

st.markdown("---")

################################################################################################################################################ two columns for side-by-side display
col2A, col2B = st.columns(2)

# ========================= Project 1: NextBuy - E-commerce Recommendation (LEFT SIDE) =========================
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

    skills = ["Python", "EDA", "Recommender Systems", "Collaborative Filtering", "Content-Based Filtering", "Precision@10", "Machine Learning"]
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

    skills = ["R", "RShiny", "EDA", "Linear Regression", "Visualization", "Data Analysis", "Statistics", "Real Estate Analytics"]
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

    skills = ["Python", "Time-Series Forecasting", "LGBMRegressor", "MultiOutputRegressor", "MAE", "MAPE", "RMSE", "EDA"]
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

    skills = ["R", "Inequality Indices", "Gini Index", "Theil Index", "Atkinson Index", "Statistics", "Research", "Data Analysis", "Latex", "PCA", "Linear Algebra"]
    badges_html = "<div style='display: flex; flex-wrap: wrap;'>"
    for skill in skills:
        badges_html += f"<span style='background-color:#4CAF50; color:white; padding:4px 8px; margin:5px; border-radius:5px;'>{skill}</span>"
    badges_html += "</div>"
    st.markdown(badges_html, unsafe_allow_html=True)

