# Product Requirements Document (PRD): Altus AI

## 1. Overview
**Altus AI** is a smart classroom assistant designed to eliminate the heavy lifting of daily academic tasks for teachers, allowing them to focus on student mentorship and personalized instruction.

## 2. Problem Statement
Teachers face an overwhelming administrative burden (drafting assignments, distributing/collecting paper submissions, manual grading). This leads to burnout and reduces time for actual teaching. 

## 3. Target Audience
- **Primary:** Teachers (K-12 and Higher Ed)
- **Secondary:** Students (completing assignments)
- **Tertiary:** School Administrators (monitoring usage and broad metrics)

## 4. Key Features & Requirements

### 4.1 Magic Curriculum-to-Quiz
- **Input Methods:** Upload PDF, Paste Text, Link Webpage.
- **Processing:** Parse material using high-performance, cost-effective LLMs (e.g., Nemotron, Minimax-m3, or Gemma) to generate age-appropriate quizzes.
- **Output:** Interactive multiple-choice and short-answer quizzes.
- **Requirement:** Generation must take less than 15 seconds.

### 4.2 Instant Auto-Grading & Analytics
- **Student Interface:** Web-based portal to complete generated quizzes.
- **Auto-Grading:** Immediate evaluation of multiple-choice and AI-assisted evaluation of short answers.
- **Analytics:** Automatic population of teacher gradebooks. Immediate feedback to students.

### 4.3 Smart Submission Tracking
- **Dashboard:** Unified view of student submissions per assignment.
- **Reminders:** One-click automated reminders to students and parents for missing assignments.

## 5. Success Metrics
- Average time saved per teacher (Target: 10-15 hours/week).
- Quiz generation latency.
- Teacher retention and daily active usage.