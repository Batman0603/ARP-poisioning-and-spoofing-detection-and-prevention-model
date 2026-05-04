# 🛡️ ARP Spoof Detection

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Unix-green?style=for-the-badge&logo=linux)
![Security](https://img.shields.io/badge/Security-Network%20Monitoring-red?style=for-the-badge&logo=shield)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

### 🔍 Lightweight ARP Spoofing Detection Tool  
Detect **ARP spoofing / Man-in-the-Middle (MITM)** attacks in real time by monitoring ARP traffic and validating IP-to-MAC mappings on your local network.

</div>

---

## ✨ Features

- ⚡ **Real-time Monitoring**  
  Continuously captures and analyzes ARP packets on the selected network interface.

- 🛡️ **ARP Spoof Detection**  
  Detects suspicious ARP replies by comparing them against trusted IP-to-MAC mappings.

- 📝 **Alert Logging**  
  Logs spoofing alerts and network discovery events into `logs/alerts.log`.

- 🔧 **Configurable Settings**  
  Easily customize interface, gateway IP, and trusted MAC addresses.

- 📂 **Clean Modular Architecture**  
  Organized project structure for easy maintenance and scalability.

---

# 📁 Project Structure

```bash
arp-spoof-detection/
│
├── README.md                 # Project overview & usage
├── requirements.txt          # Python dependencies
├── src/
│   ├── main.py               # Entry point
│   ├── arp_sniffer.py        # Capture ARP packets
│   ├── arp_detector.py       # Detection logic
│   ├── alert_manager.py      # Alerts & logging
│
├── logs/
│   └── alerts.log            # Security alerts
│
├── config/
│   └── settings.py           # Config values
│
└── docs/
    ├── architecture.md       # Architecture explanation
    └── workflow.md           # Project workflow
```

---

# ⚙️ Prerequisites

Before running the project, ensure you have:

- 🐍 Python 3.x installed
- 🔐 Root/Administrator privileges  
  *(Required for packet sniffing and ARP monitoring)*

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/arp-spoof-detection.git
cd arp-spoof-detection
```

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ Configure Settings

Update the configuration inside:

```bash
config/settings.py
```

Make sure to set:

- Network Interface
- Gateway IP Address
- Trusted Gateway MAC Address

---

# ▶️ Usage

Run the application with root privileges:

```bash
sudo python3 src/main.py
```

---

# 🔍 How It Works

```text
ARP Packet Capture
        ↓
Analyze ARP Replies
        ↓
Validate IP ↔ MAC Mapping
        ↓
Detect Suspicious Changes
        ↓
Generate Security Alert
```

---

# 📜 Logging

All alerts and suspicious activities are recorded in:

```bash
logs/alerts.log
```

Example alert:

```text
[ALERT] Possible ARP Spoofing Detected!
IP: 192.168.1.1
Expected MAC: AA:BB:CC:DD:EE:FF
Detected MAC: 11:22:33:44:55:66
```

---

# 🧠 Detection Strategy

The detector works by:

- Maintaining a trusted mapping table of IP ↔ MAC addresses
- Monitoring ARP reply packets in real time
- Comparing incoming ARP responses against known trusted mappings
- Triggering alerts whenever inconsistencies are detected

---

# 📚 Documentation

Additional project documentation can be found in:

- `docs/architecture.md`
- `docs/workflow.md`

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Scapy / Socket Libraries | Packet sniffing & ARP analysis |
| Logging Module | Alert management |

---

# ⚠️ Disclaimer

This project is intended for:

- Educational purposes
- Security research
- Authorized network monitoring only

Do **not** use this tool on networks without permission.

---

# 🤝 Contributing

Contributions, improvements, and feature suggestions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🛡️ Share it with others interested in cybersecurity

---

<div align="center">

### 🔐 Stay Secure • Monitor Smart • Detect Early

</div>
