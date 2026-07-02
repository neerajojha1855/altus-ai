import os
import requests

RESEDN_API_KEY = os.getenv("RESEND_API_KEY")

def send_remainder_email(student_email, student_name, assignment_title):
    headers = {
        "Authorization": f"Bearer {RESEDN_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "from": "Altus AI <noreply@altusai.com>",
        "to": [student_email],
        "subject": f"Remaider: {assignment_title} is pending",
        "html": f"<p>Hi {student_name},</p><p>Please complete your assignment: <strong>{assignment_title}</strong>.</p>"
    }

    requests.post("https://api.resend.com/emails", headers=headers, json=payload)