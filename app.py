import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌐",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Hide default Streamlit header */
header {
    visibility: hidden;
}

/* Background */
.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Main Title */
h1 {
    text-align: center;
    color: #00d4ff;
    font-size: 48px;
    font-weight: bold;
    margin-bottom: 20px;
}

/* Labels (IMPORTANT FIX) */
label, .stSelectbox label, .stTextArea label {
    color: white !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] {
    background-color: white;
    border-radius: 10px;
    border: 2px solid #00d4ff;
}

/* Text Area */
.stTextArea textarea {
    background-color: white;
    color: black;
    border-radius: 10px;
    border: 2px solid #00d4ff;
    font-size: 16px;
    padding: 10px;
}

/* Button */
.stButton button {
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    width: 100%;
    height: 50px;
    border: none;
    transition: 0.3s ease;
}

/* Hover Effect */
.stButton button:hover {
    transform: scale(1.02);
}

/* Result Text */
.result-text {
    font-size: 26px;
    font-weight: bold;
    margin-top: 15px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🌐 AI Language Translator")

# ---------------- LANGUAGES ----------------
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-cn"
}

# ---------------- LANGUAGE SELECTION ----------------
source_lang = st.selectbox("🌍 Source Language", list(languages.keys()))
target_lang = st.selectbox("🎯 Target Language", list(languages.keys()))

# ---------------- TEXT INPUT ----------------
text = st.text_area("✍ Enter Text to Translate")

# ---------------- TRANSLATE BUTTON ----------------
if st.button("🚀 Translate Now"):

    if text.strip() == "":
        st.warning("⚠ Please enter some text to translate")

    else:
        # Translation
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("✅ Translation Completed")

        # Output text
        st.write("### 🔹 Translated Text")
        st.markdown(
            f'<div class="result-text">{translated}</div>',
            unsafe_allow_html=True
        )

        # Text to Speech
        tts = gTTS(text=translated, lang=languages[target_lang])
        tts.save("translated_audio.mp3")

        # Play audio
        audio_file = open("translated_audio.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")
