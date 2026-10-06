import streamlit as st
import ollama

st.set_page_config(page_title="AI Email Assistant")

st.title("📧 AI Email Assistant")
st.write("Generate professional email replies using AI")

recipient = "Bharath Kumar"
your_name = "Chaithrasri"

email = st.text_area(
    "Paste the email you received:",
    height=200
)

style = st.selectbox(
    "Choose reply style:",
    ["Professional", "Friendly", "Short"]
)

if st.button("Generate Reply"):

    if email.strip() == "":
        st.warning("Please paste an email first.")

    else:
        prompt = f"""
You are an AI Email Assistant.

Write a {style.lower()} reply to the following email.

Recipient name: {recipient}
Your name: {your_name}

Email received:
{email}

The reply must:
- Address the recipient as {recipient}
- End with "Best regards," followed by {your_name}
- Return only the complete reply email
- Do not give explanations
"""

        try:
            response = ollama.chat(
                model="llama3.2:latest",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            reply = response["message"]["content"]

            st.subheader("Generated Reply")

            st.text_area(
                "Your AI-generated reply:",
                value=reply,
                height=250
            )

        except Exception as e:
            st.error(f"Error: {e}")
