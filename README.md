🤖 Gemini Flash Chat — A Local AI Tutor in Your Terminal

A fast, free-tier friendly Gemini chatbot that lives inside your VS Code terminal — built for learning, not burning quota.

✨ Why I Built This

I wanted:

A simple AI chat without web UI distractions

Something that works locally in VS Code

A bot that explains DSA, coding concepts, and theory clearly

And most importantly… doesn’t eat up free API quota in 5 minutes

So I built this.

🚀 What This Chatbot Can Do

💬 Chat directly in your terminal

📘 Explain DSA concepts (Binary Search, Trees, DP, etc.)

🧠 Give plain-text, human-readable answers (no markdown noise)

🔄 Reset conversation to save free-tier quota

⚡ Uses Gemini Flash — fast & quota-friendly

🧪 Handles rate-limit errors gracefully

🧩 What Makes This Different (Not a Generic Bot)

✔ No UI — pure terminal productivity
✔ No markdown spam — clean readable text
✔ Free-tier optimized — reset before quota pain
✔ Beginner-friendly — great for learning DSA & CS concepts

Most demos stop at “Hello World”.
This one survives real usage.

🛠️ Tech Stack

-> Python 3.11

-> Google Gemini API

-> google-generativeai

API/
├── chat.py        # Main chatbot script
├── .env           # Gemini API key
├── README.md      # You’re reading it
├── venv/          # Python virtual environment

⚙️ Setup Instructions

1️⃣ Clone the repo
git clone https://github.com/your-username/gemini-flash-chat.git
cd gemini-flash-chat

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install google-generativeai python-dotenv

4️⃣ Add API key

Create a .env file:

GEMINI_API_KEY=your_api_key_here


Get your key from 👉 https://aistudio.google.com/app/apikey

▶️ Run the Chatbot
python chat.py


You’ll see:

Gemini Chat
Commands:
  exit  -> quit chat
  reset -> clear chat history

💬 Example Usage
You: explain binary search
Bot: Binary search is a divide and conquer algorithm that works on sorted arrays...


Reset when needed:

You: reset
Chat history cleared.



python-dotenv

Runs inside VS Code / Terminal
