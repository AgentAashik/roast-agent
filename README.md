# Roast Agent 🤖🔥

A **LangChain-based AI agent** that humorously roasts users using their own social media data (provided by the company).  
This is a **fun, lighthearted project** — think witty stand-up comedy, not harassment.  

---

## 🚀 Features
- ✅ Fetches open social media data (mocked in code, replace with API).  
- ✅ Generates **playful, sarcastic roasts** in 3–5 sentences.  
- ✅ Powered by **LangChain Agents** and your choice of LLM (OpenAI, Gemini, etc.).  
- ✅ Easy to extend with more tools (e.g., sentiment analysis, roast intensity levels).  

---

## 📂 Project Structure
```

roast-agent/
│
├── roast\_agent.py   # Main LangChain agent + roast tool
├── README.md        # Documentation

```
## ⚙️ Requirements

- Python 3.9+
- [LangChain](https://python.langchain.com/)  
- An LLM backend (OpenAI, Gemini, or LiteLLM-supported)  
- Install dependencies:
  ```bash
  pip install langchain openai


---

## 🔧 Usage

### 1. Clone Repo

```bash
git clone https://github.com/AgentAashik/roast-agent.git
cd roast-agent
```

### 2. Run Locally

```bash
python roast_agent.py --user_id 12345
```

---

## 🧠 How It Works

1. **fetch\_user\_data()** – Loads mock JSON of bio, posts, likes (replace with real API).
2. **roast\_user()** – Formats data + sends to LLM with a humorous roast prompt.
3. **LangChain Agent** – Wraps roast tool so you can extend with more features.

---

## 📊 Example Roast

```
🔥 Generating roast...

--- Roast Result ---

So your bio says “coffee is my personality” — brave of you to admit that
Starbucks owns your soul. You brag about a 5K that took 3 hours — pretty
sure toddlers crawl faster. And staying up until 4am watching cat videos?
Truly the Olympian of procrastination.
```

---

## 🛠️ Development

* Replace `fetch_user_data()` with a real company API call.
* Modify the roast prompt for **mild / spicy / brutal** roast modes.
* Add FastAPI/Flask routes to expose as a microservice.
* Hook up a React frontend for live roast demos.

---

## 📌 Roadmap

* [ ] Roast intensity levels (PG-13 → Savage)
* [ ] Web dashboard with roast history
* [ ] Integration with multiple LLMs (Gemini, Claude, etc.)

---

## ⚠️ Disclaimer

This project is for **entertainment purposes only**.
Roasts are intended to be **humorous, not harmful**.
Do not use in contexts where playful sarcasm could be mistaken for harassment.

---

## 📜 License

MIT License – free to use, modify, and distribute.
