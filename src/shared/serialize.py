import json
from datetime import datetime


def serialize_datetime(data: list):
    for item in data:
        for key, value in item.items():
            if isinstance(value, dict):
                for k, v in value.items():
                    if isinstance(v, datetime):
                        value[k] = v.isoformat()

    return json.dumps(data)
