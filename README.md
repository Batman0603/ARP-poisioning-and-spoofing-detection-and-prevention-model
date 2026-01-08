# ARP Spoof Detection

A lightweight Python tool designed to detect ARP spoofing (Man-in-the-Middle) attacks on a local network by monitoring ARP traffic and validating IP-to-MAC mappings.

## Project Structure

```
arp-spoof-detection/
│
├── README.md                 # Project overview & usage
├── requirements.txt          # Python dependencies
├── src/
│   ├── main.py               # Entry point
│   ├── arp_sniffer.py        # Capture ARP packets
│   ├── arp_detector.py       # Detection logic
│   ├── alert_manager.py      # Alerts & logging
├── logs/
│   └── alerts.log            # Security alerts
├── config/
│   └── settings.py           # Config values
└── docs/
    ├── architecture.md       # Architecture explanation
    └── workflow.md           # Project workflow
```

## Prerequisites

- Python 3.x
- Root/Administrator privileges (required for packet sniffing)

## Installation

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure the application in `config/settings.py` (ensure you set your Interface, Gateway IP, and Gateway MAC).

## Usage

Run the tool with root privileges to enable packet sniffing:

```bash
sudo python3 src/main.py
```

## Features

- **Real-time Monitoring**: Continuously sniffs ARP packets on the specified interface.
- **Spoof Detection**: Compares incoming ARP replies against a known table of trusted MAC addresses.
- **Logging**: Records alerts and network discovery events to `logs/alerts.log`.