from scapy.all import sniff
from scapy.layers.l2 import ARP
from src.arp_detector import detect_arp_spoof

def start_sniffing(interface):
    sniff(
        iface=interface,
        filter="arp",
        store=False,
        prn=detect_arp_spoof
    )
