import streamlit as st
from PIL import Image

# --- Configuration ---
st.set_page_config(
    page_title="SSCI Chatbot",
    page_icon="image/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Sidebar styles */
    .sidebar .sidebar-content {
        background-color: #1a1d21; /* Dark background */
        color: white;
    }
    .sidebar .stButton>button {
        background-color: #007bff; /* Blue button */
        color: white;
    }

    /* Main area styles */
    .main {
        background: linear-gradient(to bottom, #282c34, #212529); /* Dark gradient */
        color: white;
        padding: 2rem;
    }

    /* Chat input styles */
    .stChatInputContainer {
        background-color: rgba(0, 0, 0, 0.3); /* Slightly transparent black */
        border-radius: 20px;
        padding: 0.5rem 1rem;
    }

    /* Feature boxes */
    .feature-box {
        background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent black */
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.image("image/SSCiNewLogo.png", width=500)
st.sidebar.button("Clear all conversations")
if "light_mode" not in st.session_state:
  st.session_state.light_mode = False
light_mode = st.sidebar.checkbox("Switch Light Mode", value = st.session_state.light_mode)
st.session_state.light_mode = light_mode
st.sidebar.button("Updates & FAQ")
st.sidebar.button("Log out", type = "primary")

# --- Main Area ---
st.title("Welcome to SSCI")
st.write("The power of AI at your service - Tame the knowledge!")
prompt = st.chat_input("Message chatbot :", key="unique_chat_input") 
st.markdown(
    """
    <style>
    /* Style the send button */
    button[kind="primary"][data-testid="stChatInputSendButton"] {
        background-color: #007bff; /* Blue color */
        color: white;
        border: none;
        border-radius: 50%; /* Make it round */
        width: 40px; /* Adjust size as needed */
        height: 40px;
    }
    button[kind="primary"][data-testid="stChatInputSendButton"] svg {
        display: block;
        margin: 0 auto; 
    }

     [data-testid="stChatInputContainer"]  > label { /* Hides the label */
       visibility: hidden;
    }
     [data-testid="stChatInputContainer"]  { /* Styles for input text container */
       margin-bottom:20px!important;
    }
    /* Other st-chat-input styles */
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
