import './Dashboard.css';
import SystemMetrics from './sections/system-info/SystemMetrics';
import NetworkScanner from './sections/network-scanner/NetworkScanner';

function Dashboard() {
    return (
        <section className="dashboard">
            <div className="system-metrics">
                <SystemMetrics/>
            </div>
            <div className="network-scanner">
                <NetworkScanner/>
            </div>
        </section>
    )
}

export default Dashboard;