import { useEffect, useState } from 'react';
import './MetaData.css';

function MetaData() {
    const [data, setData] = useState(null);

    useEffect(() => {
        async function getDeviceData() {
            try {
                const response = await fetch('http://127.0.0.1:5000/device');
                const jsonData = await response.json();
                setData(jsonData);
                console.log(jsonData);
            } catch (err) {
                console.log(err);
            }
        }

        getDeviceData();
    }, []);

    return (
        <pre>{data ? JSON.stringify(data, null, 2) : 'Loading...'}</pre>
    );
}

export default MetaData;
