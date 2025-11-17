import subprocess
from scripts.system_info import gather_system_info as gsi
from scripts.network_scanner.local_arp.filter import filter_local_arp as filter
from scripts.network_scanner.local_arp.gather_entry_information import gather_entry_information

system_info = (gsi.gather_system_info())
platform = system_info['os']['platform'].lower()
def read_arp_table():
    # Find ARP entries
    if platform.lower() == 'linux':
        command = ['arp', '-n']
    else:
        command = ['arp', '-a']
    result = subprocess.run(command, capture_output=True, text=True)

    # Find Unique Arp Entry Information
    local_arp_data = [filter(result.stdout)]
    return gather_entry_information(local_arp_data)
    