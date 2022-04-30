import './App.css'
import Navbar from './Navbar'

const Navbar = () => {
    return (
        <nav className="navbar">
            <h1>The Mojo bolg</h1>
            <div className="links">
            <a href="/">Home</a>
            <a href="/create">New Blog</a>
            </div>
        </nav>
    );
}
 
export default Navbar;