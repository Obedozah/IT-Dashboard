import psutil
import platform
from . import network_utils as net

def gather_system_info():

    system_info = {
        "os" : {
            "platform": platform.system(),
            "platformRelease": platform.release(),
            "platformVersion": platform.version()
        },
        "hardwareHealth": {
            "cpu": {
                "physical_cores": psutil.cpu_count(),
                "logical_cores": psutil.cpu_count(logical=True),
                "frequency": psutil.cpu_freq()._asdict(),
                "usage_percent": psutil.cpu_percent(interval=1)
            },
            "memory": {
                "total": psutil.virtual_memory().total,
                "available": psutil.virtual_memory().available,
                "used": psutil.virtual_memory().used,
                "percent": psutil.virtual_memory().percent
            }
        },
        "network_info": {
            "hostname": net.hostname,
            "ip_address": net.ip_address,
            "mac_address": net.mac_address,
            "cidr": net.cidr
        }
    }
    return system_info