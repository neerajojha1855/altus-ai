import requests
import os
import json


HF_TOKEN = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/minimax-m3"

def grade_short_answer(student_answer, ideal_answer):
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}

    prompt = f"""
    You are a strict but fair teacher grading a short answer question.
    Ideal Answer: "{ideal_answer}"
    Student Answer: "{student_answer}"

    Score the student's answer from 0.0 to 1.0 based on how closely it matches the ideal answer.
    Provide a brief feedback sentence.

    Return JSON:
    {{"score": 0.8, "feedback": "Good understanding, but missing detail X."}}
    """

    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        result = response.json()[0]['generated_text']
        return json.loads(result)
    except Exception as e:
        return {"score": 0.0, "feedback": "Grading failed."}