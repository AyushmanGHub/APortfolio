import time
import datetime
import streamlit as st
from google import generativeai as genai
from streamlit_pills import pills
import json

# --- Configure Gemini ---
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)
llm_model = genai.GenerativeModel(model_name="gemini-2.5-flash")

# --- Load Resume Data ---
@st.cache_data
def load_resume(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
resume_text = load_resume("resources/Resume_data.txt")

# --- Load Common Questions and Answers ---
COMMON_QUESTIONS_FILE = "resources/common_questions.json"

@st.cache_data
def load_common_questions():
    """Loads common questions and answers from the JSON file."""
    try:
        with open(COMMON_QUESTIONS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Error: {COMMON_QUESTIONS_FILE} not found. Please ensure the file exists in the 'resources' folder.")
        return {}
    except json.JSONDecodeError:
        st.error(f"Error decoding JSON from {COMMON_QUESTIONS_FILE}. Please check the file's format.")
        return {}
    # Load common questions once at the start of the app
common_qna = load_common_questions()

# --- Utility Functions ---
def get_recent_history(messages_list, max_tokens=8000):
    history = []
    messages = messages_list[-4:]
    for i in range(0, len(messages), 2):
        user_msg = messages[i]
        assistant_msg = messages[i + 1] if i + 1 < len(messages) else {"content": ""}
        history.append(f"User: {user_msg['content']}\nResAgent: {assistant_msg['content']}")
    while len("\n\n".join(history)) // 4 > max_tokens and len(history) > 1:
        history.pop(0)
    return "\n\n".join(history)

def build_prompt(Resume_Data, user_question, past_chat):
    return f"""
You are ResAgent — an AI assistant answering questions **only about Ayushman Anupam's resume and portfolio**.

- Use bullet points and paragraphs.
- Include dates, links, duration when available
- Don't introduce yourself.
- If off-topic, redirect to resume-related topics.
- If answer is not in Resume_Data, say: "🔎 Warning - This question extends beyond Ayushman's resume data." Never invent details
- Conclude with sentences like "Do you want to know ..."

Resume_Data include:
- **Projects**: name, date, summary, tech stack, links
- **Internships**: role, org, duration, description, skills
- **Education**: degree, institution, grades, subjects

Resume_Data:
{Resume_Data}

User Question:
{user_question}

Relevant Past Chat:
{past_chat}
"""

def generate_answer(user_query, resume_text, chat_history):
    past_chat = get_recent_history(chat_history)
    prompt = build_prompt(resume_text, user_query, past_chat)
    try:
        response = llm_model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error generating response - facing some difficulty: {str(e)}"
# --- Streamlit UI ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pills_used" not in st.session_state:
    st.session_state.pills_used = False
if "pill_query" not in st.session_state:
    st.session_state.pill_query = None
if "last_user_question" not in st.session_state: # <-- THIS LINE IS CRUCIAL
    st.session_state.last_user_question = None   # <-- THIS LINE IS CRUCIAL

if not st.session_state.messages:
    greeting = "Greetings, Human! 👋 I'm ResAgent, an AI trained to answer questions about **Ayushman's** resume and portfolio. Curious about his projects, skills, or anything else? Just ask! 😉"
    st.session_state.messages.append({"role": "assistant", "content": greeting})


st.title("👨‍💼 Welcome to My Smart Portfolio")

st.info("""
**Meet ResAgent 🤖 — Your Personal AI Guide!**

Welcome to my interactive portfolio, powered by **ResAgent** — an AI assistant trained on my resume, skills, experiences, and projects.

Here, you can explore my work, skills, internships, education, certifications, and more — just type your question to get started. Whether you're a recruiter, potential collaborator, or simply curious — ResAgent is here to help you discover more about me instantly.

🚨 ResAgent runs on open-source infrastructure, so responses might take a few moments. Thanks for your patience!

_— Ayushman_
""")

st.markdown("""
    <style>
    div[data-testid="stChatInput"] {
        background-color: #343541 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 8px 8px !important;
    }
    div[data-testid="stChatInput"] > div {
        background-color: #343541 !important;
        padding: 0 !important;
    }
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
    div[data-testid="stChatInput"] textarea::placeholder {
        color: #8e8ea0 !important;
    }
    div[data-testid="stChatInput"] textarea:focus {
        outline: none !important;
        box-shadow: none !important;
    }
    div[data-testid="stChatInput"] button {
        background-color: transparent !important;
        border: none !important;
        border-radius: 50% !important;
    }
    </style>
""", unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Suggested pill prompts
suggested_questions = [
    "Tell me about Ayushman?",
    "What are Ayushman's skills?",
    "Show me Ayushman's latest projects",
    "list me his projects?",
    "tell me about his lastest work Experience?",
    "Tell me about his volunteerings",
    "How to contact him?"
]

common_question =[
    "Tell me about Ayushman?",
    "What are Ayushman's skills?",
    "What are Ayushman's technical skills?",
    "Show me Ayushman's latest projects",
    "list me his projects?",
    "show me his work Experience/Internships?",
    "tell me about his lastest work Experience?",
    "tell me about his education",
    "Tell me about his volunteerings",
    "How to contact him?"

]

# Show pills only once at the beginning
if not st.session_state.pills_used and not any(m["role"] == "user" for m in st.session_state.messages):
    selected_pill = pills("\ud83d\udca1 Try asking:", suggested_questions, index=None)
    if selected_pill:
        st.session_state.pills_used = True
        st.session_state.pill_query = selected_pill
        st.rerun()


chat_input_text = st.chat_input("Ask me anything about Ayushman...")
start_time = time.time()
user_prompt = st.session_state.pill_query or chat_input_text
if user_prompt and st.session_state.pill_query:
    st.session_state.pill_query = None

if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.chat_message("user"):
        st.markdown(user_prompt)

    user_prompt_lower = user_prompt.lower()

    answer_from_json = None
    force_api_call = False

    if (st.session_state.last_user_question and
        user_prompt_lower == st.session_state.last_user_question.lower() and
        user_prompt_lower in common_qna):
        force_api_call = True
        st.session_state.last_user_question = None
        st.warning("You asked this common question previously. Fetching a fresh answer from ResAgent to ensure the latest information.")

    if not force_api_call and user_prompt_lower in common_qna:
        answer_from_json = common_qna[user_prompt_lower]
        st.session_state.last_user_question = user_prompt

    if answer_from_json:
        end_time = time.time()
        total_time = round(end_time - start_time, 2)
        with st.chat_message("assistant"):
            st.markdown(f"**⚡️ Quick Answer from Pre-loaded Cache! in {total_time} seconds **\n\n{answer_from_json}")
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer_from_json
        })
    else:
        
        with st.spinner("ResAgent..🔍 Please wait, I run on open-source tools, so I am slower than big guys!"):
            answer = generate_answer(
                            user_prompt,
                            resume_text,
                            st.session_state.messages
                        )

        end_time = time.time()
        total_time = round(end_time - start_time, 2)

        with st.chat_message("assistant"):
            st.markdown(answer)
            st.caption(f"🕒 {total_time}s")

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        if "🔎 Warning" not in answer:
            st.session_state.last_user_question = user_prompt
        else:
            st.session_state.last_user_question = None 
