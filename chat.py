import os
import json
from datetime import datetime

import google.generativeai as genai
from dotenv import load_dotenv
import pyttsx3

# ------------------ CONFIG ------------------

load_dotenv()

MODEL_NAME = "models/gemini-flash-latest"  # free-tier safe
HISTORY_FILE = "chat_history.json"
MAX_MESSAGES_PER_SESSION = 100

DSA_MODE = True        # DSA-only tutor
VOICE_ENABLED = True   # Text-to-Speech

# ------------------ INIT ------------------

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    if VOICE_ENABLED:
        engine.say(text)
        engine.runAndWait()

model = genai.GenerativeModel(
    MODEL_NAME,
    system_instruction=(
        "You are a DSA tutor. "
        "Answer only Data Structures and Algorithms questions. "
        "Explain in simple plain text. "
        "Do not use markdown, asterisks, bold text, tables, or separators. "
        "If the question is not related to DSA, politely refuse."
    )
)

chat_session = model.start_chat(history=[])

message_count = 0

# ------------------ UTILITIES ------------------

def save_message(role, text):
    data = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

    data.append({
        "time": datetime.now().isoformat(),
        "role": role,
        "text": text
    })

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def reset_chat():
    global chat_session, message_count
    chat_session = model.start_chat(history=[])
    message_count = 0
    print("🔄 Chat reset (history cleared)\n")

# ------------------ CHAT LOOP ------------------

if os.environ.get("CI") == "true":
    print("Chatbot loaded successfully (CI mode)")
    exit(0)

print("\nGemini DSA Tutor (Free Tier Optimized)")
print("Commands:")
print("  reset  -> clear chat history")
print("  exit   -> quit\n")


while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("Bye!")
        break

    if user_input.lower() == "reset":
        reset_chat()
        continue

    if message_count >= MAX_MESSAGES_PER_SESSION:
        print("⚠️ Message limit reached. Type 'reset' to continue.\n")
        continue

    try:
        message_count += 1
        print(f"[Usage] Messages used: {message_count}/{MAX_MESSAGES_PER_SESSION}")

        save_message("user", user_input)

        response = chat_session.send_message(user_input)
        bot_text = response.text.strip()

        print("Bot:", bot_text, "\n")
        speak(bot_text)

        save_message("bot", bot_text)

    except Exception as e:
        err = str(e).lower()

        if "quota" in err or "429" in err:
            print("⚠️ Rate limit reached.")
            print("⏳ Wait 30 seconds or type 'reset'.\n")
        else:
            print("❌ Error:", e, "\n")
