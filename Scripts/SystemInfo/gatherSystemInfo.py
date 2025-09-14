import psutil
import platform
import socket
import uuid
import netmaskToCIDR

def gather_system_info():

    # Gather Network Information
    hostname = socket.gethostname()
    macAddress = uuid.getnode()
    ipAddress = socket.gethostbyname(hostname)
    subnetMask = None
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET and addr.address == ipAddress:
                subnetMask = addr.netmask
                break

    systemInfo = {
        "os" : {
            "platform": platform.system(),
            "platformRelease": platform.release(),
            "platformVersion": platform.version()
        },
        "hardwareHealth": {
            "cpu": {
                "p hysicalCores": psutil.cpu_count(),
                "logicalCores": psutil.cpu_count(logical=True),
                "frequency": psutil.cpu_freq()._asdict(),
                "usagePercent": psutil.cpu_percent(interval=1)
            },
            "memory": {
                "total": psutil.virtual_memory().total,
                "available": psutil.virtual_memory().available,
                "used": psutil.virtual_memory().used,
                "percent": psutil.virtual_memory().percent
            }
        },
        "networkInfo": {
            "hostname": socket.gethostname(),
            "ipAddress": socket.gethostbyname(socket.gethostname()),
            "macAddress": uuid.getnode(),
            "subnetMask": subnetMask
        }
    }
    return systemInfo