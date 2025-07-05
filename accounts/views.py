from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .services import UserService
from django.views.decorators.csrf import csrf_exempt
import json


# 템플릿 렌더링 처리

@csrf_exempt
# 회원 가입
def api_signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = UserService.signup(data)
            return JsonResponse(
                {"message": "회원가입 완료", 
                 
                #위에서 새로 만든 user 객체
                "user_id": user.username},
                status=201
            )
        except ValidationError as e:
            return JsonResponse(
                {"error": str(e)},
                status=400
            )
            