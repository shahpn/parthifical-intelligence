import React, { useState, useEffect } from 'react'
import NavBar from "./components/navbar"
import Container from "./components/container"
import Footer from "./components/footer"

import './App.css'


function App() {
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch('/wishMe').then(
      data => {
        setData(data)
        console.log(data)
      }
      
    )
  }, [])

  // async function loadGames() {
  //   const response = await fetch('/wishMe');
  //   // fetch() timeouts at 300 seconds in Chrome
  //   const games = await response.json();
  //   return games;
  // }

  // loadGames()

  return(
    <div className="App">
      <NavBar />
      <Container />
      <Footer />
    </div>
  );
}

export default App