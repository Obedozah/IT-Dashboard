from manuf import manuf
import requests

def vendor_lookup(mac):
    mac_lookup = manuf.MacParser()
    vendor = mac_lookup.get_manuf(mac)
    if vendor:
        return vendor
    
    try:
        url = f"https://api.macvendors.com/{mac.upper()}"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text.strip()
    except Exception:
        pass
    return "N/A"