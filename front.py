import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="🎬 Netflix AI Recommender", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = []

def get_recommendation(prompt):
    try:
        response = requests.post(
            f"{BACKEND_URL}/api/recommend",
            json={"prompt": prompt},
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Backend API Error: {str(e)}")
        return None
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
        return None

def main():
    st.title("🍿 AI Netflix Recommender")
    st.write("Describe what you want to watch and get recommendations!")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # User input
    if prompt := st.chat_input("What would you like to watch?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Display assistant response
        with st.chat_message("assistant"):
            try:
                with st.spinner("Finding recommendations..."):
                    response = get_recommendation(prompt)
                
                if response and "response" in response:
                    st.markdown(response["response"])
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response["response"]
                    })
                elif response and "error" in response:
                    st.error(response["error"])
            except Exception as e:
                st.error(f"Processing error: {str(e)}")

if __name__ == "__main__":
    main()