import streamlit as st
import pdfplumber
import google.generativeai as genai

# Load Gemini API Key
with open("gemini_key.txt", "r") as file:
    api_key = file.read().strip()

# Configure Gemini
genai.configure(api_key=api_key)

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Title
st.title("AI Resume Analyzer")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    resume_text = ""

    # Extract text from all pages
    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                resume_text += page_text + "\n"

    # Show extracted text
    st.subheader("Resume Preview")

    st.text_area(
        "Extracted Text",
        resume_text,
        height=300
    )

    # Analyze button
    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            response = model.generate_content(
                f"""
                Analyze this resume.

                Return the response EXACTLY in this format:

                ATS Score:
                <score>

                Strengths:
                - point 1
                - point 2

                Weaknesses:
                - point 1
                - point 2

                Suggestions:
                - point 1
                - point 2

                Resume:
                {resume_text}
                """
            )

            analysis = response.text

        st.subheader("AI Analysis")

        try:

            sections = analysis.split("Strengths:")

            score_part = sections[0]

            remaining = sections[1]

            strengths_part = remaining.split("Weaknesses:")[0]

            remaining = remaining.split("Weaknesses:")[1]

            weaknesses_part = remaining.split("Suggestions:")[0]

            suggestions_part = remaining.split("Suggestions:")[1]

            score = score_part.replace("ATS Score:", "").strip()

            st.metric("ATS Score", score)

            st.success("Strengths")
            st.write(strengths_part)

            st.warning("Weaknesses")
            st.write(weaknesses_part)

            st.info("Suggestions")
            st.write(suggestions_part)

        except:

            st.write(analysis)