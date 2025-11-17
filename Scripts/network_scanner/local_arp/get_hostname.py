from scripts.system_info import gather_system_info as gsi
import socket

def get_hostname(ip, line):
    system_info = gsi.gather_system_info()
    platform = system_info['os']['platform'].lower()

    if platform.lower() != 'darwin':
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            return "N/A"
    else:
        if line.lower().startswith('?'):
            return "N/A"
        else:
            hostname = line.split('(')[0].strip()
    return hostname
    