import io
import json

from google.api_core.exceptions import Forbidden, NotFound
from pydantic import ValidationError

from src.cloud import get_from_bucket, upload_to_bucket

from .response import JSONResponse
from .schema import ConfigurationSchema


class ConfigurationFileService:
    @staticmethod
    def upload_configuration_file_to_cloud(data: dict) -> JSONResponse:
        try:
            # Making schema to verify the data provided from the request
            schema = ConfigurationSchema(**data)
            # Making the in memory file
            m_file = io.StringIO(json.dumps(schema.dict()))
            # Passing the file contents to the bucket upload function
            uploaded: bool = upload_to_bucket(
                contents=m_file.read(), blob_name="configuration-file.json"
            )
            if uploaded:
                return JSONResponse(
                    data={
                        "message": "Configuration file uploaded successfully.",
                        "status": "200",
                    },
                    status=200,
                )
            return JSONResponse(
                data={
                    "message": "An unknown error has occurred.",
                    "status": "500",
                },
                status=500,
            )
        except ValidationError as err:
            # In case of verification failed
            return JSONResponse(
                data={
                    "message": "Data validation failed.",
                    "errors": err.errors(),
                    "status": 400,
                },
                status=400,
            )
        except NotFound:
            # When the bucket is not present on the cloud storage
            return JSONResponse(
                data={"message": "Bucket Not Found", "status": "404"},
                status=404,
            )
        except Forbidden:
            # When there is an error related to access.
            return JSONResponse(
                data={"message": "Access forbidden", "status": "403"},
                status=403,
            )

    @staticmethod
    def download_configuration_file_from_cloud() -> JSONResponse:
        try:
            data: dict = get_from_bucket(blob_name="configuration-file.json")
            return JSONResponse(
                data={
                    "message": "Configuration file fetched successfully.",
                    "status": "200",
                    # Agin cross checking the validation here.
                    "data": ConfigurationSchema(**data).dict(),
                },
                status=200,
            )
        except ValidationError as err:
            # In case of verification failed
            return JSONResponse(
                data={
                    "message": "Data validation failed.",
                    "errors": err.errors(),
                    "status": 400,
                },
                status=400,
            )
        except NotFound:
            return JSONResponse(
                data={"message": "File Not Found", "status": "404"},
                status=404,
            )
        except Forbidden:
            # When there is an error related to access.
            return JSONResponse(
                data={"message": "Access forbidden", "status": "403"},
                status=403,
            )
