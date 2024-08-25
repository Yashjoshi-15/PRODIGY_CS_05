from telnetlib import IP
from scapy.all import *
import tcp

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"Source IP: {src_ip} --> Destination IP: {dst_ip} Protocol: {protocol}")
        
        if tcp in packet:
            src_port = packet[tcp].sport
            dst_port = packet[tcp].dport
            print(f"Source Port: {src_port} --> Destination Port: {dst_port}")

            if Raw in packet:
                payload = packet[Raw].load
                print(f"Payload: {payload}")

def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()


