import React from 'react';
import DisplayRlist from './Components/DisplayRlist';
import Rlist from "./Components/Rlist";


function App() {
  return (
    <div className="App">
      <div className = "content">
        {/* <Rlist title="name"></Rlist>
        <Rlist typeOfR="type"></Rlist> */}
        <DisplayRlist />
      </div>
    </div>
  );
}

export default App;