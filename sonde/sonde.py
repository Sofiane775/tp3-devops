import time, json, socket
import psutil
from datetime import datetime
import paho.mqtt.publish as publish

while True:
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "cpu_temp": 50.0,
        "cpu_load": psutil.cpu_percent(),
        "memory_used_percent": psutil.virtual_memory().percent,
        "disk_used_percent": psutil.disk_usage('/').percent,
        "host": socket.gethostname()
    }
    publish.single("system/host_params_to_server", json.dumps(data), hostname="localhost")
    time.sleep(1)
