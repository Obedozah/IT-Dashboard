from scripts.network_scanner.local_arp import get_hostname as host
from scripts.network_scanner.local_arp.port_scanner import scan_ports
from scripts.network_scanner.local_arp.vendor_lookup import vendor_lookup
from scripts.network_scanner.local_arp.check_status import check_status

def gather_entry_information(local_arp_data):
    for entry in local_arp_data[0]:
        # Hostname/Vendor
        entry['hostname'] = host.get_hostname(entry['ip'], ['line'])
        vendor = vendor_lookup(entry['mac'])
        entry['vendor'] = vendor

        # Open/Closed Ports
        open_ports, closed_ports = scan_ports(entry['ip'])
        entry['open_ports'] = open_ports
        entry['closed_ports'] = closed_ports

        # Status/TTL
        ping = check_status(entry['ip'])
        if ping is not False:
            entry['status'] = "Online"
            entry['TTL'] = ping
        else:
            entry['status'] = "Offline"
            entry['TTL'] = 'N/A'

    return local_arp_data