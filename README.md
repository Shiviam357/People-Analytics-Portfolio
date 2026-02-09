# 🤖 AI-Powered Resume Parser & Candidate Scorer

## **Overview**
This project is a miniature Applicant Tracking System (ATS) designed to automate the initial screening of candidates. By leveraging Python for data extraction and Generative AI for rational interpretation, this tool reduces the manual "first-look" time for recruiters by approximately 70%.

## **Problem Statement**
In high-volume recruitment (US Staffing), recruiters spend hours scanning resumes that often don't match the Job Description. Standard keyword-based ATS tools often miss qualified candidates who use different terminology (e.g., "Python Developer" vs. "Backend Engineer").

## **The Solution**
A three-stage pipeline that:
1.  **Ingests:** Converts various file formats (.docx, .jpg) into clean text using OCR and conversion libraries.
2.  **Parses:** Uses Regular Expressions (Regex) to extract PII (Personally Identifiable Information) like Name, Email, and LinkedIn.
3.  **Interprets:** Uses an LLM (Gemini/OpenAI) to perform a **Semantic Match** between the candidate's profile and the Job Description.

## **Key Features**
* **File Normalization:** Automatic conversion of .docx and images to structured text.
* **Intelligent Scoring:** Scores candidates on a scale of 1-10 based on skills, domain, and experience.
* **Gap Analysis:** Generates a brief report on what skills the candidate is missing for a specific role.

## **Tech Stack**
* **Language:** Python 3.x
* **Extraction:** `pytesseract` (OCR), `docx2pdf`, `re` (Regex)
* **AI Engine:** Google Gemini API / OpenAI API
* **Environment:** Python-dotenv (for API key security)

## **How to Run**
1.  Place raw resumes in `/data/raw`.
2.  Add your Job Description to `job_description.txt`.
3.  Run `python main.py`.
4.  View results in `output/analysis.json`.

### 📂 Project Structure

- `data/raw/`: Store original PDF/Docx resumes here.
- `src/extractor.py`: Contains Regex logic to pull PII (Name, Email, Phone).
- `src/csv_manager.py`: Handles the conversion of extracted data into `candidates.csv`.
- `main.py`: The entry point that runs the full pipeline.
