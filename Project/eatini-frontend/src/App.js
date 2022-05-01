import React, {Component} from 'react';
import DisplayRlist from './Components/DisplayRlist';
import Form from './Components/FormComponents/Form';
import 'bootstrap/dist/css/bootstrap.css';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import { useState } from "react";

//import Logo from './Components/Logo';



class App extends Component {

constructor(props)  {
  super(props);
  this.setRestaurants = this.setRestaurants.bind(this);
  this.state = {restaurants:[]};
}
setRestaurants(newrest) {
  this.setState({restaurants: newrest})
}
  // const [restaurants, setRestaurants] = useState([
  //   { title: 'Expresso Royale', type: 'Coffee Shop', rating: '5.0', acost: '$', location: '1402 W Gregory Dr, Urbana, IL 61801', website: 'http://places.singleplatform.com/', fromtot: '3', fromtom: '0.1', totot: '4', totom: '0.2'},
  //   { title: 'Array Cafe', type: 'Cafe', rating: '3.3', acost: '$', location: '1206 W Gregory Dr, Urbana, IL 61801', website: 'http://igb.illinois.edu/', fromtot: '5', fromtom: '0.3', totot: '6', totom: '0.5'},
  //   { title: 'Satrbucks', type: 'Cafe', rating: '3.3', acost: '$', location: '809 S Wright St, Champaign, IL 61820', website: 'starbucks.com', fromtot: '9', fromtom: '0.5', totot: '10', totom: '1.0'},
  //   { title: 'Einstein Bros. Bagels', type: 'Bagel Shop', rating: '3.3', acost: '$', location: '1401 W Green St, Urbana, IL 61801', website: 'einsteinbros.com', fromtot: '11', fromtom: '0.5', totot: '12', totom: '1.0'}, 
  // ]);
render() {
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
            <Form setRestaurants={this.setRestaurants}/>
            {/* <div className="content">
              <hi></hi>
            </div> */}
          </Col>
          <Col style= {{
            width: "900",
            backgroundColor: 'lemonchiffon',
          }}>
          <h4>🌟 Restaurant Reccomendation For You 🌟</h4>
          <DisplayRlist restaurants={this.state.restaurants}/>
          </Col>
        </Row>
      </div>
    </div>
  );
 }
}

export default App;