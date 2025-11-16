import subprocess
from scripts.system_info import gather_system_info as gsi
from scripts.network_scanner.local_arp.filter import filter_local_arp as filter
from scripts.network_scanner.local_arp.port_scanner import scan_ports as port_scan

system_info = gsi.gather_system_info()
os = system_info['os']['platform'].lower()
def read_arp_table():
    # Find ARP entries
    if os == 'linux':
        command = ['arp', '-n']
    else:
        command = ['arp', '-a']
    result = subprocess.run(command, capture_output=True, text=True)

    local_arp_data = [filter(result.stdout)]
    for entry in local_arp_data[0]:
        open_ports, closed_ports = port_scan(entry['ip'])
        entry['open_ports'] = open_ports
        entry['closed_ports'] = closed_ports

    return local_arp_data
