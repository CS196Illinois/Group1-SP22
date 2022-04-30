
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
                <label>Time Range:</label>
                <select>
                    <option value=""
                    required>
                </option>
                </select>
                <label>to</label>
                <select>
                    <option value=""></option>
                </select>
                <label>Preferred Eating Time:</label>
                <select>
                    <option value=""></option>
                </select>
                <label>minutes</label>
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