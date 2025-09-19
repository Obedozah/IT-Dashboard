from system_info import gather_system_info as gsi

def filter_local_arp(arp_data):
    
    filtered_arp_entries = []
    arp_entries = arp_data.splitlines()