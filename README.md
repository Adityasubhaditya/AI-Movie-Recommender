# 🎬 Flick Finder — AI-Powered Netflix Recommender

Welcome to **Flick Finder**, your intelligent streaming companion. Powered by advanced LLMs via **OpenRouter** and built with a sleek **Streamlit front-end** and a robust **Flask back-end**, Flick Finder delivers hyper-personalized movie and TV show recommendations.

---

## 📌 Table of Contents

- [🚀 Features](#-features)
- [🧠 How It Works](#-how-it-works)
- [🔧 Tech Stack](#-tech-stack)
- [📈 Future Additions](#-future-additions)

---

## 🚀 Features

- 🤖 AI-generated recommendations using Claude (via OpenRouter)
- 📝 Every suggestion includes:
  - 🎬 Title
  - ✍️ Short description
  - ✅ Why it fits your prompt
  - 📺 Number of seasons (for shows)
- 💬 Interactive, chat-style UI built in Streamlit
- 🔄 Smart retry logic using Tenacity for resilient API calls
- 🧪 Built-in health check endpoint
- 🌐 CORS support via Flask-CORS for cross-platform integration

---

## 🧠 How It Works

1. Enter a prompt (e.g., "I love Stranger Things but want something more psychological").
2. The **Streamlit front-end** sends the prompt to the **Flask API**.
3. Flask constructs a system prompt and forwards it to **Claude-3-Haiku** via **OpenRouter**.
4. Claude responds with 3–5 tailored recommendations, each with:
   - 🎬 Title  
   - ✍️ Description  
   - ✅ Explanation for the match  
   - 📺 Season count (for series)
5. The front-end displays everything in a clean, conversational interface.

---

## 🔧 Tech Stack

| Component      | Technology                  |
|----------------|-----------------------------|
| Front-end      | Streamlit                   |
| Back-end       | Flask                       |
| AI Model API   | OpenRouter (Claude-3-Haiku) |
| Retry Logic    | Tenacity                    |
| Configuration  | python-dotenv               |
| HTTP Requests  | requests                    |
| CORS Handling  | Flask-CORS                  |

---

## 📈 Future Additions

- 🔍 **Search History & Saved Recommendations**  
  Users can revisit past prompts and bookmark favorite picks.

- 📺 **Trailers & IMDb Integration**  
  Show trailers, ratings, cast info, and more using third-party APIs.

- 🎙️ **Voice Input Support**  
  Let users speak their preferences for hands-free recommendations.

- 🌍 **Multi-language Capability**  
  Translate prompts and suggestions for global accessibility.

- 🧠 **Model Switching**  
  Users can choose between Claude, OpenAI, or other models.

- 👤 **User Profiles & Authentication**  
  Add login functionality to personalize recommendations further.

---

