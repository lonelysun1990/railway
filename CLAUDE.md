# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Structure

This is a monorepo with separate frontend and backend services:

```
railway/
├── frontend/          # Vite + vanilla JS frontend
│   ├── index.html
│   ├── main.js
│   ├── style.css
│   ├── package.json
│   ├── vite.config.js
│   └── railway.toml
├── backend/           # FastAPI backend
│   ├── main.py
│   ├── requirements.txt
│   └── railway.toml
└── CLAUDE.md
```

## Commands

### Backend

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Run locally with auto-reload
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend

```bash
cd frontend

# Install dependencies
npm install

# Run dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Architecture

- **Backend**: FastAPI app with CORS configured. Serves `/api/hello` and `/api/health` endpoints.
- **Frontend**: Vite-powered vanilla JS app. Uses `VITE_API_URL` env var to connect to backend.

## Railway Deployment

Each folder has its own `railway.toml`. On Railway, create two services:
1. Backend service with root directory set to `backend/`
2. Frontend service with root directory set to `frontend/`

Set environment variables:
- Backend: `FRONTEND_URL` = frontend's Railway URL (for CORS)
- Frontend: `VITE_API_URL` = backend's Railway URL (for API calls)
