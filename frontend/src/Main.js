import React, {useState} from "react";
import {Link} from "react-router-dom";

const Main = () => {
    const [chargeMass, setChargeMass] = useState('');
    const [takeoffTime, setTakeoffTime] = useState('');
    const [takeoffDistance, setTakeoffDistance] = useState('');
    const [massToDestroy, setMassToDestroy] = useState('');
    const [resultsHTML, setResultsHTML] = useState(<div></div>);
    const [error, setError] = useState('');
    const backend_path = 'http://127.0.0.1:8000';
    let backend_functions;
    backend_functions = {
        "takeoff_time": setTakeoffTime,
        "takeoff_distance": setTakeoffDistance,
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        setError("")
        const url = `${backend_path}/mass_to_destroy?charge_mass_kg=${chargeMass}`;
        fetch(url)
            .then(
                response => {
                    // check for 400 error code
                    if (response.status === 400) {
                        response.json().then(data => {
                            setError(data["message"]);
                        });
                        return;
                    }
                    response.json().then(data => {
                        setMassToDestroy(data)
                    });
                }
            )
        .catch(error => {
            setError(error.message);
        });
        if (massToDestroy > 0) {
            createResultsHTML();
            return;
        }
        for (const [function_name, result_setter] of Object.entries(backend_functions)) {
            const url = `${backend_path}/${function_name}?charge_mass_kg=${chargeMass}`;
            fetch(url)
                .then(response => {
                    // check for 400 error code
                    if (response.status === 400) {
                        response.json().then(data => {
                            setError(data["message"]);
                        });
                        return;
                    }
                    response.json()
                        .then(data => {
                            result_setter(data);
                        })
                        .catch(error => {
                            setError(error.message);
                        })
                })
            }
        createResultsHTML()
    }

    const createResultsHTML = () => {
        let result;
        if (massToDestroy === undefined || massToDestroy === null || massToDestroy === 0) {
            result =
                <div>
                    {takeoffTime && <div>Takeoff Time: {takeoffTime} seconds </div>}
                    {takeoffDistance && <div>Takeoff Distance: {takeoffDistance} meters</div>}
                </div>;
        } else {
            result =
                <div>
                    {massToDestroy && <div>You need to destroy: {massToDestroy} kg in order to takeoff in time.</div>}
                </div>;
        }
        setResultsHTML(result);
    }

    return (
        <div>
            <h1>Charge Mass Calculator</h1>
            <p>
                Enter the mass of the charge in kilograms.
                If you can take off in time, the calculator will return
                the takeoff time and takeoff distance.
                If you cannot take off in time, the calculator will return the mass of the charge you need to destroy
                in order to take off in time.
            </p>
            <form onSubmit={handleSubmit}>
                <label>
                    Charge Mass (in kg):
                    <input type="number" value={chargeMass} min={0} onChange={e => setChargeMass(e.target.value)}/>
                </label>
                <button type="submit">Submit</button>
            </form>
            {error && <div>{error}</div>}
            {resultsHTML}
        </div>
    );

}

export default Main;