import requests
import pytest

def test_my_website():
    # Send a GET request to the website
    response = requests.get("http://54.241.214.169:5000/")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response body contains a specific string indicating the website has loaded
    assert "Hello, World!" in response.text

if __name__ == "__main__":
    pytest.main()
