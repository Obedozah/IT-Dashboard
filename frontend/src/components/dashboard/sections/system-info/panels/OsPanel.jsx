import './OsPanel.css';

function OsPanel({OsMetrics}) {
    return (
        <div className="os-panel panel">
            <div className="os-row">
                <span className="label">Platform</span>
                <span className="value">{OsMetrics.platform || 'Loading...'}</span>
            </div>
            <div className="os-row">
                <span className="label">Platform Release</span>
                <span className="value">{OsMetrics.platform_release || 'Loading...'}</span>
            </div>
            <div className="os-row">
                <span className="label">Architecture</span>
                <span className="value">{OsMetrics.architecture || 'Loading...'}</span>
            </div>
            <div className="os-row">
                <span className="label">Up-time</span>
                <span className="value">{OsMetrics.uptime_hours || 'Loading...'}</span>
            </div>
        </div>
    );
}

export default OsPanel;