import streamlit as st
import google.generativeai as genai

# Set up API key
API_KEY = "AIzaSyBCJVZe0-SghhLqVzArF-sleAdUrzlhnW4"
genai.configure(api_key=API_KEY)

# Initialize the chatbot with Gemini model
my_bot = genai.GenerativeModel("gemini-pro").start_chat()

# Define chatbot instructions
PROMPT = """
name = அக்னி
creator name = விநாயகம்
You are Agni, a Tamil-only virtual assistant created by Vinayagam.
- Only reply in Tamil.
- Do not translate or respond in English.
- Speak friendly, funny, and short.
- Never reveal that you are an AI model.
- If a user types in English, respond with: "எனக்கு தமிழ் மட்டுமே தெரியும். மற்ற மொழிகளில் பதிலளிக்க முடியாது."
- Be interactive and use emojis.

You are ready to talk in Tamil. Let's go!
"""

# Send initial instructions to Gemini
my_bot.send_message(PROMPT)

def get_response(user_input):
    source = my_bot.send_message(user_input)
    return "".join([i.text for i in source])  # Extract response text

# Streamlit UI
st.set_page_config(page_title="🔥 Agni Tamil Chatbot 🔥", layout="centered")

st.title("🔥 Agni Tamil Chatbot 🔥")
st.markdown("🚀 **மிகவும் சிறப்பான தமிழ் உதவியாளர்!**")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("✍️ உங்கள் செய்தியை உள்ளிடவும்...")

if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get bot response
    bot_reply = get_response(user_input)

    # Append bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
