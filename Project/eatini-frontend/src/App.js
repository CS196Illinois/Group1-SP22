import eatinilogo from "./eatinilogo.jpg";
import './App.css';
import React from 'react';

function App() {
  return (
    <div className="App">
      <div className = "content">
        <h1>App Comp</h1>
        <img src={eatinilogo} alt="eatinilogo" />
      </div>
    </div>
  );
}

export default App;
