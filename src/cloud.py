import os
from google.cloud import storage
from google.api_core.exceptions import NotFound

BUCKET_NAME = "stored-configuration-files"

CREDENTIALS_JSON = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "credentials.json"
)


def upload_to_bucket(
    path_to_file: str, blob_name: str = "configuration-file.json"
) -> str:
    storage_client = storage.Client.from_service_account_json(CREDENTIALS_JSON)
    try:
        # Looking for the bucket
        bucket = storage_client.get_bucket(BUCKET_NAME)
    except NotFound:
        # If not found then, create new
        bucket = storage_client.create_bucket(BUCKET_NAME)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)

    return blob.public_url


def get_from_bucket(blob_name: str = "configuration-file.json") -> str:
    storage_client = storage.Client.from_service_account_json(CREDENTIALS_JSON)
    bucket = storage_client.get_bucket(BUCKET_NAME)
    blob = bucket.get_blob(blob_name)
    return blob.public_url
