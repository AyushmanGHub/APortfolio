import streamlit as st
from datetime import datetime
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
import os

# --- Load API Key from Streamlit Secrets or .env ---
GROQ_API_KEY = st.secrets.get("groq_API_Key", os.getenv("groq_API_Key"))
LLM_MODEL = "llama3-70b-8192"
RESUME_FILE_PATH = os.path.join(os.path.dirname(__file__), "data/Resume_data.txt")

# --- Load Resume Data ---
@st.cache_data
def load_resume_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"Error: Resume file not found at '{file_path}'. Please check the path.")
        st.stop()
    except Exception as e:
        st.error(f"Error loading resume file: {e}")
        st.stop()

resume_data = load_resume_data(RESUME_FILE_PATH)

# --- System Instruction ---
SYSTEM_INSTRUCTION = f"""
You are an AI assistant named ResAgent, specializing in answering questions solely about Ayushman Anupam's resume and portfolio information provided below.
When responding, keep the conversation engaging, informative, and of moderate length and designate him as Ayushman.
If you encounter any inappropriate or off-topic questions, politely redirect the user back to the main topics related to Ayushman's resume.
After each answer, always ask if the user wants to know anything else.

if answer is not in Ayushman Resume Data, say "🔎 Warning - This particular question extends beyond Ayushman’s resume data. Generating a response using general AI knowledge:" then give one line space and let the llm answer it.

Here is Ayushman's Resume Data:
---START RESUME DATA---
{resume_data}
---END RESUME DATA---
"""

# # --- General Prompts (Pills) ---
# general_prompt = [
#     "Who is Ayushman?",
#     "What are Ayushman's skills?",
#     "What are Ayushman's projects?",
#     "What are Ayushman's achievements?",
#     "What are Ayushman's industry experiences?",
#     "What kind of tech role is Ayushman interested in?",
#     "Tell me about Ayushman's education."
# ]

# --- LLM Configuration ---
@st.cache_resource
def configure_llm():
    if not GROQ_API_KEY:
        st.error("GROQ_API_KEY not set. Please set it in Streamlit Secrets or your .env file.")
        st.stop()
    llm = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name=LLM_MODEL)
    return llm

# --- Logging (Optional for debugging) ---
def log_conversation(role, content):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {role}: {content}")

# --- LLM Call ---
def get_groq_response(llm_model, question):
    system_message = SystemMessage(content=SYSTEM_INSTRUCTION)
    human_message = HumanMessage(content=question)
    stream = llm_model.stream([system_message, human_message])
    return stream

# --- Streamlit App Main ---
st.title("👨‍💼 Welcome to my Portfolio")
# st.subheader("Chat with ResAgent 🤖")



st.info("""
**Meet ResAgent 🤖 — Your Personal AI Guide!**

Welcome to my interactive portfolio powered by ResAgent — an advanced AI assistant trained on my resume, skills, experiences, and projects.

You can explore my skills, projects, internships, education, certifications, achievements, and contact information — all in one place, just simply type your question to get started.

📌 Whether you're a recruiter, collaborator, or just curious — ResAgent is here to give you instant insights!

_— Ayushman_
""")

st.markdown("""
    <style>
    /* Outer Chat Container */
    div[data-testid="stChatInput"] {
        background-color: #343541 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 8px 8px !important;
    }

    /* Inner Box */
    div[data-testid="stChatInput"] > div {
        background-color: #343541 !important;
        padding: 0 !important;
    }

    /* The actual input textarea */
    div[data-testid="stChatInput"] textarea {
        background-color: #40414F !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        font-size: 16px !important;
        box-shadow: none !important;
        height: 48px !important;
    }

    /* Placeholder text */
    div[data-testid="stChatInput"] textarea::placeholder {
        color: #8e8ea0 !important;
    }

    /* Remove focus outline */
    div[data-testid="stChatInput"] textarea:focus {
        outline: none !important;
        box-shadow: none !important;
    }

    /* Submit Button (arrow) */
    div[data-testid="stChatInput"] button {
        background-color: transparent !important;
        border: none !important;
        border-radius: 50% !important;
    }
    </style>
""", unsafe_allow_html=True)

