import './CpuHealthPanel.css';

function CpuHealthPanel({CpuHealthMetrics}) {
    return (
        <div className="cpu-health-panel panel">
            <div className="label-box">
                <span className="label">CPU</span>
            </div>
            <div className="cpu-health-box">
                <div className="cpu-health-bar">
                    <div className="cpu-health-bar-portion"></div>
                </div>
            </div>
            <div className="value-box">
                <span className="value">{CpuHealthMetrics.cpu_usage_percent || 'Loading...'}</span>
            </div>
        </div>
    )
}

export default CpuHealthPanel;