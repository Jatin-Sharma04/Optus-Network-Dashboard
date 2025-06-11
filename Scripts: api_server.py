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
