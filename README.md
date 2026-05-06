# PrivateGPT — Enterprise-Grade Private AI Assistant

![Banner](https://img.shields.io/badge/Enterprise-PrivateGPT-blueviolet?style=for-the-badge&logo=openai)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Neo4j](https://img.shields.io/badge/Neo4j-008CC1?style=for-the-badge&logo=neo4j&logoColor=white)

PrivateGPT is a robust, end-to-end RAG (Retrieval-Augmented Generation) platform designed for enterprise environments. It allows organisations to securely upload, index, and query their private documentation using advanced AI models (Gemini/Claude) while maintaining data sovereignty.

---

## 🚀 Key Features

- **🔐 Secure Authentication**: JWT-based auth with OTP email verification and role-based access control (RBAC).
- **📚 Advanced RAG Pipeline**: Hybrid retrieval combining vector search with Neo4j graph-based knowledge traversal.
- **📄 Multi-format Support**: Seamless processing of PDF, DOCX, and TXT files.
- **💬 Real-time Chat**: Streaming AI responses with precise citations [Document, Page, Section].
- **🖥️ Premium UI**: Modern, responsive dashboard built with React, TailwindCSS, and Framer Motion.
- **📊 Admin Dashboard**: Comprehensive user and document management for administrators.
- **🧠 Local-First Experience**: Session-persistent notebooks and local document previews.

---

## 🏗️ Project Structure

```text
private-gpt/
├── backend/            # FastAPI Application
│   ├── app/            # Core Logic (AI, API, DB, Workers)
│   ├── alembic/        # DB Migrations
│   ├── scripts/        # Utility Scripts
│   └── Dockerfile      # Production Container
├── frontend/           # Vite + React Application
│   ├── src/            # Components, Context, Hooks, Utils
│   └── public/         # Static Assets
└── docker-compose.yml  # Orchestration for Dev Environment
```

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python 3.12, FastAPI, SQLAlchemy, Alembic |
| **Frontend** | React 18, Vite, TailwindCSS, Framer Motion, Lucide |
| **Database** | PostgreSQL 16 (Relational), Neo4j 5 (Graph) |
| **Cache/Jobs** | Redis 7, Celery |
| **AI Models** | Google Gemini 2.5 Pro / AWS Bedrock (Claude 3.5) |
| **NLP** | spaCy (Concept & Keyword Extraction) |

---

## 🏁 Quick Start

### 1. Prerequisites
- **Docker & Docker Compose** installed.
- **Node.js 20+** (for local frontend development).
- **Python 3.12+** (optional, for local backend development).

### 2. Backend Setup (Docker)
```bash
cd backend
# Create your .env file (see backend/.env.example)
docker compose up --build -d

# Run migrations & download NLP models
docker compose run --rm api alembic upgrade head
docker compose run --rm api python -m spacy download en_core_web_sm
```
*Backend runs at `http://localhost:8000`*

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
*Frontend runs at `http://localhost:5173`*

---

## 🔐 Authentication & Testing

The system implements a strict security flow. However, for development and testing:

- **Master OTP Bypass**: Use the code `123456` to bypass email verification for any user.
- **Admin Access**: Users registered with `admin@regenesys.com` are automatically granted administrative privileges.
- **API Documentation**: Interactive Swagger docs are available at `http://localhost:8000/docs`.

---

## 🌍 Deployment

- **Backend**: Containerised for easy deployment to **Render**, **AWS ECS**, or **DigitalOcean**.
- **Frontend**: Optimized for **Vercel** or **Netlify**.

---

## 📄 License

Internal Project — BCA Intern Projects 5.
Developed by **Vishal Kuriya**.
