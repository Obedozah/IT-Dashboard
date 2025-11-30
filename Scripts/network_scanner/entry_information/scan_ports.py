import threading
import socket

def scan_ports(ip):
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389]
    open_ports = []
    closed_ports = []

    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((ip, port))
        s.close()

        if result == 0:
            open_ports.append(port)
        else:
            closed_ports.append(port)
        print(f"Scanned port {port} on {ip}: {'Open' if result == 0 else 'Closed'}")

    return open_ports, closed_ports