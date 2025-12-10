import {useState, useEffect, useRef} from 'react';
import './Dashboard.css';
import SystemMetrics from './sections/system-info/SystemMetrics';
import NetworkScanner from './sections/network-scanner/NetworkScanner';

function Dashboard() {

    const [metrics, setMetrics] = useState({});
    const [isScanned, setIsScanned] = useState(false);
    const [scanMetrics, setScanMetrics] = useState({});

    // Get System Metrics from backend
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

    // Network Scanning Portion

    async function getNetworkScan() {
        try {
            const response = await fetch('/scan');
            const data = await response.json();
            setScanMetrics(data);
        } catch (err) {
            console.log("Failed to get Metrics:", err);
        }
        setIsScanned(true);
    }

    const panelRef = useRef(null);

    useEffect(() => {
        if (isScanned && panelRef.current) {
            panelRef.current.scrollIntoView({behavior: 'smooth', block: 'start'});
        }
    }, [isScanned]);

    return (
        <section className="dashboard">
            <div className="system-metrics">
                <SystemMetrics metrics={metrics} setIsScanned={setIsScanned} getNetworkScan={getNetworkScan}/>
            </div>
            <div ref={panelRef} className={`network-scanner-container ${isScanned ? 'visible' : ''}`}>
                {isScanned && <NetworkScanner scanMetrics={scanMetrics}/>}
            </div>
        </section>
    )
}

export default Dashboard;