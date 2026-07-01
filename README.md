# Altus AI - Rescuing the Educator's Time

Altus AI is an AI-powered smart classroom assistant designed to reduce the administrative burden on teachers by automating assignment generation, grading, and submission tracking.

## Features

- **Magic Curriculum-to-Quiz:** Generate interactive quizzes from PDFs, text, or web links instantly using LLMs.
- **Instant Auto-Grading:** Provide immediate feedback to students and auto-populate gradebooks.
- **Smart Submission Tracking:** Dashboard to track missing work and send one-click reminders.

## Tech Stack

- **Frontend:** React, Tailwind CSS, Zustand
- **Backend:** Python, Flask, Minimax-M3 (via Hugging Face)
- **Database:** PostgreSQL (Neon)
- **Auth & Storage:** Firebase Authentication and Cloudinary Storage
- **Hosting:** Render

## Project Structure

```
altus-ai/
├── frontend/        # React + Next.js UI (Teacher & Student dashboards)
├── backend/         # Flask REST API, DB models, Auth middleware
├── altus-agent/     # AI/LLM microservice (quiz generation, auto-grading)
├── PRD.md           # Product Requirements Document
├── ARCHITECTURE.md  # System design and tech stack details
└── README.md
```

## Getting Started
*(Instructions for local setup will be added as the codebase is initialized)*
