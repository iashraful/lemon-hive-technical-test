import json
from typing import List, Union
from flask import Response


class JSONResponse(Response):
    def __init__(self, data: Union[List[dict], dict], status: int = 200):
        super(JSONResponse, self).__init__(
            response=json.dumps(data), content_type="application/json", status=status
        )
