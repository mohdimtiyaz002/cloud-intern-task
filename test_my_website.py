import requests
import pytest

def test_my_website():
    # Send a GET request to the website
    response = requests.get("http://18.144.80.230:8080/")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response body contains a specific string indicating the website has loaded
    assert "Hello, World!" in response.text

if __name__ == "__main__":
    pytest.main()
