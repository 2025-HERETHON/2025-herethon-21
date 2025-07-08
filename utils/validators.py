from functools import wraps
from django.db import IntegrityError
from .helpers import ResponseHelper

def validate_form(func):
    """
    Returns:
        None|dict[str,any]: 유효=None | 비유효=400 Bad Request
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.form.is_valid():
            print('\n\n', ResponseHelper.error(400, "Bad Request", "필수 값을 누락하였거나, 입력 값이 유효하지 않습니다."), '\n')
            return ResponseHelper.error(400, "Bad Request", "필수 값을 누락하였거나, 입력 값이 유효하지 않습니다.")
        return func(self, *args, **kwargs)
    return wrapper

def validate_auth(func):
    """
    Returns:
        None|dict[str,any]: 유효=None | 비유효=401 Unauthorized
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            print('\n\n', ResponseHelper.error(401, "Unauthorized", "인증 정보가 없거나 만료되었습니다."), '\n')
            return ResponseHelper.error(401, "Unauthorized", "인증 정보가 없거나 만료되었습니다.")
        return func(self, *args, **kwargs)
    return wrapper

def validate_permission(func):
    """
    Returns:
        None|dict[str,any]: 유효=None | 비유효=403 Forbidden
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.instance.user != self.request.user:
            print('\n\n', ResponseHelper.error(403, "Forbidden", "콘텐츠 접근 권한이 없습니다."), '\n')
            return ResponseHelper.error(403, "Forbidden", "콘텐츠 접근 권한이 없습니다.")
        return func(self, *args, **kwargs)
    return wrapper

def validate_unique(func):
    """
    Returns:
        None|dict[str,any]: 유효=None | 비유효=409 Conflict
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except IntegrityError as error:
            if 'UNIQUE constraint failed' in str(error):
                print('\n\n', ResponseHelper.error(409, "Conflict", "이미 존재하는 값입니다."), '\n')
                return ResponseHelper.error(409, "Conflict", "이미 존재하는 값입니다.")
            else:
                print('\n\n', ResponseHelper.error(500, "Internal Server Error", str(error)), '\n')
                return ResponseHelper.error(500, "Internal Server Error", str(error))
    return wrapper