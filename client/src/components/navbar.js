import Parth from "../assets/parth.png"

import { useState } from 'react';
import { useEffect } from 'react';

const Navbar = () => {
    
    const [theme, setTheme] = useState(false);

    const handleClick = () => {
      setTheme(!theme)
    }
  
    useEffect(() => {
      if (theme===true) {
        document.body.classList.add("light")
        document.body.classList.remove("dark")
      }
      else {
        document.body.classList.add("dark")
        document.body.classList.remove("light")
      }
    })


    return (
        <nav className="navbar">
            <header className="header">
                <input className="menu-btn" type="checkbox" id="menu-btn" />
                <label className="menu-icon" for="menu-btn"><span class="navicon"></span></label>
                <ul className="menu">
                    <li>
                        <div class="container">
                            <div class="switch">
                                <label for="toggle">
                                    <input id="toggle" class="toggle-switch" type="checkbox" onClick={handleClick}/>
                                    <div className="sun-moon"></div>
                                    <div className="background"/>
                                </label>
                            </div>
                        </div>
                    </li>
                </ul>
                <a href="/"><img id="logo" alt='logo' src={Parth}></img></a>
            </header>
        </nav>
      );
}
 
export default Navbar;