from functools import wraps
from django.db import IntegrityError
from .exceptions import ClientError

def validate_form(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.form.is_valid():
            raise ClientError(400, 'Bad Request', '필수 값을 누락하였거나, 입력 값이 유효하지 않습니다.')
        return func(self, *args, **kwargs)
    return wrapper

def validate_not_self(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        import inspect
        bound = inspect.signature(func).bind(self, *args, **kwargs)
        bound.apply_defaults()

        sender = bound.arguments.get('sender')
        receiver = bound.arguments.get('receiver')

        if sender == receiver:
            raise ClientError(400, 'Bad Request', '자신에게는 요청을 수행할 수 없습니다.')
        return func(self, *args, **kwargs)
    return wrapper

def validate_auth(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            raise ClientError(401, 'Unauthorised', '인증 정보가 없거나 만료되었습니다.')
        return func(self, *args, **kwargs)
    return wrapper

def validate_permission(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.instance.user != self.request.user:
            raise ClientError(403, 'Forbidden', '콘텐츠 접근 권한이 없습니다.')
        return func(self, *args, **kwargs)
    return wrapper

def validate_unique(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except IntegrityError as error:
            if 'UNIQUE constraint failed' in str(error):
                raise ClientError(409, 'Conflict', '이미 존재하는 값입니다.')
    return wrapper