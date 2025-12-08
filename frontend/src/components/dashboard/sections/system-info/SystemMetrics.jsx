import './SystemMetrics.css';
import OsPanel from './panels/OsPanel';
import NetworkPanel from './panels/NetworkPanel';
import CpuHealthPanel from './panels/CpuHealthPanel';
import MemoryHealthPanel from './panels/MemoryHealthPanel';
import DiskPanel from './panels/DiskPanel';

function SystemMetrics() {
    return (
        <section className="system-metrics">
            <div className="os-network">
                <OsPanel/>
                <NetworkPanel/>
            </div>
            <div className="cpu-memory">
                <CpuHealthPanel/>
                <MemoryHealthPanel/>
            </div>
            <div className="disks">
                <DiskPanel/>
            </div>
        </section>
    )
}

export default SystemMetrics;