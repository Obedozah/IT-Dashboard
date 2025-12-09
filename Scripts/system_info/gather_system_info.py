import psutil
import platform
import time
import datetime
from scripts.system_info import network_utils as net

def gather_system_info():
    
    # OS Info
    uptime_seconds = int(time.time()) - psutil.boot_time()
    uptime_hours = str(datetime.timedelta(seconds=uptime_seconds))

    os_platform = platform.system()
    if (os_platform == "Darwin"): os_platform = "macOS"

    os = {
        "platform": os_platform,
        "platform_release": platform.release(),
        "architecture": platform.machine(),
        "uptime_seconds": uptime_seconds,
        "uptime_hours": uptime_hours
    }

    # Hardware Health
    memory_total = psutil.virtual_memory().total
    memory_available = psutil.virtual_memory().available
    memory_used = psutil.virtual_memory().used
    memory_free = psutil.virtual_memory().free
    mb_convert = (1024 ** 2)
    gb_convert = (1024 ** 3)
    cpu_frequency = psutil.cpu_freq()

    hardware_health = {
        # CPU
        "cpu_physical_cores": psutil.cpu_count(),
        "cpu_usage_percent": round(psutil.cpu_percent(interval=1), 2),
        "cpu_frequency_current": cpu_frequency.current,
        "cpu_frequency_min": cpu_frequency.min,
        "cpu_frequency_max": cpu_frequency.max,

        # Memory
        "memory_total": memory_total,
        "memory_total_mb": round(memory_total / mb_convert, 2),
        "memory_total_gb": round(memory_total / gb_convert,2 ),
        "memory_available": memory_available,
        "memory_available_mb": round(memory_available / mb_convert, 2),
        "memory_available_gb": round(memory_available / gb_convert, 2),
        "memory_used": memory_used,
        "memory_used_mb": round(memory_used / mb_convert, 2),
        "memory_used_gb": round(memory_used / gb_convert, 2),
        "memory_used_percent": round(psutil.virtual_memory().percent, 2),
        "memory_free": memory_free,
        "memory_free_mb": round(memory_free / mb_convert, 2),
        "memory_free_gb": round(memory_free / gb_convert, 2),
    }

    # Network Information
    network_info = {
        "hostname": net.hostname,
        "mac_address": net.mac_address,
        "ip_address": net.ip_address,
        "network_address": str(net.network_address),
        "broadcast_address": net.broadcast_address,
        "subnet_host_range": net.subnet_host_range,
    }

    return os, hardware_health, network_info