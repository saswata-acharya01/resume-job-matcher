KNOWN_SKILLS = {
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "pandas",
    "spark"
}

import ollama
import json
import re
def extract_skills(text):
    prompt=f"""
From the text below, identify any technical skills mentioned.

TEXT:
{text}
"""
    response=ollama.generate(
    model="tinyllama",
    prompt=prompt,
    stream=False
    )

    raw_output=response["response"].lower()
    print("\nRAW MODEL OUTPUT:")
    print(raw_output)
    found_skills=set()
    for skill in KNOWN_SKILLS:
        if skill in raw_output:
            found_skills.add(skill.title())
    return found_skills
resume_text = """
Data Scientist with experience in Python, SQL, Machine Learning and Pandas.
"""

job_description_text = """
We are looking for a Data Scientist skilled in Python, SQL, Deep Learning and Spark.
"""
resume_skills = extract_skills(resume_text)
job_skills = extract_skills(job_description_text)

matched_skills = resume_skills.intersection(job_skills)
missing_skills = job_skills - resume_skills

print("RESUME SKILLS:", resume_skills)
print("JOB SKILLS:", job_skills)
print("MATCHED SKILLS:", matched_skills)
print("MISSING SKILLS:", missing_skills)