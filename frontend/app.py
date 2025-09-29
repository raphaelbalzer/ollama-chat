import streamlit as st
import requests
import os

# Backend-URL aus Umgebungsvariable oder Default
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.title("Ollama Chat App 🦙")

# Modell-Auswahl
model = st.selectbox("Wähle ein Modell:", ["gemma3:4b", "gemma3:1b"])

# Prompt-Eingabe
prompt = st.text_area("Deine Nachricht:", "")

if st.button("Absenden"):
    if prompt.strip():
        with st.spinner("Frage Ollama..."):
            res = requests.post(
                f"{BACKEND_URL}/chat",
                json={"model": model, "message": prompt},
            )
            if res.status_code == 200:
                st.markdown("### Antwort")
                st.write(res.json()["response"])
            else:
                print(res)
                st.error("Fehler beim Anfragen des Backends")
