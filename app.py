import streamlit as st
from deep_translator import GoogleTranslator

# Page Config
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #667eea, #764ba2, #ff6ec4);
    background-size: 400% 400%;
    animation: gradient 12s ease infinite;
    color: white;
}

@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.main-box {
    background: rgba(255,255,255,0.15);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

h1 {
    text-align: center;
    color: white;
    font-size: 50px;
    font-weight: bold;
}

.stTextArea textarea {
    background-color: rgba(255,255,255,0.85);
    color: black;
}

.stSelectbox div[data-baseweb="select"] {
    background-color: rgba(255,255,255,0.85);
    border-radius: 12px;
    color: black;
}


.stButton button {
    background: linear-gradient(to right, #ff512f, #dd2476);
    color: white;
    font-size: 20px;
    border-radius: 15px;
    width: 100%;
    height: 55px;
    border: none;
    font-weight: bold;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.05);
    background: linear-gradient(to right, #24c6dc, #514a9d);
}

.result-box {
    background: rgba(255,255,255,0.2);
    padding: 20px;
    border-radius: 15px;
    margin-top: 25px;
    font-size: 22px;
    color: white;
    border: 2px solid white;
}

</style>
""", unsafe_allow_html=True)

# Main Container
st.markdown('<div class="main-box">', unsafe_allow_html=True)

# Title
st.title("🌍 AI Language Translator")

# Text Input
text = st.text_area("Enter Text")

# Languages
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

# Dropdowns
source_lang = st.selectbox("Source Language", list(languages.keys()))
target_lang = st.selectbox("Target Language", list(languages.keys()))

# Translate Button
if st.button("✨ Translate Now"):

    translated = GoogleTranslator(
        source=languages[source_lang],
        target=languages[target_lang]
    ).translate(text)

    st.markdown(
        f"""
        <div class="result-box">
        <h3>✅ Translated Text</h3>
        {translated}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)