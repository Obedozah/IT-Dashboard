from scripts.network_scanner.gather_entry_information import gather_entry_information as gei
from scripts.network_scanner.arp_sweep import arp_sweep as sweep
import time

def full_scan(network_info):

    # Sweep w/timer
    start_time = time.time()
    arp_sweep_data = gei(sweep(network_info))
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Sweep meta data
    length = len(arp_sweep_data)
    isolation_detected = (length <= 1)
    meta_data = {
        "device_count": len(arp_sweep_data),
        "scan_time": round(elapsed_time, 2),
        "isolation_detected": isolation_detected
    }
    return meta_data, arp_sweep_data