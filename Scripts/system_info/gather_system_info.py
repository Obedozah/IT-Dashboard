import psutil
import platform
import json
from scripts.system_info import network_utils as net

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
            "mac_address": net.mac_address,
            "ip_address": net.ip_address,
            "network_address": str(net.network_address),
            "broadcast_address": net.broadcast_address,
            "subnet_host_range": net.subnet_host_range
        }
    }
    return system_info