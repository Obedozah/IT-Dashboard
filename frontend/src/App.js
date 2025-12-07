import './App.css';
import './components/header/Header';
import './components/footer/Footer';
import './components/dashboard/Dashboard';

function App() {
    return (
        <div className="App">
            <header>
                <Header/>
            </header>

            <body>
                <Dashboard/>
            </body>

            <footer>
                <Footer/>
            </footer>
        </div>
    );
}

export default App;
