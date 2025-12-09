import {useState, useEffect} from 'react';
import './SystemMetrics.css';
import OsPanel from './panels/OsPanel';
import NetworkPanel from './panels/NetworkPanel';
import CpuPanel from './panels/CpuPanel';
import CpuHealthPanel from './panels/CpuHealthPanel';
import MemoryPanel from './panels/MemoryPanel';
import MemoryHealthPanel from './panels/MemoryHealthPanel';

function SystemMetrics() {

    const [metrics, setMetrics] = useState({});

    useEffect(() => {
        let isMounted = true;

        async function getSystemMetrics() {
            try {
                const response = await fetch('/device');
                const data = await response.json();
                if (isMounted) {
                    setMetrics(data);
                }
            } catch (err) {
                console.log("Failed to get Metrics:", err);
            }
        }
        
        getSystemMetrics();

        const intervalId = setInterval(getSystemMetrics, 1000);

        return () => {
            isMounted = false;
            clearInterval(intervalId);
        }
    }, []);

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