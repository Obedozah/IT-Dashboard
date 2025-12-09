import './MetaData.css';

function MetaData({MetaData}) {
    return (
        <section className="meta-data">
            <hr></hr>
            <h2>Network Scanner Metrics</h2>
            <div className="label-row row">
                <span className="label">
                    Meta Data
                </span>
            </div>
            <div className="device-count-row row">
                <span className="label">Device Count</span>
                <span className="value">?</span>
            </div>
            <div className="scan-time-row row">
                <span className="label">Scan Time</span>
                <span className="value">?</span>
            </div>
            <div className="network-isolation-row row">
                <span className="label">Network Isolation</span>
                <span className="value">?</span>
            </div>
        </section>   
    )
}

export default MetaData;
