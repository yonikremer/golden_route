"""A test file that runs the HTTP service and tests it with HTTP requests."""
from numbers import Real
from typing import Iterable, Any

import pytest
from fastapi.testclient import TestClient

from backend.business_logic import (
    maximal_charge_mass,
    calculate_takeoff_time,
    calculate_takeoff_distance,
    calculate_mass_to_destroy,
)
from backend.http_service import app


function_names: Iterable[str] = ("takeoff_time", "takeoff_distance", "mass_to_destroy")
function_name_to_function = {
    "takeoff_time": calculate_takeoff_time,
    "takeoff_distance": calculate_takeoff_distance,
    "mass_to_destroy": calculate_mass_to_destroy,
}
client = TestClient(app)


def get_valid_charge_masses() -> Iterable[Real]:
    yield 0
    yield 1
    yield 1.99
    yield 55.55555555
    yield 1 + 1e-6


def get_invalid_charge_masses() -> Iterable[Any]:
    yield -1
    yield -1.99
    yield -1000000000000000
    yield -55.55555555
    yield -1 - 1e-6
    yield "a"
    yield None
    yield True
    yield False
    yield []


@pytest.mark.parametrize("charge_mass", get_invalid_charge_masses())
def test_bad_requests(charge_mass):
    """Tests that the service returns a 400 error for invalid charge masses."""
    for function in function_names:
        response = client.get(f"/{function}/{charge_mass}")
        assert 400 <= response.status_code <= 499


def test_charge_mass_too_big():
    big_charge_mass = maximal_charge_mass + 1
    for stat_function in ("takeoff_time", "takeoff_distance"):
        response = client.get(f"/{stat_function}/{big_charge_mass}")
        assert response.status_code == 400
        assert "The charge mass is too big." in response.text

    response = client.get(f"/mass_to_destroy/{big_charge_mass}")
    assert response.status_code == 200
    assert response.json() == 1


@pytest.mark.parametrize("charge_mass", get_valid_charge_masses())
def test_backend_business_logic_correlation(charge_mass: Real):
    for function_name, function in function_name_to_function.items():
        for charge_mass in get_valid_charge_masses():
            response = client.get(f"/{function_name}/{charge_mass}")
            assert response.status_code == 200
            assert response.json() == function(charge_mass)


if __name__ == "__main__":
    pytest.main()
