import io
import json
from src.cloud import upload_to_bucket, get_from_bucket

CONF_DATA = {
    "firstName": "Mr",
    "secondName": "X",
    "ageInYears": 28,
    "address": "Dhaka, Bangladesh",
    "creditScore": 99.25,
}


def test_upload_to_bucket(mocker):
    # "mocker" is a default fixure available from pytest-mock
    # Mocking the storage where it's imported or using.
    mocker.patch("src.cloud.storage")
    _contents = io.StringIO(json.dumps(CONF_DATA))
    uploaded = upload_to_bucket(contents=_contents, blob_name="configuration-file.json")
    assert uploaded


def test_download_from_bucket(mocker):
    mocker.patch("src.cloud.storage")
    # Here extra mocking the output result
    mocker.patch("tests.test_cloud_functions.get_from_bucket", return_value=CONF_DATA)
    data = get_from_bucket(blob_name="configuration-file.json")
    assert data == CONF_DATA
