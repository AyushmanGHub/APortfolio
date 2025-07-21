import streamlit as st
import base64

# Utility function to load image and convert to base64 (needed for HTML)
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

st.title("🎓 Education")
st.markdown("#### My academic journey and the institutes that shaped my skills & thinking.")

# Gradient separator
st.markdown("""
<hr style="
border: 0;
height: 2px;
background: linear-gradient(to right, #ff5858, #f09819);
">
""", unsafe_allow_html=True)
st.markdown("")
# Load images as base64
cmi_img = get_image_base64("images/cmi.webp")
isi_img = get_image_base64("images/isi.webp")

# --- Chennai Mathematical Institute ---
with st.container():
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; justify-content: center; height: 200px; border: 1px solid transparent;">
                <img src="{cmi_img}" style="height: 180px; object-fit: contain;">
            </div>
            """, 
            unsafe_allow_html=True
        )
    with col2:
        st.success("Chennai Mathematical Institute")
        st.markdown("""
        **M.Sc in Data Science**  
        Chennai, India | *(2024 - 2026)*  
        `Key Subjects:` <br>
        Python, Probability and Statistics with R, Mathematical Analysis, Data Visualization, Linear Algebra, Algorithm Design and Analysis, Data Mining and Machine Learning.
        """
        , unsafe_allow_html=True)
st.markdown("---")

# --- Indian Statistical Institute ---
with st.container():
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; justify-content: center; height: 200px; border: 1px solid transparent;">
                <img src="{isi_img}" style="height: 180px; object-fit: contain;">
            </div>
            """, 
            unsafe_allow_html=True
        )
    with col2:
        st.info("Indian Statistical Institute")
        st.markdown("""
        **BMaths. (Hons.), Mathematics**  
        Bangalore, India | *(2020 - 2024)*  
        `Key Subjects:`<br> 
        Probability, Statistics, R, Graph Theory, Optimization, Economics, Linear Algebra, Design and Analysis of Algorithms, Graph and Matrices.
        """
        , unsafe_allow_html=True)
st.markdown("---")

# --- Vidya Bharati Chinmaya Vidyalaya and Shiksha Niketan Side by Side ---
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.warning("Vidya Bharati Chinmaya Vidyalaya")
        st.markdown("""
        **Intermediate Arts, Pure Science (PCM)**  
        Telco, Jamshedpur, India | *(2018 - 2020)*
        """)

    with col2:
        st.error("Shiksha Niketan School")
        st.markdown("""
        **Matriculation**  
        Jamshedpur, India | *(2018)*
        """)