import {useState} from "react";
import {Link} from 'react-router-dom';


const Weather = () => {
    const [date, setDate] = useState('');
    const [temperatures, setTemperatures] = useState([]);
    const [error, setError] = useState('');
    const [userMessage, setUserMessage] = useState('');
    const weather_api_path_base = 'https://api.open-meteo.com/v1/forecast';

    const latitude = 30;
    const longitude = 35;

    const minTemperature = 15;
    const maxTemperature = 30;

    const hours = [
        "00:00",
        "01:00",
        "02:00",
        "03:00",
        "04:00",
        "05:00",
        "06:00",
        "07:00",
        "08:00",
        "09:00",
        "10:00",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00",
        "16:00",
        "17:00",
        "18:00",
        "19:00",
        "20:00",
        "21:00",
        "22:00",
        "23:00"
    ]


    const handleSubmit = (event) => {
        setError("")
        event.preventDefault();
        // format the date to be in the format of YYYY-MM-DD
        const date_un_formatted = new Date(date);
        const date_formatted = date_un_formatted.toISOString().split('T')[0];
        const full_request_url = `${weather_api_path_base}?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m&start_date=${date_formatted}&end_date=${date_formatted}`;
        fetch(full_request_url)
            .then(
                response => {
                    // check for 400 error code
                    if (response.status === 400) {
                        response.json().then(data => {
                            setError(data["message"]);
                        });
                        setUserMessage("Your is probably not in the allowed range. Please try again with a closer date.");
                        return;
                    }
                    response.json().then(data => {
                        setTemperatures(data["hourly"]["temperature_2m"]);
                    });
                }
            )
            .catch(error => {
                setError("Error getting weather data");
            });
        const goodTakeOffTimes = hours.filter((time, index) => temperatures[index] >= minTemperature && temperatures[index] <= maxTemperature);
        if (goodTakeOffTimes.length === 0) {
            const minTemperature = Math.min(...temperatures);
            const maxTemperature = Math.max(...temperatures);
            setUserMessage("You can't take off in the selected date, " +
                "the temperatures in the selected date are between "
                + minTemperature + " and " + maxTemperature + " degrees Celsius."
                + "Which is not in the allowed range of " + minTemperature + " and "
                + maxTemperature + " degrees Celsius."
            );
        }
        else{
            setUserMessage("You can take off in the selected date at " + goodTakeOffTimes.join(', ') + ".");
        }
    }

    return (
        <div>
            <h1>Weather</h1>
            <p>
                Enter a date and get a message saying whether or your not the weather is good for a takeoff.

                If the weather is good, the message will also say at what time you can take off.
            </p>
            <Link to="/">Go to main page</Link>
            <form onSubmit={handleSubmit}>
                <label>
                    Date:
                    <input type="date" value={date} onChange={e => setDate(e.target.value)} />
                </label>
                <button type="submit">Submit</button>
            </form>
            {error && <div>{error}</div>}
            {userMessage && <div>{userMessage}</div>}
        </div>
    )

}
export default Weather;
