import './NetworkScanner.css';
import MetaData from './panels/MetaData';
import ScannedDevices from './panels/ScannedDevices';

function NetworkScanner({scanMetrics}) {

    return (
        <section className="network-scanner-content">
            <div className="meta-data">
                <MetaData metaData={scanMetrics.meta_data}/>
            </div>
            <div className="scanned-devices-component">
                <ScannedDevices scanMetrics={scanMetrics.arp_sweep_data}/>
            </div>    
        </section>
    )
}

export default NetworkScanner;