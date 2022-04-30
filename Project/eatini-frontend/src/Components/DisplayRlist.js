import { type } from "@testing-library/user-event/dist/type";
import { useState } from "react";
import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';

const DisplayRlist = () => {
  const [restaurants, setRestaurants] = useState([
    { title: 'Bagel', type: 'bagel shop', rating: '3.3', acost: '$', location: '809 S', website: 'einsteinbros.com', fromtot: '11', fromtom: '0.5', totot: '12', totom: '1.0'},
    { title: 'Expresso', type: 'coffee shop', rating: '5.0', acost: '$', location: '1402 W', website: 'places.singlplatform.com', fromtot: '3', fromtom: '0.1', totot: '4', totom: '0.2'},
  ])

  return (
    <div className="displayrlist">
      {restaurants.map(restaurant => (
        <div style={{ display: 'block', width:"400", padding: 20 }}>
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
                backgroundColor: 'lightyellow',
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