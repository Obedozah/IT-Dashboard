import {useState, useEffect} from 'react';
import './Dashboard.css';
import SystemMetrics from './sections/system-info/SystemMetrics';
import NetworkScanner from './sections/network-scanner/NetworkScanner';

function Dashboard() {

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
        <section className="dashboard">
            <div className="system-metrics">
                <SystemMetrics metrics={metrics}/>
            </div>
            <div className="network-scanner">
                <NetworkScanner/>
            </div>
        </section>
    )
}

export default Dashboard;