import json
from app.metrics import get_metrics
from app.database import save_metrics

def load_thresholds():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading config.json: {e}")
        return {
            "cpu_threshold": 75,
            "ram_threshold": 80,
            "disk_threshold": 90
        }

def check_alerts():
    thresholds = load_thresholds()
    data = get_metrics()
    alerts = []

    # Check CPU threshold
    if data["CPU (%)"] > thresholds["cpu_threshold"]:
        alerts.append(f"⚠️ High CPU Usage: {data['CPU (%)']}%")

    # Check RAM threshold
    ram_percent = (data["RAM Used (GB)"] / data["RAM Total (GB)"]) * 100
    if ram_percent > thresholds["ram_threshold"]:
        alerts.append(f"⚠️ High RAM Usage: {data['RAM Used (GB)']} GB ({round(ram_percent, 1)}%)")

    # Check Disk threshold
    disk_percent = (data["Disk Used (GB)"] / data["Disk Total (GB)"]) * 100
    if disk_percent > thresholds["disk_threshold"]:
        alerts.append(f"⚠️ Low Disk Space: {data['Disk Used (GB)']} GB ({round(disk_percent, 1)}%)")

    # Save metrics to DB
    save_metrics(data)

    # Return both metrics and any alerts
    return {
        "metrics": data,
        "alerts": alerts
    }

