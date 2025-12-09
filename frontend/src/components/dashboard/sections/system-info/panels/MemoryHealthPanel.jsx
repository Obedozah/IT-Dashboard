import './MemoryHealthPanel.css';

function MemoryHealthPanel({MemoryHealthMetrics}) {
    const usage = MemoryHealthMetrics?.memory_used_percent ?? 0;

    const getColor = (percent) => {
        if (percent >=80) return '#D05252';
        if (percent >=50) return '#F1E885';
        return '#559751';
    };

    const barColor = getColor(usage);

    return (
        <div className="memory-health-panel panel">
            <div className="memory-health-box">
                <div className="memory-health-bar">
                    <div className="memory-health-bar-portion"
                        style={{
                            height: usage + '%',
                            backgroundColor: barColor
                        }}>
                    </div>
                </div>
            </div>
            <div className="value-box">
                <span className="value">{usage + '%' || 'Loading...'}</span>
            </div>
        </div>
    )
}

export default MemoryHealthPanel;