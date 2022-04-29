import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';

// title
var Rtitle = "title";

// type
var Rtype = "type";

//rating
var Rrating = "rating";

// average cost
var Racost = "cost";

// location
var Rloc = "location";

// website
var Rweb = "url";

// from-to, need tostring or something else to turn int to string
var FromToT = "time";
var FromToM = "dis";

// to-to, need tostring or something else to turn int to string
var ToToT = "time";
var ToToM = "dis";

export default function Test() {
    return (
      <div style={{ display: 'block', width:"400", padding: 20 }}>
        <h4>React-Bootstrap Col Component</h4>
        <Row>
          <Col style={{
            width: "900",
            padding: 20,
            backgroundColor: 'pink',
          }}>
            <Rtitle /> 
            title/name
        </Col>
        </Row>

        <Row>
          <Col style={{
            width: "200",
            backgroundColor: 'lightblue',
          }}>
            <Rtype />
            type
        </Col>
          <Col style={{
            width: "500",
            backgroundColor: 'lightgreen',
          }}>
            <Rrating />
            rating
        </Col>
          <Col style={{
            width: "500",
            backgroundColor: 'violet',
          }}>
            <Racost />
            average cost
        </Col>
        </Row>

        <Row>
          <Col style={{
            width: "500",
            backgroundColor: 'orange',
          }}>
            🔻 Location: <Rloc />
          </Col>
        </Row>

        <Row>
          <Col style={{
            width: "500",
            backgroundColor: 'lightyellow',
          }}>
            📋 Webiste: <Rweb />
          </Col>
        </Row> 

        <Row>
          <Col style={{
            width: "500",
            backgroundColor: 'lightyellow',
          }}>
            ⏰ From To: <FromToM /> min, <FromToM /> mile
          </Col>
        </Row>

        <Row>
          <Col style={{
            width: "500",
            backgroundColor: 'lightyellow',
          }}>
            ⏰ To To: <FromToM /> min, <FromToM /> mile
          </Col>
        </Row>

      </div>
    );
        }

// const Rlist = () => {
//     return (

//         <Container>
//             <Row>
//                 <Col> {props.title}</Col>
//             </Row>
//         </Container>
//     );
// }

// export default function Rlist(props) {
//     return (
// <div>
//     {props.title}
//     {props.typeOfR}
//     {props.rating}
//     {props.averageCost}
//     {props.Location}
//     {props.Wbesite}
//     {props.fromTo}
//     {props.ToTo}
// </div>
//     );
// };