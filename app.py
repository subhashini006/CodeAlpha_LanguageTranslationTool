import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import speech_recognition as sr

# Page Configuration
st.set_page_config(
    page_title="AI Voice Translator",
    page_icon="🌐",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

/* Remove Header Space */
header {
    visibility: hidden;
}

.main .block-container {
    padding-top: 0rem;
    padding-bottom: 1rem;
}

/* Background */
.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    min-height: 100vh;
    color: white;
}

/* Title */
h1 {
    text-align: center;
    color: #00d4ff;
    font-size: 52px;
    font-weight: bold;
    margin-bottom: 30px;
    margin-top: 10px;
}

/* Labels */
label {
    color: white !important;
    font-size: 18px !important;
    font-weight: 600;
}

/* Text Area */
.stTextArea textarea {
    background-color: white;
    color: black;
    border-radius: 12px;
    border: 2px solid #00d4ff;
    font-size: 18px;
    padding: 12px;
}

/* Dropdown */
.stSelectbox div[data-baseweb="select"] {
    background-color: white;
    border-radius: 12px;
    color: black;
    border: 2px solid #00d4ff;
}

/* Buttons */
.stButton button {
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    font-size: 20px;
    font-weight: bold;
    border-radius: 12px;
    width: 100%;
    height: 55px;
    border: none;
    transition: 0.3s ease;
    margin-top: 10px;
}

/* Hover */
.stButton button:hover {
    transform: scale(1.02);
    background: linear-gradient(to right, #0072ff, #00c6ff);
}

/* Result Text */
.result-text {
    font-size: 30px;
    color: white;
    font-weight: bold;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🌐 AI Voice Language Translator")

# Languages Dictionary
languages = {
    "English": "en-IN",
    "Tamil": "ta-IN",
    "Hindi": "hi-IN",
    "French": "fr-FR",
    "German": "de-DE",
    "Spanish": "es-ES",
    "Japanese": "ja-JP",
    "Chinese": "zh-CN"
}

# Session State
if "voice_text" not in st.session_state:
    st.session_state.voice_text = ""

# Source Language
source_lang = st.selectbox(
    "🌍 Source Language",
    list(languages.keys())
)

# Target Language
target_lang = st.selectbox(
    "🎯 Target Language",
    list(languages.keys())
)

# Voice Input Button
if st.button("🎤 Speak"):

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            st.info("🎙 Speak Now...")

            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source)

            # Recognize Speech Based on Selected Language
            voice = recognizer.recognize_google(
                audio,
                language=languages[source_lang]
            )

            st.session_state.voice_text = voice

            st.success(f"✅ You Said: {voice}")

    except:
        st.error("❌ Could not recognize voice")

# Text Area
text = st.text_area(
    "✍ Enter Text or Use Voice",
    value=st.session_state.voice_text
)

# Translate Button
if st.button("🚀 Translate Now"):

    if text.strip() == "":
        st.warning("⚠ Please enter or speak some text")

    else:

        # Translation
        translated = GoogleTranslator(
            source=languages[source_lang].split("-")[0],
            target=languages[target_lang].split("-")[0]
        ).translate(text)

        # Success Message
        st.success("✅ Translation Completed")

        # Heading
        st.write("### 🔹 Translated Text")

        # Output
        st.markdown(
            f'<div class="result-text">{translated}</div>',
            unsafe_allow_html=True
        )

        # Text To Speech
        tts = gTTS(
            text=translated,
            lang=languages[target_lang].split("-")[0]
        )

        # Save Audio
        tts.save("translated_audio.mp3")

        # Play Audio
        audio_file = open("translated_audio.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")
