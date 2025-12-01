import subprocess
from scripts.system_info import gather_system_info as gsi
import re

system_info = gsi.gather_system_info()
platform = system_info['os']['platform'].lower()

def check_status(ip):
    if platform.lower() == 'windows':
        command = ['ping', '-n', '1', ip]
    else:
        command = ['ping', '-c', '1', ip]

    status = subprocess.run(command, capture_output=True, text=True)
    if status.returncode == 0:
        ttl_line = re.search(r'ttl=(\d+)', status.stdout.lower())
        ttl = ttl_line.group(1)
        return "Online", ttl
    else:
        return "Offline", "N/A"