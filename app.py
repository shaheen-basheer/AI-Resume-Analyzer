import streamlit as st
import pdfplumber
import google.generativeai as genai
import re

from database import save_analysis
from database import get_history


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

# Job Description Input
job_description = st.text_area(
    "Paste Job Description (Optional)",
    height=200
)

if uploaded_file is not None:

    resume_text = ""

    # Extract text from all pages
    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                resume_text += page_text + "\n"

    # Resume Preview
    st.subheader("Resume Preview")

    st.text_area(
        "Extracted Text",
        resume_text,
        height=300
    )

    # Analyze Button
    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            response = model.generate_content(
                f"""
                You are an ATS Resume Analyzer.

                Analyze the resume against the provided Job Description.

                Return EXACTLY in this format:

                ATS Score:
                <score>

                Strengths:
                - point 1
                - point 2

                Weaknesses:
                - point 1
                - point 2

                Missing Skills:
                - skill 1
                - skill 2

                Suggestions:
                - point 1
                - point 2

                Job Description:
                {job_description}

                Resume:
                {resume_text}
                """
            )

            analysis = response.text

        st.subheader("AI Analysis")

        try:

            score = analysis.split("ATS Score:")[1].split("Strengths:")[0].strip()

            strengths = analysis.split("Strengths:")[1].split("Weaknesses:")[0].strip()

            weaknesses = analysis.split("Weaknesses:")[1].split("Missing Skills:")[0].strip()

            missing_skills = analysis.split("Missing Skills:")[1].split("Suggestions:")[0].strip()

            suggestions = analysis.split("Suggestions:")[1].strip()

            # Save to Database
            save_analysis(
                uploaded_file.name,
                score,
                analysis
            )

            # ATS Score Card
            st.metric("ATS Score", score)

            # Progress Bar
            try:

                match = re.search(r"\d+", score)

                if match:

                    numeric_score = int(match.group())

                    st.progress(numeric_score / 100)

            except:

                pass

            # Strengths
            st.success("Strengths")
            st.write(strengths)

            # Weaknesses
            st.warning("Weaknesses")
            st.write(weaknesses)

            # Missing Skills
            st.error("Missing Skills")

            skills = missing_skills.split("-")

            for skill in skills:

                skill = skill.strip()

                if skill:

                    st.markdown(
                        f"""
                        <span style="
                        background-color:#ff4b4b;
                        color:white;
                        padding:6px 12px;
                        border-radius:12px;
                        margin:4px;
                        display:inline-block;">
                        {skill}
                        </span>
                        """,
                        unsafe_allow_html=True
                    )

            # Suggestions
            st.info("Suggestions")
            st.write(suggestions)

            # Download Button
            st.download_button(
                label="Download Analysis",
                data=analysis,
                file_name="resume_analysis.txt",
                mime="text/plain"
            )

        except:

            st.write(analysis)

# History Section
st.divider()

st.subheader("Analysis History")

history = get_history()

if history:

    for row in history:

        st.write(
            f"📄 {row[0]} | ATS Score: {row[1]} | {row[2]}"
        )

else:

    st.write("No analysis history yet.")