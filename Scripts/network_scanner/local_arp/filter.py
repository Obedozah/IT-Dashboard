import re
import ipaddress

def is_bad_ip(ip):
    ip_object = ipaddress.ip_address(ip)
    if ip_object.is_loopback: return True
    if ip_object.is_multicast: return True
    if ip_object.is_unspecified: return True
    return False

def filter_local_arp(arp_data):
    filtered = []
    for line in arp_data.splitlines():
        line = line.strip()

        # Filtering out irrelevant lines
        if not line:
            continue
        # Irrelevant lines for Windows/Linux ARP output
        if line.lower().startswith('interface:') or line.lower().startswith('internet address') or line.lower().startswith('address'):
            continue

        # Extract/Filter IP Address
        ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
        if not ip_match:
            continue
        ip = ip_match.group(0)
        if is_bad_ip(ip):
            continue

        # Extract/Filter Mac Address
        mac_match = re.search(r'(([0-9A-Fa-f]{1,2}[:\-]){5}([0-9A-Fa-f]{1,2}))', line)
        if not mac_match:
            continue
        mac = mac_match.group(0)
        if mac.lower() == 'ff:ff:ff:ff:ff:ff' or mac.lower() == '00:00:00:00:00:00':
            continue

        # Add to filtered list
        filtered.append({
            'ip': ip,
            'mac': mac,
            'line': line
        })

    return filtered