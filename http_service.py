"""an HTTP server that allows you to use the pysics calculator in the business_logic.py file"""
import fastapi
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from business_logic import calculate_acceleration, calculate_takeoff_distance, calculate_takeoff_time, \
    ChargeMassErrorTooBig, calculate_mass_to_destroy

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/acceleration")
@app.get("/acceleration/{charge_mass_kg}")
def acceleration(charge_mass_kg: float):
    try:
        return calculate_acceleration(charge_mass_kg)
    except ValueError as e:
        return fastapi.Response(status_code=400, content=str(e))


@app.get("/takeoff_time")
@app.get("/takeoff_time/{charge_mass_kg}")
def takeoff_time(charge_mass_kg: float):
    try:
        return calculate_takeoff_time(charge_mass_kg)
    except ChargeMassErrorTooBig as e:
        return fastapi.Response(status_code=400, content=str(e))
    except ValueError as e:
        return fastapi.Response(status_code=400, content=str(e))


@app.get("/takeoff_distance")
@app.get("/takeoff_distance/{charge_mass_kg}")
def takeoff_distance(charge_mass_kg: float):
    try:
        return calculate_takeoff_distance(charge_mass_kg)
    except ValueError as e:
        return fastapi.Response(status_code=400, content=str(e))


@app.get("/mass_to_destroy")
@app.get("/mass_to_destroy/{charge_mass_kg}")
def mass_to_destroy(charge_mass_kg: float):
    try:
        return calculate_mass_to_destroy(charge_mass_kg)
    except ValueError as e:
        return fastapi.Response(status_code=400, content=str(e))


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
