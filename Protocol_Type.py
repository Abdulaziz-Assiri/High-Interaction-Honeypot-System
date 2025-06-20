from scapy.all import sniff, Packet
from scapy.layers.inet import IP, TCP, UDP
import ipaddress
import sys
import os

class Protocol_Type:
    attack_attempts = {}
    tcp_connection_count = 0
    udp_connection_count = 0

    def is_class_d_or_e(self, ip_address):
        try:
            ip_obj = ipaddress.ip_address(ip_address)
            return ip_obj.is_multicast or (ip_obj.version == 4 and ip_obj.packed[0] >= 240)
        except ValueError:
            return False

    def packet_callback(self, packet: Packet):
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst

            if self.is_class_d_or_e(src_ip) or self.is_class_d_or_e(dst_ip):
                return

            protocol = None

            if TCP in packet:
                protocol = "TCP"
                Protocol_Type.tcp_connection_count += 1
            elif UDP in packet:
                protocol = "UDP"
                Protocol_Type.udp_connection_count += 1

            if protocol is not None:
                Protocol_Type.attack_attempts[dst_ip] = Protocol_Type.attack_attempts.get(dst_ip, 0) + 1
                sorted_attempts = sorted(Protocol_Type.attack_attempts.items(), key=lambda item: item[1], reverse=True)
                print(f"TCP Connections: {Protocol_Type.tcp_connection_count}, UDP Connections: {Protocol_Type.udp_connection_count}")
                sys.stdout.flush()

    def main(self):
        interface = "your hoenypot interface"
        print(f"Sniffing traffic on interface {interface}...")
        try:
            sniff(iface=interface, prn=self.packet_callback, store=0)
        except PermissionError:
            print("Error: You need root privileges to sniff network traffic.")
            sys.stdout.flush()
        except KeyboardInterrupt:
            print("\nSniffing stopped by user.")
            sys.stdout.flush()

if __name__ == "__main__":
    sniffer = Protocol_Type()
    sniffer.main()
