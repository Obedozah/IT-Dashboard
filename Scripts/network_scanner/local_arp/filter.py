import re
import ipaddress

def filter_local_arp(arp_data):
    filtered = []
    for line in arp_data.splitlines():
        line = line.strip()
        if not line:
            continue

        if line.lower().startswith('Interface:') or line.lower().startswith('Internet Address'):
            continue

        ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
        if not ip_match:
            continue

        ip = ip_match.group(0)
        if is_bad_ip(ip):
            continue

        mac_match = re.search(r'(([0-9A-Fa-f]{2}[:\-]){5}([0-9A-Fa-f]{2}))', line)
        if not mac_match:
            continue

        mac = mac_match.group(0)
        if mac.lower() == 'ff:ff:ff:ff:ff:ff' or mac.lower() == '00:00:00:00:00:00':
            continue

        filtered.append({
            'ip': ip,
            'mac': mac,
            'raw_line': line
        })

    return filtered

def is_bad_ip(ip):
    ip_object = ipaddress.ip_address(ip)
    if ip_object.is_loopback: return True
    if ip_object.is_multicast: return True
    if ip_object.is_unspecified: return True
    return False