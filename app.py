# easy-7-internal-endpoint/app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

@app.route("/")
def index():
    return """
<h2>Status Service</h2>
<p>Public system health endpoint.</p>
<ul>
<li>GET /internal/health</li>
<li>GET /health</li>
</ul>
"""

@app.route("/health")
def health():
    return "ok"

@app.route("/internal/health")
def internal():
    return jsonify({"db":"ok","cache":"ok","flag":FLAG})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
