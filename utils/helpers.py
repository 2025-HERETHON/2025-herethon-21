from typing import Optional, TypedDict
from datetime import datetime
from django.utils import timezone
from .formatters import format_timestamp

class ResponseHelper:
    class SuccessType(TypedDict):
        timestamp: datetime
        status: int
        title: str
        data: Optional[list[dict[str,any]]|dict[str,any]|list[str]]
        message: Optional[str]

    class ErrorType(TypedDict):
        timestamp: datetime
        status: int
        title: str
        message: str

    @staticmethod
    def success(status:int, title:str, data:Optional[list[dict[str,any]]|dict[str,any]|list[str]]=None, message:Optional[str]=None) -> SuccessType:
        response = {
            "timestamp": format_timestamp(timezone.localtime(timezone.now())),
            "status": status,
            "title": title
        }
        if data: response |= {"data": data}
        if message: response |= {"message": message}
        return response

    @staticmethod
    def error(status:int, title:str, message:str) -> ErrorType:
        return {
            "timestamp": format_timestamp(timezone.localtime(timezone.now())),
            "status": status,
            "title": title,
            "message": message
        }