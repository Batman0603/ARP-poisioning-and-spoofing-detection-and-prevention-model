import sys
from src.arp_sniffer import start_sniffing
from config.settings import INTERFACE

if __name__ == "__main__":
    print("[*] Starting ARP Spoof Detection...")
    try:
        start_sniffing(INTERFACE)
    except KeyboardInterrupt:
        print("\n[!] Stopping ARP Spoof Detection.")
        sys.exit(0)
