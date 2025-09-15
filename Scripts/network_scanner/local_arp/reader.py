import subprocess
#import filter
from system_info import gather_system_info as gsi

system_info = gsi.gather_system_info()
os = system_info['os']['platform'].lower()
def read_arp_table():
    if os == 'linux':
        command = ['arp', '-n']
    else:
        command = ['arp', '-a']

    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout
    # return filter.filter_local_arp(result.stdout)