import json
import os

from google.api_core.exceptions import NotFound
from google.cloud import storage

BUCKET_NAME = "stored-configuration-files"

CREDENTIALS_JSON = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "credentials.json"
)


def upload_to_bucket(contents: str, blob_name) -> str:
    # Creating storage client from the credentials.
    storage_client = storage.Client.from_service_account_json(CREDENTIALS_JSON)
    try:
        # Looking for the bucket
        bucket = storage_client.get_bucket(BUCKET_NAME)
    except NotFound:
        # If not found then, create new
        bucket = storage_client.create_bucket(BUCKET_NAME)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(contents)
    return blob.public_url


def get_from_bucket(blob_name) -> dict:
    storage_client = storage.Client.from_service_account_json(CREDENTIALS_JSON)
    # Get the bucket from the storage
    bucket = storage_client.get_bucket(BUCKET_NAME)
    blob = bucket.get_blob(blob_name)
    # Making json/dict from the blob
    data: dict = json.loads(blob.download_as_text(encoding="utf-8"))
    return data
