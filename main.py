from flask import Flask, request

from src.response import JSONResponse
from src.services import ConfigurationFileService

app = Flask(__name__)


@app.route("/config", methods=["GET", "POST"])
def upload_download_config():
    try:
        if request.method == "POST":
            # If the request is post then upload the file
            return ConfigurationFileService.upload_configuration_file_to_cloud(
                data=request.json
            )
        else:
            # Otherwise download the file
            return ConfigurationFileService.download_configuration_file_from_cloud()
    except Exception:
        return JSONResponse(
            data={"message": "Server Failure", "status": "500"},
            status=500,
        )
