import streamlit as st
import pdfplumber

# Page Title
st.title("AI Resume Analyzer")

# PDF Upload
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

# If a file is uploaded
if uploaded_file is not None:

    try:
        all_text = ""

        # Open PDF
        with pdfplumber.open(uploaded_file) as pdf:

            # Loop through all pages
            for page in pdf.pages:

                page_text = page.extract_text()

                # Skip empty pages
                if page_text:
                    all_text += page_text + "\n\n"

        # Check if any text was extracted
        if all_text.strip():

            st.success("Resume uploaded successfully!")

            st.subheader("Extracted Resume Text")

            st.text_area(
                "Preview",
                all_text,
                height=400
            )

        else:
            st.warning("No readable text found in this PDF.")

    except Exception as e:
        st.error(f"Error reading PDF: {e}")