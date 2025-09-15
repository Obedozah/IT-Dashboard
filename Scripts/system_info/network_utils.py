import socket 
import uuid
import psutil
import ipaddress

# Convert subnetmask to CIDR
def netmask_to_cidr(subnet_mask):
    octets = subnet_mask.split('.')
    binary_octets = [bin(int(octet))[2:].zfill(8) for octet in octets]
    return sum(octet.count('1') for octet in binary_octets)

# Resolve subnet mask
def get_subnet_mask():
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET and addr.address == socket.gethostbyname(socket.gethostname()):
                return addr.netmask
    return None

# Reformat Mac address
def format_mac_address(mac_address):
    mac_hex = hex(mac_address)
    mac_str = ':'.join(mac_hex[i:i+2] for i in range(2, len(mac_hex), 2))
    return mac_str

# Non-gathered variables
ip = socket.gethostbyname(socket.gethostname())
subnet_mask = get_subnet_mask()
cidr = netmask_to_cidr(subnet_mask)

# Gathered variables
hostname = socket.gethostname()
mac_address = format_mac_address(uuid.getnode())
ip_address = ipaddress.ip_interface(ip + '/' + str(cidr))
network_address = ip_address.network
broadcast_address = network_address.broadcast_address
subnet_host_range = list(network_address.hosts())