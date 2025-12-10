import './ScannedDevices.css';

function ScannedDevices({scanMetrics}) {

    return (
        <section className="scanned-devices-content panel">
            {scanMetrics?.map((device) => (
                <div key={device.ip} className="scanned-device">
                    <div className="ping-status-content">
                        <span className="ping-status">{device.ping_status}</span>
                        <div className="ping-status-indicator panel" style={{backgroundColor: device.ping_status === "Online" ? "#559751" : "#D05252"}}></div>
                    </div>

                    <div className="scanned-device-rows">
                        <div className="scanned-device-row hostname-row panel">
                            <span className="label">Hostname</span>
                            <span className="value">{device.hostname}</span>
                        </div>
                        <div className="scanned-device-row mac-row panel">
                            <span className="label">MAC Address</span>
                            <span className="value">{device.mac}</span>
                        </div>
                        <div className="scanned-device-row ip-row panel">
                            <span className="label">IP Address</span>
                            <span className="value">{device.ip}</span>
                        </div>
                        <div className="scanned-device-row vendor-row panel">
                            <span className="label">Vendor</span>
                            <span className="value">{device.vendor}</span>
                        </div>
                    </div>

                    <div className="port-rows">
                        <div className="open-ports-content">
                            <span className="label">Open ports</span>
                            <div className="value panel">
                                {device.open_ports.length > 0 ? (
                                    device.open_ports.map((port, index) => (
                                        <div key={index} className="port-item">{port}</div>
                                    ))
                                ) :
                                (
                                        <div>None</div>
                                )}
                            </div>
                        </div>
                        <div className="closed-ports-content">
                            <span className="label">Closed ports</span>
                            <div className="value panel">
                                {device.closed_ports.length > 0 ? (
                                    device.closed_ports.map((port, index) => (
                                        <div key={index} className="port-item">{port}</div>
                                    ))
                                ) :
                                (
                                        <div>None</div>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            ))}
        </section>
    )
}

export default ScannedDevices;