# app.py
import streamlit as st
import requests

st.set_page_config(page_title="Langchain RAG Chatbot", layout="wide")

BACKEND_URL = "http://localhost:8000"  # ← Your URL

# -----------------------------------------------
# 💅 CSS - Same as image!
# -----------------------------------------------
st.markdown(
    """
<style>
/* ---- LIGHT WHITE THEME ---- */
.stApp { background: #f5f5f5; font-family: 'Segoe UI', sans-serif; }

[data-testid="stSidebar"] {
    background: white !important;
    border-right: 1px solid #e0e0e0;
    padding: 1rem;
}
[data-testid="stSidebar"] * { color: #333 !important; }

/* ---- SELECTBOX ---- */
[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
    background: white !important;
    border: 1px solid #ddd !important;
    border-radius: 8px !important;
}

/* ---- FILE UPLOADER ---- */
[data-testid="stFileUploader"] {
    background: white !important;
    border: 2px dashed #ccc !important;
    border-radius: 10px !important;
    padding: 10px !important;
}

/* ---- UPLOAD BUTTON ---- */
.stButton button {
    background: white !important;
    color: #333 !important;
    border: 1px solid #ddd !important;
    border-radius: 8px !important;
    padding: 6px 20px !important;
    font-size: 0.9rem !important;
    width: 100% !important;
}
.stButton button:hover {
    background: #f0f0f0 !important;
    border-color: #bbb !important;
}

/* ---- MAIN TITLE ---- */
.main-title {
    text-align: center;
    font-size: 2rem;
    font-weight: 700;
    color: #222;
    margin-bottom: 1.5rem;
}

/* ---- CHAT AREA ---- */
.chat-area {
    background: white;
    border-radius: 16px;
    padding: 20px;
    min-height: 450px;
    max-height: 500px;
    overflow-y: auto;
    border: 1px solid #e8e8e8;
    margin-bottom: 1rem;
}

/* ---- CHAT ROWS ---- */
.chat-row {
    display: flex;
    align-items: flex-start;
    margin: 12px 0;
    gap: 12px;
}

/* ---- AVATAR CIRCLES ---- */
.avatar-red {
    width: 36px; height: 36px; min-width: 36px;
    background: #e74c3c;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem;
}
.avatar-orange {
    width: 36px; height: 36px; min-width: 36px;
    background: #f39c12;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem;
}

/* ---- MESSAGE TEXT ---- */
.msg-text {
    background: #f9f9f9;
    border: 1px solid #eee;
    border-radius: 12px;
    padding: 10px 16px;
    color: #333;
    font-size: 0.95rem;
    line-height: 1.5;
    flex: 1;
}

/* ---- QUERY INPUT ---- */
.stTextInput input {
    background: white !important;
    border: 1px solid #ddd !important;
    border-radius: 10px !important;
    color: #333 !important;
    caret-color: #333 !important;
    padding: 12px 16px !important;
    font-size: 0.95rem !important;
}
.stTextInput input::placeholder { color: #aaa !important; }
.stTextInput input:focus { border-color: #aaa !important; }

/* ---- DOC ITEM ---- */
.doc-item {
    background: #f7f7f7;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 7px 12px;
    margin: 4px 0;
    color: #444 !important;
    font-size: 0.82rem;
}

/* ---- SEND BUTTON ---- */
.send-btn button {
    background: #f0f0f0 !important;
    border: 1px solid #ddd !important;
    border-radius: 8px !important;
    color: #555 !important;
    font-size: 1.1rem !important;
}

/* ---- EMPTY STATE ---- */
.empty-state {
    text-align: center;
    color: #bbb;
    margin-top: 180px;
    font-size: 1rem;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------
# SESSION SETUP
# -----------------------------------------------
if "session_id" not in st.session_state:
    try:
        res = requests.get(f"{BACKEND_URL}/new-session", timeout=10)
        st.session_state.session_id = res.json()["session_id"]
    except:
        st.error("❌ Cannot connect to backend! Check BACKEND_URL")
        st.stop()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "documents" not in st.session_state:
    st.session_state.documents = []

# -----------------------------------------------
# 📌 SIDEBAR - Exact same as image!
# -----------------------------------------------
with st.sidebar:
    # Model Selector
    st.markdown("**Model**")
    model = st.selectbox(
        "", ["llama-3.3-70b-versatile", "gpt-4o-mini"], label_visibility="collapsed"
    )

    st.markdown("---")

    # Upload Document
    st.markdown("**Upload Document**")
    st.caption("Choose a file")
    uploaded_file = st.file_uploader(
        "", type=["pdf", "docx"], label_visibility="collapsed"
    )

    if uploaded_file:
        if st.button("Upload"):
            with st.spinner("Uploading..."):
                try:
                    files = {
                        "file": (uploaded_file.name, uploaded_file, uploaded_file.type)
                    }
                    res = requests.post(
                        f"{BACKEND_URL}/upload", files=files, timeout=60
                    )
                    if res.status_code == 200:
                        st.success(f"✅ Done!")
                        if uploaded_file.name not in st.session_state.documents:
                            st.session_state.documents.append(uploaded_file.name)
                    else:
                        st.error("❌ Upload failed!")
                except Exception as e:
                    st.error(f"❌ {str(e)}")

    st.markdown("---")

    # Uploaded Documents List
    st.markdown("**Uploaded Documents**")
    if st.button("🔄 Refresh Document List"):
        st.rerun()

    if st.session_state.documents:
        for doc in st.session_state.documents:
            st.markdown(f'<div class="doc-item">📄 {doc}</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            '<div class="doc-item">No documents yet</div>', unsafe_allow_html=True
        )

    st.markdown("---")

    # Delete Document
    if st.session_state.documents:
        st.markdown("**Select a document to delete**")
        doc_to_delete = st.selectbox(
            "", st.session_state.documents, label_visibility="collapsed"
        )
        if st.button("🗑️ Delete Selected Document"):
            st.session_state.documents.remove(doc_to_delete)
            st.success(f"Deleted {doc_to_delete}")
            st.rerun()

# -----------------------------------------------
# 🏠 MAIN AREA
# -----------------------------------------------
st.markdown(
    '<div class="main-title">Langchain RAG Chatbot</div>', unsafe_allow_html=True
)

# ---- Chat Area ----
chat_html = '<div class="chat-area">'

if not st.session_state.chat_history:
    chat_html += '<div class="empty-state">Ask a question to get started 💬</div>'
else:
    for msg in st.session_state.chat_history:
        if msg["role"] == "human":
            chat_html += f"""
            <div class="chat-row">
                <div class="avatar-red">🧑</div>
                <div class="msg-text">{msg["content"]}</div>
            </div>"""
        else:
            chat_html += f"""
            <div class="chat-row">
                <div class="avatar-orange">🤖</div>
                <div class="msg-text">{msg["content"]}</div>
            </div>"""

chat_html += "</div>"
st.markdown(chat_html, unsafe_allow_html=True)

# ---- Query Input ----
col1, col2 = st.columns([6, 1])
with col1:
    question = st.text_input(
        "", placeholder="Query:", label_visibility="collapsed", key="query_box"
    )
with col2:
    with st.container():
        st.markdown('<div class="send-btn">', unsafe_allow_html=True)
        send = st.button("➤")
        st.markdown("</div>", unsafe_allow_html=True)

# ---- Send Logic ----
if send and question:
    with st.spinner("Thinking..."):
        try:
            res = requests.post(
                f"{BACKEND_URL}/chat",
                json={"session_id": st.session_state.session_id, "question": question},
                timeout=60,
            )
            if res.status_code == 200:
                answer = res.json()["answer"]
                st.session_state.chat_history.append(
                    {"role": "human", "content": question}
                )
                st.session_state.chat_history.append({"role": "ai", "content": answer})
                st.rerun()
            else:
                st.error(f"❌ Error {res.status_code}")
        except requests.exceptions.Timeout:
            st.error("⏱️ Timeout! Is Colab still running?")
        except requests.exceptions.JSONDecodeError:
            st.error("❌ Empty response! Check if Colab is running!")
        except Exception as e:
            st.error(f"❌ {str(e)}")
