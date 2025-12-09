import './DiskPanel.css';

function DiskPanel({DiskMetrics}) {

    return (
        <div className="disk-panel panel">
            <div className="label-box">
                <span className="label">Disks</span>
            </div>

            <div className="disk-box">
                <div className="device-row row">
                    <span className="label">Device</span>
                    <span className="value">Value</span>
                </div>
                <div className="mount-point-row row">
                    <span className="label">Mount Point</span>
                    <span className="value">Value</span>
                </div>
                <div className="fs-type-row row">
                    <span className="label">FS Type</span>
                    <span className="value">Value</span>
                </div>
                <div className="disk-space-box">
                    <div className="disk-chart"></div>
                </div>
            </div>

            <div className="value-box">
                <span className="value">Value</span>
            </div>
        </div>
    )
}

export default DiskPanel;