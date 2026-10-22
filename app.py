import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Powered Study Assistant",
    page_icon="🎓"
)

st.title("🎓 AI Powered Study Assistant")
st.write("Ask questions and learn in simple English!")

# Read API key from Streamlit Secrets
try:
    api_key = st.secrets["AQ.Ab8RN6I124Z5Hm9gDVVI89AeJIYO4woBE1mOHhRc_iEH9oL90Q"]
    client = genai.Client(api_key=api_key)
except Exception:
    st.error("Please configure GEMINI_API_KEY in Streamlit Secrets.")
    st.stop()


def study_assistant(user_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_prompt
    )
    return response.text


user_question = st.text_area(
    "Enter your question",
    placeholder="Explain Generative AI in simple terms"
)

if st.button("Get Answer"):
    if user_question.strip():
        try:
            with st.spinner("Generating answer..."):
                result = study_assistant(user_question)

            st.subheader("Answer")
            st.write(result)

        except Exception as e:
            st.error(f"Unable to generate answer: {e}")
    else:
        st.warning("Please enter a question.")
