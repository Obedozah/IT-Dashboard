import json
import time
from scripts.system_info import gather_system_info as gsi
from scripts.network_scanner.arp_sweep import arp_sweep
from scripts.network_scanner.gather_entry_information import gather_entry_information as gei


if __name__ == "__main__":
    start_time = time.time()

    # Gather/Print System Information
    os, hardware_health, network_info = gsi.gather_system_info()
    print(f"OS: {json.dumps(os, indent = 2)}")
    print(f"Hardware Health: {json.dumps(hardware_health, indent = 2)}")
    print(f"Network Info: {json.dumps(network_info, indent = 2)}")

    # Sweep LAN/Print Gathered System Info
    arp_sweep_data = arp_sweep(network_info)
    print(f"Arp Sweep: {json.dumps(gei(arp_sweep_data), indent = 2)}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Entire Program Execution Time: {elapsed_time} seconds")