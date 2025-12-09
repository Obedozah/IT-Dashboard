import './MemoryHealthPanel.css';

function MemoryHealthPanel({MemoryHealthMetrics}) {
    return (
        <div className="memory-health-panel panel">
            <div className="label-box">
                <span className="label">Memory</span>
            </div>
            <div className="memory-health-box">
                <div className="memory-health-bar">
                    <div className="memory-health-bar-portion"></div>
                </div>
            </div>
            <div className="value-box">
                <span className="value">{MemoryHealthMetrics.memory_used_percent || 'Loading...'}</span>
            </div>
        </div>
    )
}

export default MemoryHealthPanel;