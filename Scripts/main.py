from scripts.system_info import gather_system_info as gsi
from scripts.network_scanner.local_arp import reader

if __name__ == "__main__":
    print(gsi.gather_system_info())
    print("\n")
    print(reader.read_arp_table())