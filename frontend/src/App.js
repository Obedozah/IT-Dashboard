import './App.css';
import Header from './components/header/Header';
import Dashboard from './components/dashboard/Dashboard';
import Footer from './components/footer/Footer';

function App() {
    return (
        <div className="App">
            <Header/>
            
            <Dashboard/>
            
            <Footer/>
        </div>
    );
}

export default App;
