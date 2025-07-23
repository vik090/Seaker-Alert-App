  README FILE

````markdown
# 🚨 Seaker-Alert-App

A real-time system metrics monitoring and alert dashboard built using Python, Flask, SQLite, and Docker.

---

## 🖥️ Features

- ✅ Live system monitoring:
  - CPU usage
  - RAM usage
  - Disk usage
  - System uptime
  - Temperature (optional)

- ✅ Customizable alert thresholds
- ✅ On-screen alerts when values exceed limits
- ✅ Historical metrics saved in SQLite
- ✅ Web dashboard with live and historical data
- ✅ Dockerized for easy deployment

---

## 🚀 Quick Start

### ✅ Option 1: Run with Docker

> Requires Docker installed

```bash
# Build the image
docker build -t seaker-alert-app .

# Run the app
docker run -p 5000:5000 seaker-alert-app
````

Or use Docker Compose:

```bash
docker-compose up --build
```

📍 Then open in browser: [http://localhost:5000](http://localhost:5000)

---

### 🐍 Option 2: Run Locally (Python)

> Requires Python 3.x installed

```bash
pip install -r requirements.txt
python dashboard.py
```

---

## ⚙️ Alert Configuration

Change the alert thresholds in:

```json
app/config.json
```

Example:

```json
{
  "cpu_threshold": 75,
  "ram_threshold": 80,
  "disk_threshold": 90
}
```

---

## 🌐 Routes

| Route      | Description                   |
| ---------- | ----------------------------- |
| `/`        | Web dashboard (HTML)          |
| `/metrics` | Returns live metrics & alerts |
| `/history` | Shows last 10 records (JSON)  |

---

## 📁 Project Structure

```
Seaker-Alert-App/
├── app/
│   ├── alerts.py
│   ├── config.json
│   ├── database.py
│   └── metrics.py
├── templates/
│   └── index.html
├── dashboard.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── block_diagram.png
└── metrics.db
```

---

## 🛠 Built With

* Python 3.10
* Flask
* psutil
* SQLAlchemy (SQLite)
* Docker

---

## 📊 Live Demo

> 🟢 Running Demo (If Deployed)

🔗 [https://seaker-alert-app-demo.vercel.app](https://seaker-alert-app-demo.vercel.app)
*(Replace this with your actual deployment link if hosted)*

---

## 👨‍💼 Candidate Details

* **Name:** Vikram Reddy
* **Role Applied:** Jr. IoT Engineer
* **Date:** July 2025
* **GitHub:** [https://github.com/vik090](https://github.com/vik090)

---

## 📷 Block Diagram

Below is the block diagram for data flow in the app:
![](block_diagram.png)

```
System
  ↓
metrics.py → alerts.py → database.py
  ↓                   ↓
dashboard.py → /metrics & /history → index.html
```

---

## 📩 Submission Checklist

* ✅ GitHub repo with source code and Dockerfile
* ✅ README with clear setup and usage
* ✅ Metrics + Alert + Historical data functional
* ✅ Docker + SQLite working
* ✅ Block diagram included
* ✅ Ready for live interview demo
