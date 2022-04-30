import { type } from "@testing-library/user-event/dist/type";
import { useState } from "react";
import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';

const DisplayRlist = () => {
  const [restaurants, setRestaurants] = useState([
    { title: 'Expresso Royale', type: 'Coffee Shop', rating: '5.0', acost: '$', location: '1402 W Gregory Dr, Urbana, IL 61801', website: 'http://places.singleplatform.com/', fromtot: '3', fromtom: '0.1', totot: '4', totom: '0.2'},
    { title: 'Array Cafe', type: 'Cafe', rating: '3.3', acost: '$', location: '1206 W Gregory Dr, Urbana, IL 61801', website: 'http://igb.illinois.edu/', fromtot: '5', fromtom: '0.3', totot: '6', totom: '0.5'},
    { title: 'Satrbucks', type: 'Cafe', rating: '3.3', acost: '$', location: '809 S Wright St, Champaign, IL 61820', website: 'starbucks.com', fromtot: '9', fromtom: '0.5', totot: '10', totom: '1.0'},
    { title: 'Einstein Bros. Bagels', type: 'Bagel Shop', rating: '3.3', acost: '$', location: '1401 W Green St, Urbana, IL 61801', website: 'einsteinbros.com', fromtot: '11', fromtom: '0.5', totot: '12', totom: '1.0'}, 
  ]);


//   useEffect(() => {
//       console.log('use effect ran');
//       console.log(restaurants);
//   }, []);

  return (
    <div className="displayrlist">
      {restaurants.map(restaurant => (
        <div style={{ display: 'block', width:"900", padding: 20 }}>
            <Row>
                <Col style={{
                width: "900",
                padding: 20,
                backgroundColor: 'pink',
                }}>
                { restaurant.title }
            </Col>
            </Row>

            <Row>
                <Col style={{
                width: "200",
                backgroundColor: 'lightcyan',
                }}>
                { restaurant.type }
            </Col>
                <Col style={{
                width: "500",
                backgroundColor: 'HoneyDew',
                }}>
                { restaurant.rating }
            </Col>
                <Col style={{
                width: "500",
                backgroundColor: 'lavender',
                }}>
                { restaurant.acost }
            </Col>
            </Row>

            <Row>
                <Col style={{
                width: "500",
                backgroundColor: 'LightSalmon',
                }}>
                🔻 Location: { restaurant.location }
                </Col>
            </Row>

            <Row>
                <Col style={{
                width: "500",
                backgroundColor: 'lavenderblush',
                }}>
                📋 Webiste: { restaurant.website }
                </Col>
            </Row> 

            <Row>
                <Col style={{
                width: "500",
                backgroundColor: 'lightyellow',
                }}>
                ⏰ From To: { restaurant.fromtot } min, { restaurant.fromtom } mile
                </Col>
            </Row>

            <Row>
                <Col style={{
                width: "500",
                backgroundColor: 'lightyellow',
                }}>
                ⏰ To To: { restaurant.totot } min, { restaurant.totom } mile
                </Col>
            </Row>

        </div>
        ))}
    </div>
  );
}
 
export default DisplayRlist;