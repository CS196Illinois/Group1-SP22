import React from "react";
import './App.css';
import DisplayRlist from "../DisplayRlist";
import { useState } from "react";
class Form extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            value: '',
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
    handleSubmit(e) {
        console.log(this.state);
        e.preventDefault()

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
                    <label>Start Time:</label>
                    <input
                        type="text"
                        required
                        value={this.state.StartTime}
                        onChange={this.handleStartTimeChange}
                    />
                    <label>End Time:</label>
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
                    <label>Cuisine:</label>
                    <select>
                        <option value=""></option>
                        value={this.state.Cuisine}
                        onChange={this.handleCuisineChange}
                    </select>
                    <label>Price</label>
                    <select>
                        <option value=""></option>
                        value={this.state.Price}
                        onChange={this.handlePriceChange}
                    </select>
                    <button type="submit">Find Restaurants!</button>
                </form>
            </div>

        )
    }
}
export default Form;