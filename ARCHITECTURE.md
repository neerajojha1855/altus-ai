# Architecture: Altus AI

## System Overview
Altus AI utilizes a modern decoupled architecture with a reactive frontend and a lightweight, AI-integrated backend microservice.

## Tech Stack

### Frontend (Client-Side)
- **Framework:** HTML, JavaScript
- **Styling:** Tailwind CSS for rapid, consistent, modern UI design

### Backend (API & Business Logic)
- **Framework:** Python / Flask
- **AI Integration:** Minimax-M3 ( via HuggingFace).

### Data Layer
- **Primary Database:** PostgreSQL (Structured academic data: Schools -> Teachers -> Classes -> Students -> Grades)
- **Database Hosting:** Neon (Serverless)

### Authentication & Storage
- **Identity Provider:** Firebase Authentication (Role-based: Teacher, Student, Admin)
- **Object Storage:** Cloudinary Storage (for PDFs and documents)

### Infrastructure & Deployment
- **Hosting Platform:** Render
- **Future Scalability:** Docker containerization deployed on Google Cloud Run or AWS ECS.

## High-Level Data Flow
1. **User Action:** Teacher uploads a PDF via the React Frontend.
2. **API Request:** Frontend sends PDF to Flask Backend.
3. **Storage:** Backend saves PDF to Object Storage (Firebase/S3).
4. **AI Processing:** Backend extracts text and calls LLM (Nemotron, Minimax-m3, or Gemma) to generate quiz JSON.
5. **Database:** Quiz structure saved to PostgreSQL.
6. **Response:** Backend returns Quiz ID to Frontend, making it available for Students.
