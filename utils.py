from enum import Enum
from typing import Any, Optional

class ResponseType(Enum):
    SUCCESS = "success"
    ERROR = "error"

def response(responseType: ResponseType, data:Any, msg:str = ""):
    return {
        "status": responseType.value,
        "data":data,
        "msg":msg
    }