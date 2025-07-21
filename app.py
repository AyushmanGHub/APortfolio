import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
import importlib.util

# Set page config only once
if "config_set" not in st.session_state:
    st.set_page_config(
        page_title="Ayushman's Portfolio",
        page_icon="💻",
        layout="wide",
        initial_sidebar_state="auto",
    )
    st.session_state.config_set = True

# --- Sidebar Social Links (cached) ---
@st.cache_data
def get_sidebar_social_links():
    return """
    <div style='text-align: center;'>
        <a href='https://www.linkedin.com/in/ayushman-anupam' target='_blank'>
            <img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'>
        </a>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <a href='https://github.com/AyushmanGHub' target='_blank'>
            <img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'>
        </a>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <a href='mailto:ayushmantutu@gmail.com'>
            <img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'>
        </a>
    </div>
    <div style='text-align: center; margin-top: 20px;'>
        <a href='https://drive.google.com/file/d/13fhhQG4FL9JnFIW3oZwbtJI0Yd4BzzF7/view?usp=drive_link' target='_blank'>
            <button style='background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px; cursor: pointer; box-shadow: 0 4px 8px rgba(0,0,0,0.2); transition: 0.3s;'>
                📄 My Resume
            </button>
        </a>
    </div>
    """

# --- Menu Configuration ---
MENU_OPTIONS = [
    "ResAgent", "About Me", "Experience", "Education",
    "Projects", "Certifications", "Volunteering", "Blog", "Contact me"
]

PAGE_MODULES = {
    "ResAgent": "_pages.ResAgent",
    "About Me": "_pages.About_Me",
    "Experience": "_pages.Experience",
    "Education": "_pages.Education",
    "Projects": "_pages.Projects",
    "Certifications": "_pages.Certifications",
    "Volunteering": "_pages.Volunteering",
    "Blog": "_pages.Blog",
    "Contact me": "_pages.Contact",
}

PRECOMPUTED_PAGE_PATHS = {
    name: Path(path.replace(".", "/") + ".py")
    for name, path in PAGE_MODULES.items()
}

@st.cache_data
def get_all_page_contents():
    """Cache all page contents once"""
    cache = {}
    for name, path in PRECOMPUTED_PAGE_PATHS.items():
        try:
            if path.exists():
                with open(path, encoding="utf-8") as f:
                    cache[name] = f.read()
        except Exception as e:
            st.error(f"❌ Error loading {name}: {str(e)}")
    return cache

# Preload all pages once
if "page_content_cache" not in st.session_state:
    st.session_state.page_content_cache = get_all_page_contents()

# --- Sidebar Navigation ---
with st.sidebar:
    choose = option_menu(
        menu_title="Ayushman Anupam",
        options=MENU_OPTIONS,
        menu_icon="🎓",
        default_index=1,
        styles={
            "container": {"padding": "0!important", "background-color": "#0D1117"},
            "icon": {"color": "darkorange", "font-size": "20px"},
            "nav-link": {
                "font-size": "17px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#1F2937",
            },
            "nav-link-selected": {"background-color": "#A41117"},
        }
    )

    st.markdown(get_sidebar_social_links(), unsafe_allow_html=True)

# --- Load and execute the selected page ---
def load_page_module_from_path(page_name: str, path: Path):
    try:
        spec = importlib.util.spec_from_file_location(page_name, path)
        if not spec:
            return None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        st.error(f"❌ Error importing {page_name}: {str(e)}")
        return None

def render_page(page_name: str):
    content = st.session_state.page_content_cache.get(page_name)
    if content:
        try:
            exec(content, globals())
        except Exception as e:
            st.error(f"❌ Error executing {page_name}: {str(e)}")
    else:
        st.error(f"❌ Page not found: {page_name}")

# Set current page in session_state
if st.session_state.get("current_page") != choose:
    st.session_state.current_page = choose

# Render current page
render_page(choose)
