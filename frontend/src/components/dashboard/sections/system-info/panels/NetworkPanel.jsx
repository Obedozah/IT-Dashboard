import './NetworkPanel.css';

function NetworkPanel({NetworkMetrics}) {
    return (
        <div className="network-panel panel">
            <div className="network-row">
                <span className="label">Hostname</span>
                <span className="value">{NetworkMetrics.hostname || 'Loading...'}</span>
            </div>
            <div className="network-row">
                <span className="label">Mac Address</span>
                <span className="value">{NetworkMetrics.mac_address || 'Loading...'}</span>
            </div>
            <div className="network-row">
                <span className="label">Private IP Address</span>
                <span className="value">{NetworkMetrics.ip_address || 'Loading...'}</span>
            </div>
            <div className="network-row">
                <span className="label">LAN Network Address</span>
                <span className="value">{NetworkMetrics.network_address || 'Loading...'}</span>
            </div>
            <div className="network-row">
                <span className="label">Broadcast Address</span>
                <span className="value">{NetworkMetrics.broadcast_address || 'Loading...'}</span>
            </div>
            <div className="network-row">
                <span className="label">LAN Host Range</span>
                <span className="value">{NetworkMetrics.subnet_host_range || 'Loading...'}</span>
            </div>
        </div>
    )
}

export default NetworkPanel;