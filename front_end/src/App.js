import React, { useState } from 'react';

const App = () => {
  const [chargeMass, setChargeMass] = useState('');
  const [acceleration, setAcceleration] = useState('');
  const [takeoffTime, setTakeoffTime] = useState('');
  const [takeoffDistance, setTakeoffDistance] = useState('');
  const [massToDestroy, setMassToDestroy] = useState('');
  const [resultsHTML, setResultsHTML] = useState(<div></div>);
  const [error, setError] = useState('');
  const backend_path = 'http://127.0.0.1:8000';
    let backend_functions;
    backend_functions = {
        "acceleration": setAcceleration,
        "mass_to_destroy": setMassToDestroy,
        "takeoff_time": setTakeoffTime,
        "takeoff_distance": setTakeoffDistance,
    };

  const handleSubmit = (event) => {
    event.preventDefault();
    setError("")
    for (const [function_name, result_setter] of Object.entries(backend_functions)) {
        const url = `${backend_path}/${function_name}?charge_mass_kg=${chargeMass}`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                result_setter(data);
            })
            .catch(error => {
                console.log(error)
                setError(error.message);
            })
    }
    createResultsHTML()
  }

  const createResultsHTML = () => {
      let result;
      if (massToDestroy === undefined || massToDestroy === null || massToDestroy === 0) {
          console.log("massToDestroy is " + massToDestroy);
          console.log("type off massToDestroy is " + typeof massToDestroy);
          result =
              <div>
                {acceleration && <div>Acceleration: {acceleration} meters/seconds^2</div>}
                {takeoffTime && <div>Takeoff Time: {takeoffTime} seconds </div>}
                {takeoffDistance && <div>Takeoff Distance: {takeoffDistance} meters</div>}
              </div>;
      }
      else {
          result =
              <div>
                {massToDestroy && <div>You need to destroy: {massToDestroy} kg in order to takeoff in time.</div>}
              </div>;
      }
      setResultsHTML(result);
  }

  return (
      <div>
          <form onSubmit={handleSubmit}>
              <label>
                 Charge Mass (in kg):
                <input type="number" value={chargeMass} min={0} onChange={e => setChargeMass(e.target.value)} />
              </label>
              <button type="submit">Submit</button>
          </form>
          {error && <div>{error}</div>}
          {resultsHTML}
      </div>
  );
}

export default App;
