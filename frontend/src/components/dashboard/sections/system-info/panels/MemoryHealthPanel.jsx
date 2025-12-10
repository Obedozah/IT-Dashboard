import './MemoryHealthPanel.css';

function MemoryHealthPanel({MemoryHealthMetrics}) {
    const getColor = (percent) => {
        if (percent >=80) return '#D05252';
        if (percent >=50) return '#F1E885';
        return '#559751';
    };

    const barColor = getColor(MemoryHealthMetrics.memory_used_percent);

    return (
        <div className="memory-health-panel panel">
            <div className="memory-health-box">
                <div className="memory-health-bar">
                    <div className="memory-health-bar-portion"
                        style={{
                            height: MemoryHealthMetrics.memory_used_percent + '%',
                            backgroundColor: barColor
                        }}>
                    </div>
                </div>
            </div>
            <div className="value-box">
                <span className="value">{MemoryHealthMetrics?.memory_used_percent != null ? MemoryHealthMetrics.memory_used_percent + '%' : 'Loading...'}</span>
            </div>
        </div>
    )
}

export default MemoryHealthPanel;