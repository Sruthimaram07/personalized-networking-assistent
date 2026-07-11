import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤝"
)

st.title("🤝 Personalized Networking Assistant")

event = st.text_input("Enter Event")
interest = st.text_input("Enter Interest")

if st.button("Generate Conversation"):

    if not event or not interest:
        st.warning("Please enter both Event and Interest.")
    else:
        response = requests.post(
            f"{API_URL}/generate",
            json={
                "event": event,
                "interest": interest
            }
        )

        if response.status_code == 200:
            data = response.json()

            st.subheader("Keywords")
            st.write(data["keywords"])

            st.subheader("Conversation Starter")
            st.success(data["conversation_starter"])

            st.subheader("Fact Check")

            topic = event

            fact_response = requests.get(
                f"{API_URL}/fact-check/{topic}"
            )

            if fact_response.status_code == 200:
                fact = fact_response.json()
                st.info(fact["summary"])

        else:
            st.error("Failed to generate conversation.")