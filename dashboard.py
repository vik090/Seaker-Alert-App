from flask import Flask, render_template, jsonify
from app.alerts import check_alerts
from app.database import get_last_n_records

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    return jsonify(check_alerts())

@app.route("/history")
def history():
    records = get_last_n_records(10)
    output = []
    for r in records:
        output.append({
            "timestamp": r.timestamp.strftime("%H:%M:%S"),
            "cpu": r.cpu,
            "ram": r.ram_used,
            "disk": r.disk_used
        })
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

