from flask import Flask
from flask_cors import CORS
from scripts.system_info import gather_system_info as gsi
from scripts.network_scanner.full_scan import full_scan

app = Flask(__name__)
CORS(app)

os, hardware_health, network_info = gsi.gather_system_info()

@app.route('/device', methods= ["GET"])
def gather_system_info():
    os, hardware_health, network_info = gsi.gather_system_info()
    system_info = {
        "os": os,
        "hardware_health": hardware_health,
        "network_info": network_info
    }
    return system_info

@app.route('/scan', methods=["GET"])
def scan():
    _, _, network_info = gsi.gather_system_info()
    meta_data, arp_sweep_data = full_scan(network_info)
    scan_data = {
        "meta_data": meta_data,
        "arp_sweep_data": arp_sweep_data
    }
    return scan_data

if __name__ == "__main__":
    app.run()