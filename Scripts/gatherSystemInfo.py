import psutil
import platform
import socket
import uuid

def gather_system_info():
    systemInfo = {
        "os" : {
            "platform": platform.system(),
            "platformRelease": platform.release(),
            "platformVersion": platform.version()
        },
        "cpu": {
            "physicalCores": psutil.cpu_count(),
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
    }
    networkInfo = {
        "hostname": socket.gethostname(),
        "ipAddress": socket.gethostbyname(networkInfo.hostname),
        "macAddress": getMacAddress()
    }

def getMacAddress():
    macAddressBits = uuid.getnode()
    macAddressHex = '%012x' % macAddressBits
    macAddress = ':'.join(macAddressHex[i:i+2] for i in range(0, 12, 2))
    return macAddress