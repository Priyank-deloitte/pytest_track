import pytest
import requests


@pytest.mark.parametrize("page, size", [(0, 10), (1, 5), (2, 3)])
def test_fetch_passenger_details(page, size):
    base_url = "https://api.instantwebtools.net/v1/passenger"
    params = {"page": page, "size": size}

    response = requests.get(base_url, params=params)
    assert response.status_code == 200

    passenger_data = response.json()
    assert len(passenger_data["data"]) == size
    # Additional assertions on the fetched passenger data can be performed here

    print(f"Passenger details fetched for page={page} and size={size}:")
    print(passenger_data)
