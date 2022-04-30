import React from 'react';
import DisplayRlist from './Components/DisplayRlist';
import Form from './Components/FormComponents/Form';
import 'bootstrap/dist/css/bootstrap.css';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';


function App() {
  return (
    <div className="App">
      <div className = "content">
        {/* <Rlist title="name"></Rlist>
        <Rlist typeOfR="type"></Rlist> */}
        {/* <h4>🌟 You can consider about going to these restaurants 🌟</h4>
        <DisplayRlist /> */}
        <Row>
          <Col>
            <Form />
            <div className="content">
              <hi></hi>
            </div>
          </Col>
        </ Row>
        <Row>
          <Col>
          <DisplayRlist />
          </Col>
        </Row>
      </div>
    </div>
  );
}

export default App;