from flask import Flask
from scripts.system_info import gather_system_info as gsi
from scripts.network_scanner.arp_sweep.arp_sweep import arp_sweep as sweep
from scripts.network_scanner.entry_information.gather_entry_information import gather_entry_information as gei

app = Flask(__name__)
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
def arp_sweep():
    _, _, network_info = gsi.gather_system_info()
    arp_sweep_data = gei(sweep(network_info))
    return arp_sweep_data

if __name__ == "__main__":
    app.run()