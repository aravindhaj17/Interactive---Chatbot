import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def chat():
    # Configure Gemini
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    # Free-tier friendly model
    model = genai.GenerativeModel(
        "models/gemini-flash-latest",
        system_instruction=(
            "Respond in plain text only. "
            "Do not use markdown, asterisks (*), bold text, tables, or separators. "
            "Use simple paragraphs and numbered lists. "
            "Keep answers concise and easy to understand."
        )
    )

    # Start chat session
    chat_session = model.start_chat(history=[])

    print("\nGemini Chat")
    print("Commands:")
    print("  exit  -> quit chat")
    print("  reset -> clear chat history (recommended)\n")

    while True:
        user_input = input("You: ").strip()

        # Exit command
        if user_input.lower() in ["exit", "quit"]:
            print("Bye!")
            break

        # Reset command (VERY IMPORTANT for free tier)
        if user_input.lower() == "reset":
            chat_session = model.start_chat(history=[])
            print("Chat history cleared.\n")
            continue

        # Send message safely
        try:
            response = chat_session.send_message(user_input)
            print("Bot:", response.text, "\n")

        except Exception as e:
            error_msg = str(e).lower()

            if "quota" in error_msg or "429" in error_msg:
                print("Rate limit reached.")
                print("Tip: wait 30 seconds or type 'reset' to continue.\n")
            else:
                print("Unexpected error:", e, "\n")

if __name__ == "__main__":
    chat()
