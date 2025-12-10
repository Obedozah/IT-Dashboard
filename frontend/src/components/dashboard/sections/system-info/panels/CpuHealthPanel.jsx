import './CpuHealthPanel.css';

function CpuHealthPanel({CpuHealthMetrics}) {

    const getColor = (percent) => {
        if (percent >=80) return '#D05252';
        if (percent >=50) return '#F1E885';
        return '#559751';
    };

    const barColor = getColor(CpuHealthMetrics.cpu_usage_percent);

    return (
        <div className="cpu-health-panel panel">
            <div className="cpu-health-box">
                <div className="cpu-health-bar">
                    <div className="cpu-health-bar-portion"
                        style={{
                            height: CpuHealthMetrics.cpu_usage_percent + '%',
                            backgroundColor: barColor
                        }}>    
                    </div>
                </div>
            </div>
            <div className="value-box">
                <span className="value">{CpuHealthMetrics?.cpu_usage_percent != null ? CpuHealthMetrics.cpu_usage_percent + '%' : 'Loading...'}</span>
            </div>
        </div>
    )
}

export default CpuHealthPanel;