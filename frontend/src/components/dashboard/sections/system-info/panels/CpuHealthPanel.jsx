import './CpuHealthPanel.css';

function CpuHealthPanel() {
    return (
        <div className="cpu-health-panel">
            <span className="label">CPU</span>
            <div className="cpu-health-visual">visual</div>
            <span className="value">value</span>
        </div>
    )
}

export default CpuHealthPanel;