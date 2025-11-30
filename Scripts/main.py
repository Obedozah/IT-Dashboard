import json
from scripts.system_info import gather_system_info as gsi
from scripts.network_scanner.local_arp import reader
import time

if __name__ == "__main__":
    start_time = time.time()
    system_info = gsi.gather_system_info()
    print(json.dumps(system_info, indent = 2))
    local_arp = reader.read_arp_table()
    print(json.dumps(local_arp, indent = 2))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution Time: {elapsed_time} seconds")