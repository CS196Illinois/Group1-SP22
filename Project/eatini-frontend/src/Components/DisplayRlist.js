import { type } from "@testing-library/user-event/dist/type";
import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';

class DisplayRlist extends React.Component {

    constructor(props) {
        super(props);
        this.restaurant = props.restaurants;
    }




//   useEffect(() => {
//       console.log('use effect ran');
//       console.log(restaurants);
//   }, []);

render() {
  return (
    <div>
      {this.props.restaurants.map(restaurant => (
        <div style={{ display: 'block', width:"900", padding: 20 }}>
            <Row>
                <Col style={{
                width: "900",
                padding: 20,
                backgroundColor: 'pink',
                }}>
                { restaurant.name }
            </Col>
            </Row>

            <Row>
            {/* <Col style={{
                width: "200",
                backgroundColor: 'lightcyan',
                }}>
                { restaurant.type }
            </Col> */}
                <Col style={{
                width: "500",
                backgroundColor: 'HoneyDew',
                }}>
                ⭐️ Rating: { restaurant.rating }
            </Col>
                <Col style={{
                width: "500",
                backgroundColor: 'lavender',
                }}>
                💰 Average Price: { restaurant.price_level }
            </Col>
            </Row>

            <Row>
                <Col style={{
                width: "500",
                backgroundColor: 'LightSalmon',
                }}>
                🔻 Location: { restaurant.vicinity }
                </Col>
            </Row>

            {/* <Row>
                <Col style={{
                width: "500",
                backgroundColor: 'lavenderblush',
                }}>
                📋 Webiste: { restaurant.website }
                </Col>
            </Row>  */}

            <Row>
                <Col style={{
                width: "500",
                backgroundColor: 'lightyellow',
                }}>
                ⏰ To Restaurant: { restaurant.ToResTime } min
                </Col>
            </Row>

            <Row>
                <Col style={{
                width: "500",
                backgroundColor: 'lightyellow',
                }}>
                ⏰ From Restaurant: { restaurant.ToDesTime } min
                </Col>
            </Row>

        </div>
        ))}
    </div>
  );
 }
}
 
export default DisplayRlist;