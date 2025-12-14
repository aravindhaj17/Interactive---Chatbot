🤖 Gemini DSA Tutor — Terminal-Based AI for Serious Learning

A free-tier optimized Gemini-powered DSA tutor that runs entirely in your terminal.
Built for daily learning, clear explanations, and long sessions — without burning API quota.

✨ Why This Project

Most AI chatbot demos:

Look good once

Break after a few messages

Burn free API quota fast

Are cluttered with markdown and UI noise

This project was built to solve that.

Goals:

Run locally inside VS Code / Terminal

Explain Data Structures & Algorithms only

Produce plain-text, human-readable answers

Stay usable on the Gemini free tier

Feel like a real study companion, not a demo

🚀 Features

💬 Interactive chat directly in the terminal

🎓 DSA-only tutor mode (refuses non-DSA questions)

🧠 Plain-text explanations (no markdown clutter)

🔄 Reset command to clear context and save tokens

📊 Message usage counter per session

💾 Local chat history saved as JSON

🔊 Optional Text-to-Speech (TTS) support

⚡ Uses Gemini Flash for speed and free-tier efficiency

🧪 Graceful handling of quota and rate-limit errors

🧩 What Makes It Different

No browser UI — pure terminal productivity

No markdown spam — clean readable answers

Designed for real daily use, not just demos

Free-tier aware — reset before quota pain

Ideal for DSA practice and interview prep

Most projects stop at “Hello World”.
This one survives real learning sessions.

🛠️ Tech Stack

Python 3.11

Google Gemini API

google-generativeai

python-dotenv

pyttsx3 (offline TTS)

Runs entirely inside VS Code / Terminal.

📁 Project Structure
API/
├── chat.py              # Main DSA tutor chatbot
├── chat_history.json    # Auto-created local chat history
├── .env                 # Gemini API key
├── README.md            # Project documentation
├── venv/                # Python virtual environment

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/your-username/gemini-dsa-tutor.git
cd gemini-dsa-tutor

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install google-generativeai python-dotenv pyttsx3

4️⃣ Add your Gemini API key

Create a .env file:

GEMINI_API_KEY=your_api_key_here


Get your API key from:
👉 https://aistudio.google.com/app/apikey

▶️ Run the Tutor
python chat.py


You’ll see:

Gemini DSA Tutor (Free Tier Optimized)
Commands:
  reset  -> clear chat history
  exit   -> quit

💬 Example Usage
You: explain stack
Bot: A stack is a data structure that follows the Last In, First Out principle...


Reset when needed:

You: reset
Chat reset (history cleared)
