import psutil
import platform
import time
import datetime
from scripts.system_info import network_utils as net

def gather_system_info():
    
    # OS Info
    uptime_seconds = int(time.time()) - psutil.boot_time()
    uptime_hours = str(datetime.timedelta(seconds=uptime_seconds))

    os = {
        "platform": platform.system(),
        "platform_release": platform.release(),
        "platform_version": platform.version(),
        "kernel_version": platform.uname().release,
        "architecture": platform.machine(),
        "uptime_seconds": uptime_seconds,
        "uptime_hours": uptime_hours
    }

    # Hardware Health
    memory_total = psutil.virtual_memory().total
    memory_available = psutil.virtual_memory().available
    memory_used = psutil.virtual_memory().used
    mb_convert = (1024 ** 2)

    all_disks = []
    gb_convert = (1024 ** 3)
    for disk in psutil.disk_partitions():
        usage = psutil.disk_usage(disk.mountpoint)
        if round(usage.used / gb_convert, 2) < 1: continue
        all_disks.append({
            "device": disk.device,
            "mountpoint": disk.mountpoint,
            "fstype": disk.fstype,
            "total_gb": round(usage.total / gb_convert, 2),
            "used_gb": round(usage.used / gb_convert, 2),
            "free_gb": round(usage.free / gb_convert, 2),
            "percent_used": usage.percent
        })

    hardware_health = {
        # CPU
        "cpu_physical_cores": psutil.cpu_count(),
        "cpu_logical_cores": psutil.cpu_count(logical=True),
        "cpu_frequency_mhz": psutil.cpu_freq()._asdict(),
        "cpu_usage_percent": psutil.cpu_percent(interval=1),

        # Memory
        "memory_total": memory_total,
        "memory_total_mb": memory_total / mb_convert,
        "memory_available": memory_available,
        "memory_available_mb": memory_available / mb_convert,
        "memory_used": memory_used,
        "memory_used_mb": memory_used / mb_convert,
        "memory_used_percent": psutil.virtual_memory().percent,

        # Disk Usage
        "all_disks": all_disks
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