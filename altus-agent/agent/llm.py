import requests
import json
import os

HF_TOKEN = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/minimax-m3"

def generate_quiz(text, num_mcq=3, num_short=2):
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}

    prompt = f"""
    Based on the following text, generate a quiz with {num_mcq} multiple-choice questions and {num_short} short-answer questions.
    Return the output STRICTLY in JSON format matching this schema:
    {{
        "mcq": [
            {{"question": "...", "options": ["A", "B", "C", "D"], "correct_answer": "A"}}
        ],
        "short_answer": [
            {{"question": "...", "ideal_answer": "..."}}
        ]
    }}

    Text: {text}
    """

    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        result = response.json()[0]['generated_text']
        return json.loads(result)
    except Exception as e:
        return {"error": "Failed to parse LLM response"}