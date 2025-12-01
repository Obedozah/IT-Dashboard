import socket

def scan_ports(ip, port, timeout):
    open_ports = []
    closed_ports = []
    common_ports = [22, 23, 80, 443, 8080, 3306, 5432, 6379]

    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((ip, port))

        if result == 0:
            open_ports.append(port)
            s.close()
        else:
            closed_ports.append(port)
            s.close()
    return open_ports, closed_ports