import icmplib
from icmplib import ping

def check_status(ip):

    # Ping Status for IP
    try:
        ping_status = ping(ip, count=4, timeout=0.1, privileged=False)
        if ping_status.is_alive:
            return "Online"
        else:
            return "Offline"
    except icmplib.exceptions.ICMPLibError as e:
        print(f"Error Pinging: {e}")
        return "Offline"