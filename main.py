import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Railway App</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #0f0f0f;
      color: #f0f0f0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .card {
      background: #1a1a1a;
      border: 1px solid #2e2e2e;
      border-radius: 12px;
      padding: 2.5rem 3rem;
      max-width: 480px;
      width: 90%;
      text-align: center;
      box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #1c3a2a;
      color: #4ade80;
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 1.5rem;
    }

    .badge::before {
      content: "";
      width: 7px;
      height: 7px;
      background: #4ade80;
      border-radius: 50%;
      animation: pulse 1.8s infinite;
    }

    @keyframes pulse {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.3; }
    }

    h1 {
      font-size: 1.9rem;
      font-weight: 700;
      margin-bottom: 0.6rem;
      letter-spacing: -0.02em;
    }

    p.sub {
      color: #888;
      font-size: 0.95rem;
      margin-bottom: 2rem;
      line-height: 1.5;
    }

    button {
      background: #7c3aed;
      color: #fff;
      border: none;
      border-radius: 8px;
      padding: 0.65rem 1.5rem;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.15s;
    }

    button:hover { background: #6d28d9; }
    button:active { background: #5b21b6; }

    #response {
      margin-top: 1.5rem;
      background: #111;
      border: 1px solid #2e2e2e;
      border-radius: 8px;
      padding: 0.9rem 1.1rem;
      font-family: "SF Mono", "Fira Code", monospace;
      font-size: 0.82rem;
      color: #a3e635;
      text-align: left;
      display: none;
      white-space: pre;
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="badge">Deployed on Railway</div>
    <h1>Hello, Railway!</h1>
    <p class="sub">This app is running on Railway.com.<br>Click below to ping the API.</p>
    <button onclick="ping()">Ping API</button>
    <div id="response"></div>
  </div>

  <script>
    async function ping() {
      const box = document.getElementById("response");
      box.style.display = "block";
      box.textContent = "Loading...";
      try {
        const res = await fetch("/api/hello");
        const data = await res.json();
        box.textContent = JSON.stringify(data, null, 2);
      } catch (e) {
        box.textContent = "Error: " + e.message;
      }
    }
  </script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
async def index():
    return HTML


@app.get("/api/hello")
async def hello():
    return {"message": "Hello from Railway!", "status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
