import streamlit as st

st.set_page_config(page_title="SSCi Chatbot",page_icon="image\logo.png", layout="wide", initial_sidebar_state="expanded")

# --- Sidebar ---
st.sidebar.image("image\SSCiNewLogo.png", width=200, use_container_width=True)
st.sidebar.markdown("### Options")
st.sidebar.button("How to write an impacting...")
st.sidebar.button("Web accessibility")
st.sidebar.button("Design inspiration")
st.sidebar.button("What is machine learning")

st.sidebar.markdown("---")
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #202020; /* Dark background */
            color: white; /* White text */
        }
        .sidebar-item {
            display: flex;
            align-items: center;
            font-size: 16px;
            padding: 10px 0;
        }
        .sidebar-item img {
            width: 20px;
            height: 20px;
            margin-right: 10px;
        }
        .sidebar-item span {
            color: white;
            font-weight: normal;
        }
        .logout-btn {
            color: red;
            font-weight: bold;
            display: flex;
            align-items: center;
        }
        .logout-btn img {
            margin-right: 10px;
            width: 20px;
            height: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar items
with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-item">
            <img src="https://img.icons8.com/m_rounded/512/FFFFFF/trash.png" alt="Clear conversations">
            <span>Clear all conversations</span>
        </div>
        <div class="sidebar-item">
            <img src="https://img.icons8.com/fluent-systems-filled/512/FFFFFF/external-link.png" alt="Updates">
            <span>Updates & FAQ</span>
        </div>
        <div class="logout-btn">
            <img src="https://uxwing.com/wp-content/themes/uxwing/download/controller-and-music/turn-off-icon.png" alt="Updates">
            <span>Log out</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <style>
        .main-container {
            background-color: #202020;
            color: white;
            text-align: center;
            font-family: Arial, sans-serif;
            padding-top: 50px;
        }
        .header {
            font-size: 40px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .subheader {
            font-size: 18px;
            color: #888888;
        }
        .chat-box {
            margin: 50px auto;
            width: 60%;
            text-align: center;
        }
        .features-container {
            display: flex;
            justify-content: center;
            margin-top: 50px;
        }
        .feature {
            width: 200px;
            margin: 0 20px;
            text-align: center;
        }
        .feature h3 {
            margin: 10px 0;
            font-size: 18px;
        }
        .feature p {
            font-size: 14px;
            color: #cccccc;
        }
    </style>
    <div class="main-container">
        <div class="header">Welcome to SSCi</div>
        <div class="subheader">The power of AI at your service - Tame the knowledge!</div>
        <div class="chat-box">
            <input type="text" style="width: 70%; padding: 10px;" placeholder="Message chatbot:">
            <button style="padding: 10px 20px; background-color: #0078D7; color: white; border: none;">&#9654;</button>
        </div>
        <div class="features-container">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
