import './NetworkScanner.css';
import MetaData from './panels/MetaData';
import ScannedDevices from './panels/ScannedDevices';

function NetworkScanner() {
    return (
        <section className="network-scanner">
            <div className="meta-data">
                <MetaData/>
            </div>
            <div className="scanned-devices">
                <ScannedDevices/>
            </div>    
        </section>
    )
}

export default NetworkScanner;