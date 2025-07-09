import logging
from django.conf import settings
from django.http.request import HttpRequest
from django.shortcuts import render
from .exceptions import ClientError

logger = logging.getLogger(__name__)

class ErrorHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request:HttpRequest, exception:Exception):
        if settings.DEBUG: return None  # 개발 환경에서는 Django 기본 디버그 페이지 노출

        if isinstance(exception, ClientError):
            logger.warning(f'{exception.status_code} {exception.status_title}: {exception.message}', exc_info=True)
            exception_status_code = exception.status_code
            exception_status_title = exception.status_title
            exception_message = exception.message
        else:
            logger.error(f'{type(exception).__name__}: {exception}', exc_info=True)
            exception_status_code = 500
            exception_status_title = 'Internal Server Error'
            exception_message = str(exception)

        context = {
            'exception': {
                'status_code': exception_status_code,
                'status_title': exception_status_title,
                'message': exception_message,
            }
        }
        return render(request, 'error.html', context, status=exception_status_code)