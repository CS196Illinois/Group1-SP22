import React from 'react';
import DisplayRlist from './Components/DisplayRlist';
import Form from './Components/FormComponents/Form';
import 'bootstrap/dist/css/bootstrap.css';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
//import Logo from './Components/Logo';


function App() {
  return (
    <div className="App">
      <div className = "content">
        {/* <Rlist title="name"></Rlist>
        <Rlist typeOfR="type"></Rlist> */}
        {/* <h4>🌟 You can consider about going to these restaurants 🌟</h4>
        <DisplayRlist /> */}

        <Row>
          <Col style= {{
            width: "50",
            backgroundColor: 'lavenderblush',
          }}>
            <h4>🗒 Your Schedule 🗒</h4>
            <Form />
            {/* <div className="content">
              <hi></hi>
            </div> */}
          </Col>
          <Col style= {{
            width: "900",
            backgroundColor: 'lemonchiffon',
          }}>
          <h4>🌟 Restaurant Reccomendation For You 🌟</h4>
          <DisplayRlist />
          </Col>
        </Row>
      </div>
    </div>
  );
}

export default App;