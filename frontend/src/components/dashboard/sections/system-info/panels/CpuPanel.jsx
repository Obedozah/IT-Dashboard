import './CpuPanel.css';

function CpuPanel({CpuMetrics}) {

    return (
        <div className="cpu-panel panel">
            <div className="label-row row">
                <span className="label">CPU</span>
            </div>
            <div className="core-row row">
                <span className="label">Core Count</span>
                <span className="value">{CpuMetrics.cpu_physical_cores + ' MHz'}</span>
            </div>
            <div className="min-frequency-row row">
                <span className="label">Min Freq.</span>
                <span className="value">{CpuMetrics.cpu_frequency_min + ' MHz'}</span>
            </div>
            <div className="current-frequency-row row">
                <span className="label">Current Freq.</span>
                <span className="value">{CpuMetrics.cpu_frequency_current + ' MHz'}</span>
            </div>
            <div className="max-frequency-row row">
                <span className="label">Max Freq.</span>
                <span className="value">{CpuMetrics.cpu_frequency_max + ' MHz'}</span>
            </div>
        </div>
    )
}

export default CpuPanel;