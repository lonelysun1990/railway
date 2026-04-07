# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally with auto-reload
uvicorn main:app --reload

# Run on a specific port
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Architecture

Single-file FastAPI app (`main.py`) with no external templates or static assets:

- `GET /` — serves a self-contained HTML page (inline in `HTML` string) with a dark UI and a "Ping API" button
- `GET /api/hello` — returns `{"message": "Hello from Railway!", "status": "ok"}`

The HTML/CSS/JS is embedded directly in `main.py` as a module-level string constant and returned via `HTMLResponse`. No Jinja2, no `static/` directory.

## Railway Deployment

`railway.toml` sets the start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`. Railway injects `PORT` at runtime; `main.py` reads it via `os.environ.get("PORT", 8000)`.
