
import './SystemMetrics.css';
import OsPanel from './panels/OsPanel';
import NetworkPanel from './panels/NetworkPanel';
import CpuPanel from './panels/CpuPanel';
import CpuHealthPanel from './panels/CpuHealthPanel';
import MemoryPanel from './panels/MemoryPanel';
import MemoryHealthPanel from './panels/MemoryHealthPanel';

function SystemMetrics({metrics}) {

    return (
        <section className="system-metrics">
            <h2>System Metrics</h2>
            <div className="system-metrics-panels">
                <div className="os-network">
                    <OsPanel OsMetrics={metrics.os || {}}/>
                    <NetworkPanel NetworkMetrics={metrics.network_info || {}}/>
                </div>
                <div className="cpu-memory">
                    <div className="cpu">
                        <CpuPanel CpuMetrics={metrics.hardware_health || {}}/>
                        <CpuHealthPanel CpuHealthMetrics={metrics.hardware_health || {}}/>    
                    </div>
                    <div className="memory">
                        <MemoryPanel MemoryMetrics={metrics.hardware_health || {}}/>
                        <MemoryHealthPanel MemoryHealthMetrics={metrics.hardware_health || {}}/>
                    </div>
                </div>
            </div>
            <button className="network-scanner-button">Scan and Analyze LAN</button>
        </section>
    )
}

export default SystemMetrics;