# st.markdown("""
#     <style>
#     /* Outer ChatInput container */
#     div[data-testid="stChatInput"] {
#         border: 2px solid #ffa726 !important;
#         border-radius: 8px !important;
#         background-color: #fff3cd !important;
#         padding: 4px !important;
#     }

#     /* Inner container */
#     div[data-testid="stChatInput"] > div {
#         border: none !important;
#         background-color: #fff3cd !important;
#         border-radius: 8px !important;
#         padding: 0px !important;
#     }

#     /* Actual textarea text color fix */
#     div[data-testid="stChatInput"] textarea,
#     div[data-testid="stChatInput"] textarea::placeholder {
#         background-color: #fff3cd !important;
#         border: none !important;
#         border-radius: 8px !important;
#         padding: 4px !important;  /* reduced padding */
#         font-weight: 500;
#         font-size: 20px;
#         color: #000000 !important;          
#         caret-color: #000000 !important;
#         box-shadow: none !important;
#     }

#     /* Placeholder text color */
#     div[data-testid="stChatInput"] textarea::placeholder {
#         color: #999999 !important;
#     }

#     /* Remove focus glow */
#     div[data-testid="stChatInput"] textarea:focus {
#         box-shadow: none !important;
#         outline: none !important;
#     }

#     /* Submit button style */
#     div[data-testid="stChatInput"] button {
#         border-radius: 6px !important;
#         background-color: transparent !important;
#     }
#     </style>
# """, unsafe_allow_html=True)


# Initialize Session State
if "llm_model" not in st.session_state:
    st.session_state.llm_model = configure_llm()
if "messages" not in st.session_state:
    st.session_state.messages = []
# if "pill_selected" not in st.session_state:
#     st.session_state.pill_selected = False

# Initial Greeting
if not st.session_state.messages:
    initial_greeting = "Greetings, Human! 👋 I'm ResAgent, an AI trained to answer questions about **Ayushman's** resume and portfolio. Curious about his projects, skills, or anything else? Just ask! 😉"
    st.session_state.messages.append({"role": "assistant", "content": initial_greeting})

# Display existing messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# from streamlit_pills import pills
# # --- General Prompts (Pills) ---
# general_prompt = [
#     "Who is Ayushman?",
#     "What are Ayushman's skills?",
#     "What are Ayushman's projects?",
#     "What are Ayushman's achievements?",
#     "What are Ayushman's industry experiences?",
#     "What kind of tech role is Ayushman interested in?",
#     "Tell me about Ayushman's education."
# ]

# # Display Pills
# if not st.session_state.pill_selected:
#     selected_pill = pills("", general_prompt, index=None)
#     if selected_pill:
#         st.session_state.pill_selected = True
#         prompt = selected_pill
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         log_conversation("user", prompt)
#         with st.chat_message("user"):
#             st.markdown(prompt)
#         response_content = ""
#         stream = get_groq_response(st.session_state.llm_model, prompt)
#         for chunk in stream:
#             response_content += chunk.content
#         with st.chat_message("assistant"):
#             st.markdown(response_content)
#         st.session_state.messages.append({"role": "assistant", "content": response_content})
#         log_conversation("assistant", response_content)
#         st.rerun()

# Handle User Input
user_prompt = st.chat_input("Ask me anything about Ayushman...")
if user_prompt:
    # st.session_state.pill_selected = True
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    log_conversation("user", user_prompt)
    with st.chat_message("user"):
        st.markdown(user_prompt)
    response_content = ""
    stream = get_groq_response(st.session_state.llm_model, user_prompt)
    for chunk in stream:
        response_content += chunk.content
    with st.chat_message("assistant"):
        st.markdown(response_content)
    st.session_state.messages.append({"role": "assistant", "content": response_content})
    log_conversation("assistant", response_content)
    # st.rerun()
