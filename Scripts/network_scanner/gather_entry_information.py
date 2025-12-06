import socket
from scripts.network_scanner.scan_helper_scripts.vendor_lookup import vendor_lookup
from scripts.network_scanner.scan_helper_scripts.check_status import check_status
from scripts.network_scanner.scan_helper_scripts.scan_ports import scan_ports
from concurrent.futures import ThreadPoolExecutor

def gather_entry_information(entry_data):

    # Vendor Lookup
    for entry in entry_data:
        try:
            entry["hostname"] = socket.gethostbyaddr(entry["ip"])[0]
        except socket.herror:
            entry["hostname"] = "N/A"
        entry["vendor"] = vendor_lookup(entry["mac"])

    # Status/TTL with Threading
    ping_futures = []
    with ThreadPoolExecutor(max_workers=10) as exec:
        for entry in entry_data:
            ping_futures.append(exec.submit(check_status, entry["ip"]))

        for entry, future in zip(entry_data, ping_futures):
            entry["ping_status"] = future.result()
    
    # Port Scanning with Threading
    portscan_futures = []
    with ThreadPoolExecutor(max_workers=10) as exec:
        for entry in entry_data:
            portscan_futures.append(exec.submit(scan_ports, entry["ip"], 0.1))

        for entry, future in zip(entry_data, portscan_futures):
            entry["open_ports"], entry["closed_ports"] = future.result()

    return entry_data