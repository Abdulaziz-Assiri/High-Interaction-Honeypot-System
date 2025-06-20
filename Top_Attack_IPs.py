from scapy.all import sniff, Packet
from scapy.layers.inet import IP, TCP, UDP
import ipaddress
import sys

class Top_Attack_IPs:
    attack_attempts = {}

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

            dst_port = None
            protocol = None

            if TCP in packet:
                dst_port = packet[TCP].dport
                protocol = "TCP"
            elif UDP in packet:
                dst_port = packet[UDP].dport
                protocol = "UDP"

            if dst_port is not None:

                Top_Attack_IPs.attack_attempts[dst_ip] = Top_Attack_IPs.attack_attempts.get(dst_ip, 0) + 1
                sorted_attempts = sorted(Top_Attack_IPs.attack_attempts.items(), key=lambda item: item[1], reverse=True)
                print(sorted_attempts)
                sys.stdout.flush()



    def main(self):
        interface = "honeypot network interface"
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
    sniffer = Top_Attack_IPs()
    sniffer.main()
