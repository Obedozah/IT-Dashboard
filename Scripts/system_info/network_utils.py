import socket 
import uuid
import ipaddress
import netifaces

# Get Default Interface
def get_default_interface():
    gws = netifaces.gateways()
    default_interface = gws['default'][netifaces.AF_INET][1]
    return default_interface

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

# Unused variables
default_interface = get_default_interface()
IF_NET = netifaces.ifaddresses(default_interface).get(netifaces.AF_INET)[0]
ip = IF_NET['addr']
netmask = IF_NET['netmask']
cidr = netmask_to_cidr(netmask)

# Network util variables

hostname = socket.gethostname()
mac_address = format_mac_address(uuid.getnode())
ip_address = ipaddress.IPv4Interface(ip + '/' + str(cidr))
network_address = ip_address.network
broadcast_address = IF_NET['broadcast']
subnet_host_range = subnet_host_range(network_address.hosts())