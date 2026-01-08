# Application Workflow

This document outlines the operational workflow of the ARP Spoof Detection tool from startup to termination.

## 1. Initialization
- The user executes `src/main.py`.
- The system imports configuration settings from `config/settings.py`.
- The `arp_table` is initialized with the Gateway IP and MAC address to prevent immediate false positives or spoofing of the gateway.

## 2. Sniffing Phase
- `start_sniffing()` is called with the specified network interface.
- Scapy begins listening for packets matching the `arp` filter.
- The system enters a blocking loop, processing packets as they arrive.

## 3. Detection Logic (Per Packet)
When a packet is captured, the `detect_arp_spoof(packet)` function is triggered:

1.  **Validation**: Checks if the packet contains an ARP layer and is an ARP Reply (Opcode 2).
2.  **Extraction**: Extracts the Sender IP (`psrc`) and Sender MAC (`hwsrc`).
3.  **Comparison**:
    *   **Case A: IP is in `arp_table`**
        *   Compare the stored MAC with the packet's MAC.
        *   **If Different**: ARP Spoofing detected. Call `raise_alert()`.
        *   **If Same**: Valid traffic. Print visual feedback ("Scanning...").
    *   **Case B: IP is NOT in `arp_table`**
        *   Treat as a new device.
        *   Log the discovery via `log_info()`.
        *   Add the IP-MAC pair to `arp_table`.

## 4. Alerting
- **On Spoof Detection**:
    - A warning is printed to the console immediately.
    - A detailed log entry (Timestamp, IP, Old MAC, New MAC) is written to `logs/alerts.log`.

## 5. Termination
- The user presses `Ctrl+C`.
- `main.py` catches the `KeyboardInterrupt`.
- The program prints a stopping message and exits cleanly.