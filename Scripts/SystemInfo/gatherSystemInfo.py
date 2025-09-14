import psutil
import platform
from . import network_utils as net

def gather_system_info():

    systemInfo = {
        "os" : {
            "platform": platform.system(),
            "platformRelease": platform.release(),
            "platformVersion": platform.version()
        },
        "hardwareHealth": {
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
        },
        "networkInfo": {
            "hostname": net.hostname,
            "ipAddress": net.ipAddress,
            "macAddress": net.macAddress,
            "CIDR": net.CIDR
        }
    }
    return systemInfo