# GenAI Resume–Job Skill Matcher (Local LLM)

## 🔍 Problem Statement
Recruiters and applicants often struggle to identify skill gaps between resumes and job descriptions.
This project uses Generative AI to automatically extract and compare skills from both sources.

## 💡 Solution
A **local GenAI-powered system** that:
- Extracts skills from resume text
- Extracts required skills from job descriptions
- Identifies matched and missing skills

Designed to work **entirely offline** using lightweight local LLMs.

## 🧠 Key Design Choices
- Used a **local LLM (TinyLLaMA via Ollama)** to avoid API costs
- Implemented a **hybrid approach**:
  - LLM for semantic understanding
  - Deterministic Python logic for reliability
- Designed around **hardware memory constraints**

## 🛠 Tech Stack
- Python
- Ollama
- TinyLLaMA
- Regex & Set-based logic

## ⚙️ How It Works
1. Resume and job text are processed by a local LLM
2. Known technical skills are identified from LLM output
3. Skills are compared using set operations

## 📊 Example Output
RESUME SKILLS: Python, SQL, Machine Learning, Pandas
JOB SKILLS: Python, SQL, Deep Learning, Spark
MATCHED SKILLS: Python, SQL
MISSING SKILLS: Deep Learning, Spark

## 🚀 Future Improvements
- Skill similarity mapping (ML ↔ Deep Learning)
- Match percentage scoring
- Streamlit web interface
- Configurable skill taxonomy