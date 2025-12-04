import socket

def scan_ports(ip, timeout):

    # Port Variables
    open_ports = []
    closed_ports = []
    common_ports = [
        22, 80, 443,
        53,
        135, 137, 138, 139, 445,
        3389, 5900,
        23, 161
    ]

    # Check Ports
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