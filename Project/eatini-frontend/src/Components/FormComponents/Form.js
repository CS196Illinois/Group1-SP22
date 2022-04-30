import React from "react";
import './App.css';
import DisplayRlist from "../DisplayRlist";

const Form = () => {
    return (
        <div className="create">
            <form>
                <label>From:</label>
                <input
                    type="text"
                    required
                />
                <label>To:</label>
                <input
                    type="text"
                    required
                />
                <label>Start Time:</label>
                <input
                    type="text"
                    required
                />
                <label>End Time:</label>
                <input
                    type="text"
                    required
                />
                <label>Eating Time (minutes):</label>
                <input
                    type="text"
                    required
                />
                <label>Cuisine:</label>
                <select>
                    <option value=""></option>
                </select>
                <label>Price</label>
                <select>
                    <option value=""></option>
                </select>
                <button>Find Restaurants!</button>
            </form>
        </div>

    )
}

export default Form;