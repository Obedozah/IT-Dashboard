import socket 
import uuid
import ipaddress
import psutil

# Get Default Interface
def get_default_interface():
    stats = psutil.net_if_stats()
    addrs = psutil.net_if_addrs()

    # Pick interface that is UP and has an IPv4 address
    for interface, iface_stats in stats.items():
        if iface_stats.isup and interface in addrs:
            for addr in addrs[interface]:
                if addr.family == socket.AF_INET:
                    return interface

    raise RuntimeError("No active network interface found.")

# Convert subnetmask to CIDR
def netmask_to_cidr(subnet_mask):
    octets = subnet_mask.split('.')
    binary_octets = [bin(int(octet))[2:].zfill(8) for octet in octets]
    return sum(octet.count('1') for octet in binary_octets)

# Reformat MAC address
def format_mac_address(mac_address):
    mac_hex = hex(mac_address)
    mac_str = ':'.join(mac_hex[i:i+2] for i in range(2, len(mac_hex), 2)) 
    return mac_str

# Return subnet host range
def subnet_host_range(hosts):
    subnet_list = list(hosts)
    return str(subnet_list[0]) + ' - ' + str(subnet_list[-1])

def find_broadcast_address(ip_address, netmask):
    if IF_NET.broadcast is None and netmask is not None:
        iface = ipaddress.IPv4Interface(f"{ip_address}/{netmask}")
        broadcast_address = str(iface.network.broadcast_address)
    else:
        broadcast_address = IF_NET.broadcast
    return broadcast_address
    

# Unused variables
default_interface = get_default_interface()
IF_NET = next(a for a in psutil.net_if_addrs()[default_interface] if a.family == socket.AF_INET)
netmask = IF_NET.netmask
cidr = netmask_to_cidr(netmask)

# Network util variables
hostname = socket.gethostname()
mac_address = format_mac_address(uuid.getnode())
ip_address = IF_NET.address
network_address = ipaddress.ip_network(f"{ip_address}/{cidr}", strict=False)
broadcast_address = find_broadcast_address(ip_address, netmask)
subnet_host_range = subnet_host_range(network_address.hosts())