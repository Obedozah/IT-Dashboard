from scripts.system_info import gather_system_info as gsi
from scripts.network_scanner.local_arp import reader

if __name__ == "__main__":
    system_info = gsi.gather_system_info()
    print(system_info)
    print(reader.read_arp_table())
