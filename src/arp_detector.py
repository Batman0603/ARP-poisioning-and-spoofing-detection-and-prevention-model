import sys
from scapy.layers.l2 import ARP
from src.alert_manager import raise_alert, log_info
from config.settings import GATEWAY_IP, GATEWAY_MAC

arp_table = {GATEWAY_IP: GATEWAY_MAC}

def detect_arp_spoof(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        ip = packet[ARP].psrc
        mac = packet[ARP].hwsrc

        if ip in arp_table:
            if arp_table[ip] != mac:
                sys.stdout.write("\n")
                sys.stdout.flush()
                raise_alert(ip, arp_table[ip], mac)
            else:
                # Visual feedback to confirm the tool is scanning traffic
                sys.stdout.write(f"\r[*] Scanning... Verified packet from {ip}     ")
                sys.stdout.flush()
        else:
            print() # Ensure the log prints on a new line
            if ip not in arp_table:
                log_info(f"Learned new device: {ip} -> {mac}")
            arp_table[ip] = mac
