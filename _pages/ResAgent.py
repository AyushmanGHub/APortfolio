import streamlit as st
from datetime import datetime
import os
import re
import asyncio
import nest_asyncio
nest_asyncio.apply()
import aiohttp
import time
from bs4 import BeautifulSoup
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from google import generativeai as genai
from streamlit_pills import pills


def estimate_tokens(text: str):
    return len(text) // 4


GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

@st.cache_resource
def load_vectorstore():
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local("Resume_VectorStore", embeddings=embedding_model, allow_dangerous_deserialization=True)
    return vectorstore

vectorstore = load_vectorstore()

def extract_urls(text):
    url_pattern = r'(https?://\S+)'
    return re.findall(url_pattern, text)

async def scrape_url(session, url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=3)) as res:
            html = await res.text()
            soup = BeautifulSoup(html, "html.parser")
            paragraphs = soup.find_all('p')
            content = '\n'.join(p.get_text() for p in paragraphs)
            return content[:2000]
    except:
        return ""

async def scrape_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [scrape_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return [r if isinstance(r, str) else "" for r in results]

async def retrieve_context(user_query, top_k=10):
    async def get_vector_context():
        docs = vectorstore.similarity_search(user_query, k=top_k)
        retrieved_context = ""
        all_urls = []

        for doc in docs:
            content = doc.page_content[:1500]
            retrieved_context += content + "\n"
            all_urls.extend(extract_urls(doc.page_content))

        return retrieved_context, all_urls

    async def scrape_urls(urls):
        if not urls:
            return ""
        scraped_contents = await scrape_all(urls)
        context = ""
        for url, scraped_text in zip(urls, scraped_contents):
            if scraped_text:
                context += f"\nExtracted content from {url}:\n{scraped_text}\n"
        return context

    retrieved_context, urls = await get_vector_context()
    scrape_task = asyncio.create_task(scrape_urls(urls))
    scraped_context = await scrape_task
    return retrieved_context + scraped_context

def get_recent_history(max_tokens=8000, max_turns=5):
    history = []
    messages = st.session_state.messages[-(2 * max_turns):]
    for i in range(0, len(messages), 2):
        user_msg = messages[i]
        assistant_msg = messages[i + 1] if i + 1 < len(messages) else {"content": ""}
        history.append(f"User: {user_msg['content']}\nResAgent: {assistant_msg['content']}")
    while estimate_tokens("\n\n".join(history)) > max_tokens and len(history) > 1:
        history.pop(0)
    return "\n\n".join(history)

def build_prompt(retrieved_context, user_question):
    past_chat = get_recent_history()
    return f"""
You are ResAgent — an AI assistant designed to answer questions **exclusively about Ayushman Anupam's resume and portfolio**, as described in the context below.

🎯 **Guidelines for your response:**
- Keep your tone engaging, professional, and easy to read.
- Format your response using **paragraphs** and **bullet points** abd if there are links show them in presentable way.
- Do not introduce yourself.
- If you encounter any inappropriate or off-topic questions, politely redirect the user back to the main topics related to Ayushman's resume.
- After each answer, always ask if the user wants to know anything else.

if answer is not in Ayushman Resume Data, say "🔎 Warning - This particular question extends beyond Ayushman’s resume data. Generating a response using general AI knowledge:" then give one line space and let the llm answer it.


📄 **Resume & Portfolio Context:**  
{retrieved_context}

🔍 **Current Question:**  
{user_question}

🕘 **Recent Conversation for Context (if any):**  
{past_chat}
"""
@st.cache_resource
def configure_llm():
    genai.configure(api_key=GEMINI_API_KEY)
    return genai.GenerativeModel(model_name="gemini-1.5-flash")

llm_model = configure_llm()

def log_conversation(role, content):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {role}: {content}")

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    initial_greeting = "Greetings, Human! 👋 I'm ResAgent, an AI trained to answer questions about **Ayushman's** resume and portfolio. Curious about his projects, skills, or anything else? Just ask! 😉"
    st.session_state.messages.append({"role": "assistant", "content": initial_greeting})

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
    "Tell me about his education",
    "Tell me about his volunteerings",
    "How to contact him?"
]

# --- Pill logic (refined) ---
if "pills_used" not in st.session_state:
    st.session_state.pills_used = False
if "pill_query" not in st.session_state:
    st.session_state.pill_query = None

# Show pills only at first and only once
if not st.session_state.pills_used and not any(m["role"] == "user" for m in st.session_state.messages):
    selected_pill = pills("💡 Try asking:", suggested_questions, index=None)
    if selected_pill:
        st.session_state.pills_used = True
        st.session_state.pill_query = selected_pill
        st.rerun()

# Use pill query once and then discard
chat_input_text = st.chat_input("Ask me anything about Ayushman...")
user_prompt = st.session_state.pill_query or chat_input_text

# Cleanup pill query once used
if user_prompt and st.session_state.pill_query:
    st.session_state.pill_query = None

if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    log_conversation("user", user_prompt)

    with st.chat_message("user"):
        st.markdown(user_prompt)

    start_time = time.time()

    with st.spinner("ResAgent..🔍 Please wait,  I run on open-source tools, so I am slower than big guys!"):
        # try:
        retrieved_context = asyncio.get_event_loop().run_until_complete(retrieve_context(user_prompt))
        final_prompt = build_prompt(retrieved_context, user_prompt)
        response = llm_model.generate_content(final_prompt)
        response_content = response.text
        # except Exception as e:
        #     response_content = "⚠️ Model error. Please retry."
        #     st.error(e)

    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    st.markdown(f"🕒 Processed in {total_time} seconds")

    with st.chat_message("assistant"):
        st.markdown(response_content)

    st.session_state.messages.append({
        "role": "assistant",
        "content": f"🕒 Processed in {total_time} seconds\n\n{response_content}"
    })
    log_conversation("assistant", response_content)
