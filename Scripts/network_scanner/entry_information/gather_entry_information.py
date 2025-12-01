from scripts.network_scanner.entry_information.get_hostname import get_hostname
from scripts.network_scanner.entry_information.scan_ports import scan_ports
from scripts.network_scanner.entry_information.vendor_lookup import vendor_lookup
from scripts.network_scanner.entry_information.check_status import check_status
from concurrent.futures import ThreadPoolExecutor

def gather_entry_information(local_arp_data):
    for entry in local_arp_data[0]:
        # Hostname/Vendor
        entry['hostname'] = get_hostname(entry['ip'], entry['raw_line'])
        vendor = vendor_lookup(entry['mac'])
        entry['vendor'] = vendor
    
    # Status/TTL with Threading
    ping_futures = []
    with ThreadPoolExecutor(max_workers=20) as exec:
        for e in local_arp_data[0]:
            ping_futures.append(exec.submit(check_status, e["ip"]))

        for e, future in zip(local_arp_data[0], ping_futures):
            e["status"], e["ttl"] = future.result()

    # Port Scanning with Threading WIP

    return local_arp_data