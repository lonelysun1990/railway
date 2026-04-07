// API URL - set via environment variable in production
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

window.ping = async function() {
  const box = document.getElementById("response");
  box.style.display = "block";
  box.textContent = "Loading...";
  try {
    const res = await fetch(`${API_URL}/api/hello`);
    const data = await res.json();
    box.textContent = JSON.stringify(data, null, 2);
  } catch (e) {
    box.textContent = "Error: " + e.message;
  }
}
