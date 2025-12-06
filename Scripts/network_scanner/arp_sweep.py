from scapy.all import ARP, Ether, srp

def arp_sweep(network_info):

    # Sweep Variables
    devices = []
    target_ip_range = network_info["network_address"]
    broadcast_address = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request = broadcast_address / ARP(pdst=target_ip_range)
    answered, _ = srp(arp_request, timeout = 1, verbose = 0)

    # Appending Answered Devices
    for _, received in answered:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices