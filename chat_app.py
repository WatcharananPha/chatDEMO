import streamlit as st
from PIL import Image

# ---  Config Page  ----
st.set_page_config(
    page_title="SSCI Chatbot",
    page_icon="image\logo.png   ",
    layout="wide"
)

# --- Style setting ---
st.markdown("""
<style>
    .css-qbe2hs { /* Styles for the bot message bubbles */
        background-color: rgba(255,255,255,0.1)!important;
        border-radius:15px!important;
        padding:0.5em 1.5em 0.5em 1.5em!important;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .css-10trblm { /* Styles for the user message bubbles */
        background-color: rgba(239,239,239,0.5)!important;
        padding:0.5em 1.5em 0.5em 1.5em!important;
        border-radius:15px!important;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    /* Style the chat input area */
    textarea[data-testid="stChatInput"] {
        background-color: rgba(239, 239, 239, 0.5) !important;
        border-radius: 15px !important;
        padding: 0.5em 1em !important; /* Adjust padding as needed */
        border: none !important; /* Remove default border */
        font-size: 16px; /* Adjust font size as needed */
        outline: none;  /* Remove the focus outline*/
    }
</style>""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

ssci_logo = Image.open("image\SSCiNewLogo.png")
col1, col2 = st.columns([1, 15])

if ssci_logo:
    col1.image(ssci_logo, width=1000)

col2.markdown(
    f"""<p style="font-size:20px">Hello, I am a Chatbot, how may I help you?</p>""",
    unsafe_allow_html=True
)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"]) 

if prompt := st.chat_input("Message:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt) 
    if prompt == "Hey, what's a chatbot?":
        response_text = """
            A chatbot or chatterbot is a software application used to conduct 
            an on-line chat conversation via text or text-to-speech, in lieu of 
            providing direct contact with a live human agent. Designed to 
            convincingly simulate the way a human would behave as a 
            conversational partner, chatbot systems typically require 
            continuous tuning and testing, and many in production remain
            unable to adequately converse, while none of them can pass the
            standard Turing test. The term "ChatterBot" was originally coined 
            by Michael Mauldin (creator of the first Verbot) in 1994 to 
            describe these conversational programs.
        """
    else:
        response_text = "I'm still learning! Ask me about what a chatbot is."
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    with st.chat_message("assistant"):
        st.markdown(response_text)