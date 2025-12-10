from flask import Flask, send_from_directory
import webbrowser
import threading
import os
from flask_cors import CORS
from scripts.system_info import gather_system_info as gsi
from scripts.network_scanner.full_scan import full_scan

app = Flask(__name__, static_folder="frontend/build")
CORS(app)

@app.route('/', defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")

current_os, hardware_health, network_info = gsi.gather_system_info()

@app.route('/device', methods= ["GET"])
def gather_system_info():
    os, hardware_health, network_info = gsi.gather_system_info()
    system_info = {
        "os": current_os,
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

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run()