import React, { useState, useEffect } from 'react'
import NavBar from "./components/navbar"
import Container from "./components/container"
import Footer from "./components/footer"

import './App.css'


function App() {
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch('/username').then(
      data => {
        setData(data)
        console.log(data)
      }
      
    )
  }, [])

  return(
    <div className="App">
      <NavBar />
      <Container />
      <Footer />
    </div>
  );
}

export default App