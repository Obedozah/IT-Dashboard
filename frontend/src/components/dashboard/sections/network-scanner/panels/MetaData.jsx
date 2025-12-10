import './MetaData.css';

function MetaData({metaData}) {
    return (
        <section className="meta-data">
            <hr></hr>
            <h2>Network Scanner Metrics</h2>

            <div className="rows panel">
                <div className="label-row row">
                    <span className="label">
                        Scan Metrics
                    </span>
                </div>
                <div className="device-count-row row">
                    <span className="label">Devices Found</span>
                    <span className="value">{metaData?.device_count != null ? metaData.device_count + ' Found' : 'Loading...'}</span>
                </div>
                <div className="scan-time-row row">
                    <span className="label">Scan Time</span>
                    <span className="value">{metaData?.scan_time != null ? metaData.scan_time + ' Seconds' : 'Loading...'}</span>
                </div>
                <div className="network-isolation-row row">
                    <span className="label">Network Isolation</span>
                    <span className="value">{metaData?.isolation_detected ?? 'Loading...'}</span>
                </div>
            </div>
        </section>   
    )
}

export default MetaData;
