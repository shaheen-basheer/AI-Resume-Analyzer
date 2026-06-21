# AI Resume Analyzer

An AI-powered Resume Analyzer built using Python, Streamlit, Gemini AI, PDFPlumber, and SQLite.

The application allows users to upload resumes, extract text from PDFs, analyze resumes using AI, compare resumes with job descriptions, identify missing skills, and store previous analyses in a database.

---

## Features

### Resume Upload

* Upload PDF resumes
* Supports multi-page PDFs
* Extracts resume text automatically

### AI Resume Analysis

* ATS Score generation
* Resume strengths analysis
* Resume weaknesses analysis
* Improvement suggestions

### Job Description Matching

* Compare resume against a specific job description
* Detect missing skills
* Generate ATS compatibility score

### Database Integration

* Stores previous resume analyses
* Analysis history tracking using SQLite

### Download Reports

* Download AI feedback as a text report

---

## Technologies Used

* Python
* Streamlit
* Google Gemini AI
* PDFPlumber
* SQLite
* Git & GitHub

---

## Project Structure

AI_resume_analyzer/

├── app.py

├── database.py

├── requirements.txt

├── resume_analysis.db

├── screenshots/

└── README.md

---

## Screenshots

### Home Page

![Home](screenshots/home.png)

### Resume Upload

![Upload](screenshots/upload.png)

### AI Analysis

![Analysis 1](screenshots/analysis1.png)
![Analysis 2](screenshots/analysisimage2.png)
![Analysis 3](screenshots/analysisimage3.png)

### Analysis History

![History](screenshots/history.png)

---

## Installation

Clone the repository:

git clone https://github.com/shaheen-basheer/AI-Resume-Analyzer.git

Navigate to project folder:

cd AI-Resume-Analyzer

Create virtual environment:

python -m venv venv

Activate environment:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run application:

streamlit run app.py

---

## Future Improvements

* Resume ranking
* Multiple resume comparison
* PDF report generation
* Recruiter dashboard
* Cloud deployment

---

## Author

Shaheen P

Government Model Engineering College

Electronics and Communication Engineering
