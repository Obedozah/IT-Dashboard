from scripts.system_info import gather_system_info as gsi

def filter_local_arp(arp_data):
    arp_entries = arp_data.splitlines()
    filtered_data = []
    for entry in arp_entries:
        if entry[0] == '?':
            continue
        filtered_data.append(entry)
    return filtered_data
