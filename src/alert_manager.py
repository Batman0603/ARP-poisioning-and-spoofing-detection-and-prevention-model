import os
from datetime import datetime
from config.settings import ALERT_LOG

def raise_alert(ip, old_mac, new_mac):
    message = (
        f"[ALERT] ARP Spoofing Detected!\n"
        f"IP Address: {ip}\n"
        f"Old MAC: {old_mac}\n"
        f"New MAC: {new_mac}\n"
        f"Time: {datetime.now()}\n\n"
    )

    print(message)

    log_dir = os.path.dirname(ALERT_LOG)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    with open(ALERT_LOG, "a") as f:
        f.write(message)

def log_info(message):
    timestamp = datetime.now()
    formatted_message = f"[*] {timestamp} - {message}"
    print(formatted_message)

    log_dir = os.path.dirname(ALERT_LOG)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    with open(ALERT_LOG, "a") as f:
        f.write(formatted_message + "\n")
