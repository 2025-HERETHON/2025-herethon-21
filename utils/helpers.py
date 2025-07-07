from typing import Optional
from django.utils import timezone

class ResponseHelper:
    @staticmethod
    def success(status:int, title:str, data:Optional[list[str]|dict[str,any]]=None, message:Optional[str]=None) -> dict[str,any]:
        response = {
            "timestamp": timezone.localtime(timezone.now()),
            "status": status,
            "title": title
        }
        if data: response |= {"data": data}
        if message: response |= {"message": message}
        return response
    
    @staticmethod
    def error(status:int, title:str, message:str) -> dict[str,any]:
        return {
            "timestamp": timezone.localtime(timezone.now()),
            "status": status,
            "title": title,
            "message": message
        }