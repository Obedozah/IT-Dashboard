import socket 
import uuid
import psutil

def netmaskToCIDR(subnetMask):
    if not subnetMask:
        return None
    octets = subnetMask.split('.')
    binaryOctets = [bin(int(octet))[2:].zfill(8) for octet in octets]
    return sum(octet.count('1') for octet in binaryOctets)

# Gather Network Information
hostname = socket.gethostname()
macAddress = uuid.getnode()
ipAddress = socket.gethostbyname(hostname)

subnetMask = None
for interface, addrs in psutil.net_if_addrs().items():
    for addr in addrs:
        if addr.family == socket.AF_INET and addr.address == ipAddress:
            subnetMask = addr.netmask
            break

CIDR = netmaskToCIDR(subnetMask)
    