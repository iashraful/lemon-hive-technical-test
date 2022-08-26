from urllib import response
import pytest
from main import app as flask_app

TEST_DATA = {
    "firstName": "Mr",
    "secondName": "X",
    "ageInYears": 28,
    "address": "Dhaka, Bangladesh",
    "creditScore": 99.25,
}


@pytest.fixture()
def app():
    # Setups here
    flask_app.config.update({"TESTING": True})
    # More configs goes here

    yield flask_app

    # Finally Clean up the setups
    flask_app.config.update({"TESTING": False})


@pytest.fixture()
def client(app):
    return app.test_client()


def test_get_config(client, mocker):
    mocker.patch("src.services.get_from_bucket", return_value=TEST_DATA)
    response = client.get("/config")
    assert response.status_code == 200
    assert response.json["data"] == TEST_DATA


def test_post_config(client, mocker):
    mocker.patch("src.services.upload_to_bucket", return_value=True)
    response = client.post("/config", json=TEST_DATA)
    assert response.status_code == 200
