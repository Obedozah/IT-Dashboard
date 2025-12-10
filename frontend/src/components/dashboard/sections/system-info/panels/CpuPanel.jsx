import './CpuPanel.css';

function CpuPanel({CpuMetrics}) {

    return (
        <div className="cpu-panel panel">
            <div className="label-row row">
                <span className="label">CPU</span>
            </div>
            <div className="core-row row">
                <span className="label">Core Count</span>
                <span className="value">{CpuMetrics?.cpu_physical_cores != null ? CpuMetrics.cpu_physical_cores + ' MHz' : 'Loading...'}</span>
            </div>
            <div className="min-frequency-row row">
                <span className="label">Min Freq.</span>
                <span className="value">{CpuMetrics?.cpu_frequency_min != null ? CpuMetrics.cpu_frequency_min + ' MHz' : 'Loading...'}</span>
            </div>
            <div className="current-frequency-row row">
                <span className="label">Current Freq.</span>
                <span className="value">{CpuMetrics?.cpu_frequency_current != null ? CpuMetrics.cpu_frequency_current + ' MHz' : 'Loading...'}</span>
            </div>
            <div className="max-frequency-row row">
                <span className="label">Max Freq.</span>
                <span className="value">{CpuMetrics?.cpu_frequency_max != null ? CpuMetrics.cpu_frequency_max + ' MHz' : 'Loading...'}</span>
            </div>
        </div>
    )
}

export default CpuPanel;