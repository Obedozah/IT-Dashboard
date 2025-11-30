from scripts.network_scanner.entry_information.scan_ports import scan_ports

if __name__ == "__main__":
    test_ip = "192.168.61.1"

    open_ports, closed_ports = scan_ports(test_ip)
    print(f"Open ports on {test_ip}: {open_ports}")
    print(f"Closed ports on {test_ip}: {closed_ports}")