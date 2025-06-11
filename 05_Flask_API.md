
---

### `docs/05_Flask_API.md`

```markdown
# Flask API Setup

1️⃣ Install Python and create virtual environment:

```bash
sudo apt install python3-venv python3-pip -y
mkdir -p /opt/scripts
cd /opt/scripts
python3 -m venv venv
source venv/bin/activate
pip install flask

Create api_server.py:

from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(__name__)

def generate_mock_status():
    services = [
        "5G Base Stations",
        "Authentication Server",
        "Billing Platform",
        "Core Router",
        "Customer Self-Service",
        "DNS Servers",
        "Fiber Uplinks",
        "International Gateway"
    ]

    states = ["Operational", "Degraded", "Partial Outage", "Outage", "Maintenance"]

    status_report = {"services": {}}

    for service in services:
        status_report["services"][service] = random.choice(states)

    status_report["timestamp"] = datetime.utcnow().isoformat()
    return status_report

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify(generate_mock_status())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

Create systemd service:

sudo nano /etc/systemd/system/optus-api.service


[Unit]
Description=Optus Network API Flask App
After=network.target

[Service]
User=azureuser
WorkingDirectory=/opt/scripts
ExecStart=/opt/scripts/venv/bin/python3 /opt/scripts/api_server.py
Restart=always

[Install]
WantedBy=multi-user.target


Reload services:

sudo systemctl daemon-reload
sudo systemctl enable optus-api
sudo systemctl start optus-api
