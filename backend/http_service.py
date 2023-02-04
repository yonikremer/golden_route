"""an HTTP server that allows you to use the pysics calculator in the business_logic.py file"""
from typing import Union

import fastapi
from fastapi.middleware.cors import CORSMiddleware

from business_logic import (
    calculate_acceleration,
    calculate_takeoff_distance,
    calculate_takeoff_time,
    ChargeMassErrorTooBig,
    calculate_mass_to_destroy
)

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

NumberType = Union[int, float]


@app.get("/acceleration")
@app.get("/acceleration/{charge_mass_kg}")
def acceleration(charge_mass_kg: NumberType):
    """Calculate the acceleration of the plane with a given charge mass.
    Raises:
        InvalidChargeMass: if the charge mass is not a non-negative number."""
    try:
        return calculate_acceleration(charge_mass_kg)
    except ValueError as e:
        return fastapi.Response(status_code=400, content=str(e))


@app.get("/takeoff_time")
@app.get("/takeoff_time/{charge_mass_kg}")
def takeoff_time(charge_mass_kg: NumberType):
    """Gets the mass of the charge in kilograms (non-negative number).
    Calculate the time it takes to take off with the charge mass.
    Raises:
        ChargeMassErrorTooBig if the plane can't take off in MAX_TAKEOFF_TIME_SEC.
        InvalidChargeMass: if the charge mass is not a non-negative number."""
    try:
        return calculate_takeoff_time(charge_mass_kg)
    except ChargeMassErrorTooBig as e:
        return fastapi.Response(status_code=400, content=str(e))
    except ValueError as e:
        return fastapi.Response(status_code=400, content=str(e))


@app.get("/takeoff_distance")
@app.get("/takeoff_distance/{charge_mass_kg}")
def takeoff_distance(charge_mass_kg: NumberType):
    """Gets the mass of the charge in kilograms (non-negative number).
        Calculate the distance it takes to take off with a given charge mass.
        raises ValueError if the plane can't take off in MAX_TAKEOFF_TIME_SEC.
        Raises:
            ChargeMassErrorTooBig: if the plane can't take off in MAX_TAKEOFF_TIME_SEC.
            InvalidChargeMass: if the charge mass is not a non-negative number.
        """
    try:
        return calculate_takeoff_distance(charge_mass_kg)
    except ValueError as e:
        return fastapi.Response(status_code=400, content=str(e))


@app.get("/mass_to_destroy")
@app.get("/mass_to_destroy/{charge_mass_kg}")
def mass_to_destroy(charge_mass_kg: NumberType):
    """Gets the mass of the charge in kilograms (non-negative number).
    If the plane can take off in time,
    You don't need to destroy any charge, so the function returns 0.
    Else, the function returns the mass of the charge that you need to destroy
     in order to take off in time.
     Raises:
         InvalidChargeMass: if the charge mass is not a non-negative number."""
    try:
        return calculate_mass_to_destroy(charge_mass_kg)
    except ValueError as e:
        return fastapi.Response(status_code=400, content=str(e))
