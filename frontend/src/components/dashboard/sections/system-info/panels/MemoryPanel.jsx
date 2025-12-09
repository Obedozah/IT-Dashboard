import './MemoryPanel.css';

function MemoryPanel({MemoryMetrics}) {

    return (
        <div className="memory-panel panel">
            <div className="label-row row">
                <span className="label">Memory</span>
            </div>
            <div className="memory-total-row row">
                <span className="label">Total Memory</span>
                <span className="value">{MemoryMetrics.memory_total_gb + ' GB'}</span>
            </div>
            <div className="memory-available-row row">
                <span className="label">Memory Available</span>
                <span className="value">{MemoryMetrics.memory_available_gb + ' GB'}</span>
            </div>
            <div className="memory-used-row row">
                <span className="label">Memory Used</span>
                <span className="value">{MemoryMetrics.memory_used_gb + ' GB'}</span>
            </div>
            <div className="memory-cached-row row">
                <span className="label">Memory Free</span>
                <span className="value">{MemoryMetrics.memory_free_gb + ' GB'}</span>
            </div>
        </div>
    )
}

export default MemoryPanel;