import socket 
import uuid
import psutil

def netmask_to_cidr(subnet_mask):
    if not subnet_mask:
        return None
    octets = subnet_mask.split('.')
    binary_octets = [bin(int(octet))[2:].zfill(8) for octet in octets]
    return sum(octet.count('1') for octet in binary_octets)

# Gather Network Information
hostname = socket.gethostname()
mac_address = uuid.getnode()
ip_address = socket.gethostbyname(hostname)

subnet_mask = None
for interface, addrs in psutil.net_if_addrs().items():
    for addr in addrs:
        if addr.family == socket.AF_INET and addr.address == ip_address:
            subnet_mask = addr.netmask
            break

cidr = netmask_to_cidr(subnet_mask)
    