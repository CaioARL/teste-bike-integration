# -----------------------------
from pathlib import Path
dirProject = str(Path().resolve())
import sys
sys.path.append(dirProject)
# ----------------------------
import requests
import config

class RequestUtil:
    
    def doRequest(api, params, body) -> requests.models.Response:
        end_point = config.end_point
        service = end_point + api
        headers = {"access-token": config.x_access_token}

        return requests.get(service, headers=headers, params=params, json=body)