import './CpuHealthPanel.css';

function CpuHealthPanel({CpuHealthMetrics}) {
    const usage = CpuHealthMetrics?.cpu_usage_percent ?? 0;

    const getColor = (percent) => {
        if (percent >=80) return '#D05252';
        if (percent >=50) return '#F1E885';
        return '#559751';
    };

    const barColor = getColor(usage);

    return (
        <div className="cpu-health-panel panel">
            <div className="cpu-health-box">
                <div className="cpu-health-bar">
                    <div className="cpu-health-bar-portion"
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

export default CpuHealthPanel;