from system_info import gather_system_info as gsi
from network_scanner.local_arp import reader

if __name__ == "__main__":
    system_info = gsi.gather_system_info()
    print(system_info)
    local_arp = reader.read_arp_table()
    print(local_arp)