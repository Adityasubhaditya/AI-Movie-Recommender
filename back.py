from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("Missing OPENROUTER_API_KEY in .env")

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

OPENROUTER_API_URL = "https://api.openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "anthropic/claude-3-haiku"

SYSTEM_PROMPT = """
You are a Netflix recommendation expert. Provide:
1. 3-5 tailored recommendations
2. Brief descriptions
3. Why they match the request
4. Seasons info for shows
Format with emojis and clear sections.
"""

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def call_openrouter(messages):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
    }

    payload = {
        "model": DEFAULT_MODEL,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 800
    }

    try:
        response = requests.post(
            OPENROUTER_API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"OpenRouter API Error: {str(e)}")
        raise

@app.route("/api/recommend", methods=["POST"])
def recommend():
    try:
        data = request.get_json()
        if not data or "prompt" not in data:
            return jsonify({"error": "Missing 'prompt' in request"}), 400
        
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": data["prompt"]}
        ]

        response = call_openrouter(messages)
        ai_message = response["choices"][0]["message"]
        
        return jsonify({
            "response": ai_message["content"],
            "model": DEFAULT_MODEL
        })

    except Exception as e:
        logger.exception("Error in /api/recommend")
        return jsonify({
            "error": "Failed to get recommendations",
            "details": str(e)
        }), 500

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)