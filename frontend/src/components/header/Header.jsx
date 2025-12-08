import './Header.css'

function Header() {
    return (
        <section className="header">
            <div className="left-header">
                <img className="logo" src="./favicon.png" alt="Logo"></img>
                <h1>IT Dashboard</h1>
            </div>
            <div className="right-header">
                <h1>Avery Lopez</h1>
            </div>
        </section>
    )
}
export default Header;