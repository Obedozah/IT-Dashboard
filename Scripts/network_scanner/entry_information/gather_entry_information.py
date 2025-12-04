import time
import socket
from scripts.network_scanner.entry_information.vendor_lookup import vendor_lookup
from scripts.network_scanner.entry_information.check_status import check_status
from scripts.network_scanner.entry_information.scan_ports import scan_ports
from concurrent.futures import ThreadPoolExecutor

def gather_entry_information(entry_data):
    curr_time = time.time()

    # Vendor Lookup
    for entry in entry_data:
        try:
            entry["hostname"] = socket.gethostbyaddr(entry["ip"])[0]
        except socket.herror:
            entry["hostname"] = "N/A"
        entry["vendor"] = vendor_lookup(entry["mac"])
    end_time = time.time()
    elapsed_time = end_time - curr_time
    print(f"Hostname/Vendor Lookup Time: {elapsed_time} seconds")
    
    # Status/TTL with Threading
    curr_time = time.time()
    ping_futures = []
    with ThreadPoolExecutor(max_workers=10) as exec:
        for entry in entry_data:
            ping_futures.append(exec.submit(check_status, entry["ip"]))

        for entry, future in zip(entry_data, ping_futures):
            entry["ping_status"] = future.result()
    end_time = time.time()
    elapsed_time = end_time - curr_time
    print(f"Status Check Time: {elapsed_time} seconds")

    # Port Scanning with Threading
    curr_time = time.time()
    portscan_futures = []
    with ThreadPoolExecutor(max_workers=10) as exec:
        for entry in entry_data:
            portscan_futures.append(exec.submit(scan_ports, entry["ip"], 0.1))

        for entry, future in zip(entry_data, portscan_futures):
            entry["open_ports"], entry["closed_ports"] = future.result()

    end_time = time.time()
    elapsed_time = end_time - curr_time
    print(f"Port Scanning Time: {elapsed_time} seconds")

    return entry_data