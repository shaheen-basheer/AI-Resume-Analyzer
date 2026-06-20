import streamlit as st
import pdfplumber
import google.generativeai as genai

# Configure Gemini

with open("gemini_key.txt", "r") as file:
    api_key = file.read().strip()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    resume_text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                resume_text += page_text + "\n"

    st.subheader("Resume Preview")

    st.text_area(
        "Extracted Text",
        resume_text,
        height=300
    )

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            response = model.generate_content(
                f"""
                Analyze this resume.

                Give:

                ATS Score (0-100)

                Strengths

                Weaknesses

                Suggestions

                Resume:
                {resume_text}
                """
            )

        st.subheader("AI Analysis")

        st.write(response.text)