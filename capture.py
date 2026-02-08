# Captures DNS packets from the network interface

from scapy.all import sniff, DNS

def capture_dns(callback):
    # This function looks for DNS traffic

    def handle_packet(packet):
        # Checks if the packet contains a DNS layer
        if packet.layer(DNS) and packet[DNS].qd:
            # Extract the queried domain name 
            domain = packet[DNS].qd.qname.decode(errors = "ignore")

            # Send domain to the detection logic
            callback(domain)

    # Start sniffing UDP DNS traffic at (port 53) 
    sniff(filter = "udp port 53", prn = handle_packet, store = False)
    
