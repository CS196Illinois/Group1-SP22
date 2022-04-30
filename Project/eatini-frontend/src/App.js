import React from 'react';
import DisplayRlist from './Components/DisplayRlist';
import Rlist from "./Components/Rlist";


function App() {
  return (
    <div className="App">
      <div className = "content">
        {/* <Rlist title="name"></Rlist>
        <Rlist typeOfR="type"></Rlist> */}
        <h4>🌟 You can consider about going to these restaurants 🌟</h4>
        <DisplayRlist />
      </div>
    </div>
  );
}

export default App;