import psutil
import time
import os
from datetime import datetime

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    boot_time = datetime.fromtimestamp(psutil.boot_time())

    return {
        'cpu_usage': cpu_usage,
        'memory_total': memory_info.total / (1024 ** 3),  # GB
        'memory_used': memory_info.used / (1024 ** 3),    # GB
        'disk_total': disk_info.total / (1024 ** 3),      # GB
        'disk_used': disk_info.used / (1024 ** 3),        # GB
        'boot_time': boot_time.strftime("%Y-%m-%d %H:%M:%S")
    }

def display_system_info(info):
    clear_console()
    print("MaxStation - Real-Time System Monitoring")
    print(f"CPU Usage: {info['cpu_usage']}%")
    print(f"Memory Used: {info['memory_used']:.2f} GB / {info['memory_total']:.2f} GB")
    print(f"Disk Used: {info['disk_used']:.2f} GB / {info['disk_total']:.2f} GB")
    print(f"System Boot Time: {info['boot_time']}")

def main():
    try:
        while True:
            system_info = get_system_info()
            display_system_info(system_info)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting MaxStation. Goodbye!")

if __name__ == "__main__":
    main()