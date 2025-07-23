import psutil
import time

def get_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory()
    ram_used = round(ram.used / (1024 ** 3), 2)
    ram_total = round(ram.total / (1024 ** 3), 2)

    disk = psutil.disk_usage('/')
    disk_used = round(disk.used / (1024 ** 3), 2)
    disk_total = round(disk.total / (1024 ** 3), 2)

    uptime_seconds = time.time() - psutil.boot_time()
    uptime_hours = round(uptime_seconds / 3600, 2)

    # Optional: Try to read temperature
    try:
        temps = psutil.sensors_temperatures()
        temp = None
        if temps:
            for name, entries in temps.items():
                for entry in entries:
                    if entry.current:
                        temp = entry.current
                        break
                if temp:
                    break
    except Exception:
        temp = None

    return {
        "CPU (%)": cpu_percent,
        "RAM Used (GB)": ram_used,
        "RAM Total (GB)": ram_total,
        "Disk Used (GB)": disk_used,
        "Disk Total (GB)": disk_total,
        "Uptime (hours)": uptime_hours,
        "Temperature (°C)": temp if temp else "N/A"
    }

# Only run this when testing directly
if __name__ == "__main__":
    import pprint
    pprint.pprint(get_metrics())
