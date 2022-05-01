import React from "react";
import './App.css';
import DisplayRlist from "../DisplayRlist";
import { useState } from "react";
import { props } from "bluebird";
class Form extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            from: '',
            To: '',
            StartTime: '',
            EndTime: '',
            EatingTime: '',
            Cuisine: '',
            Price: ''


        };
        console.log(this.state)
        this.handleFromChange = this.handleFromChange.bind(this);
        this.handleToChange = this.handleToChange.bind(this);
        this.handleStartTimeChange = this.handleStartTimeChange.bind(this);
        this.handleEndTimeChange = this.handleEndTimeChange.bind(this);
        this.handleEatingTimeChange = this.handleEatingTimeChange.bind(this);
        this.handleCuisineChange = this.handleCuisineChange.bind(this);
        this.handlePriceChange = this.handlePriceChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }

    async handleSubmit(e) {
        e.preventDefault()
        console.log(this.state);

        const requestOptions = {
            method: 'POST',
            headers: {'Content-Type' : 'application/json'},
            mode: 'cors',
            body: JSON.stringify({
                radius: "2000",
                rating: "1.0",
                keyword: this.state.Cuisine,
                timeinfo: {
                    currentloc: this.state.from,
                    destloc: this.state.To,
                    eatingtime: this.state.EatingTime,
                    starttime: "0",
                    endtime: this.state.EndTime
            }

            })
        };
        console.log(requestOptions);

        const responseData = await fetch(' http://127.0.0.1:5000/restaurant', requestOptions)
        // .then(response=>response.json())
        .then(function(response) { 
            // console.log(response.json())
            var data = response.json();
            return data
            // console.log(data)
        }).then(function(parsedData) {
            console.log(parsedData)
            return parsedData
        })
        console.log(responseData)
        this.props.setRestaurants(responseData)
        

    }

    handleFromChange(e) {
        e.preventDefault()
        console.log('handle change');
        this.setState({
           from: e.target.value,
        });
    }
    
    handleToChange(e) {
        e.preventDefault()
        console.log('handle change');
        this.setState({
            To: e.target.value,
        });
    }    
    handleStartTimeChange(e) {
        e.preventDefault()
        console.log('handle change');
        this.setState({        
            StartTime: e.target.value,
        });
    }
    handleEndTimeChange(e) {
        e.preventDefault()
        console.log('handle change');
        this.setState({            
            EndTime: e.target.value,
        });
    }    
    handleEatingTimeChange(e) {
        e.preventDefault()
        console.log('handle change');
        this.setState({               
            EatingTime: e.target.value,
        });
        console.log(this.state);
    }
    handleCuisineChange(e) {
        e.preventDefault()
        console.log('handle change')
        this.setState({
            Cuisine: e.target.Cuisine,
        });
    }
         
    handlePriceChange(e) {
        e.preventDefault()
        console.log('handle change')
        this.setState({
            Price: e.target.Price
        });
        console.log(e.target.from);
        console.log(e.target.value);
        console.log(this.state);

    }

   
        //     const form = {}

        //     setIsPending(true)

        //     fetch('/restaurants')
        //     method: 'GET',
        //     headers: { "Content-Type" : "application-json"},
        //     body: JSON.stringify(form)
        // }).then(() => {
        //     console.log('form submitted');

        //});
    // }
    render() {

        return (
            <div className="create">
                <form onSubmit={this.handleSubmit}>
                    <label>From:
                        <input
                            type="text"
                            required
                            from={this.state.from}
                            onChange={this.handleFromChange}
                        />
                    </label>
                    <label>To:</label>
                    <input
                        type="text"
                        required
                        value={this.state.To}
                        onChange={this.handleToChange}
                    />
                    {/* <label>Start Time:</label>
                    <input
                        type="text"
                        required
                        value={this.state.StartTime}
                        onChange={this.handleStartTimeChange}
                    /> */}
                    <label>Total time (minutes):</label>
                    <input
                        type="text"
                        required
                        value={this.state.EndTime}
                        onChange={this.handleEndTimeChange}
                    />
                    <label>Eating Time (minutes):</label>
                    <input
                        type="text"
                        required
                        value={this.state.EatingTime}
                        onChange={this.handleEatingTimeChange}
                    />
                    {/* <label>Cuisine:</label>
                    <input
                        type="text"
                        value={this.state.Cuisine}
                        onChange={this.handleCuisineChange}
                    /> */}
                    {/* <label>Price</label> */}
                    {/* <select>
                        <option value=""></option>
                        value={this.state.Price}
                        onChange={this.handlePriceChange}
                    </select> */}
                    <button type="submit">Find Restaurants!</button>
                </form>
            </div>

        )
    }
}
export default Form;