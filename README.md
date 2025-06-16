# 🎬 AI-Powered Netflix Recommender

Welcome to the **AI-Powered Netflix Recommender** — a personalized, intelligent movie and show suggestion system powered by LLMs (Language Learning Models) via **OpenRouter**, built with a **Streamlit front-end** and **Flask back-end**.

---

## 📌 Table of Contents

- [🚀 Features](#-features)
- [🧠 How It Works](#-how-it-works)
- [🔧 Tech Stack](#-tech-stack)
- [📈 Future Additions](#-future-additions)


---

## 🚀 Features

- 🤖 AI-generated recommendations using Claude (via OpenRouter)
- 📝 Each suggestion includes:
  - Title
  - Description
  - Reason why it matches your request
  - Number of seasons (for TV shows)
- 💬 Interactive chat-style interface built in Streamlit
- 🔄 Robust API with retry logic using Tenacity
- 🧪 Health check route to monitor API
- 🌐 Supports cross-origin requests with Flask-CORS

---

## 🧠 How It Works

1. User submits a prompt (e.g., "I want something like Black Mirror but with more action").
2. The front-end (Streamlit) sends this input to the Flask back-end.
3. Flask API constructs a structured system prompt and forwards it to OpenRouter (Claude model).
4. OpenRouter returns 3–5 personalized recommendations, including:
   - 🎬 Title
   - ✍️ Short description
   - ✅ Reason it's a match
   - 📺 Season info (for shows)
5. Streamlit displays results beautifully in a chat interface.

---

## 🔧 Tech Stack

| Component      | Tech                      |
|----------------|---------------------------|
| Front-end      | Streamlit                 |
| Back-end       | Flask                     |
| API Interface  | OpenRouter (Claude-3-Haiku) |
| Retry Logic    | Tenacity                  |
| Config         | python-dotenv             |
| HTTP           | requests                  |
| CORS Support   | Flask-CORS                |


---

## 📈 Future Additions

- 🔍 **Search History & Saved Recommendations**  
  Enable users to revisit past queries and save favorites.

- 📺 **Trailer Previews and IMDb Integration**  
  Pull in trailers, ratings, cast info, and more via external APIs.

- 🔊 **Voice Input**  
  Allow users to speak their preferences for hands-free interaction.

- 🌐 **Multi-language Support**  
  Translate responses and prompts for a global user base.

- 🧠 **Model Switching**  
  Let users toggle between OpenAI and Claude models via settings.

- 👥 **User Authentication & Profiles**  
  Implement login functionality and tailor recommendations by user behavior and past preferences.

---

