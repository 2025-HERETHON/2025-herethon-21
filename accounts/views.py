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
            
@csrf_exempt
def api_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = UserService.login(data)

            '''
            아래 if 문(=방어 코드) 하나로 로그인 성공 여부가 달림. 왜?
            해당 코드를 넣어서 서버가 죽지 않음.(= 500 에러 안 남)
            그래서 postman에서 올바르게 재시도.
            → authenticate가 정상 통과되면서 로그인 성공!
            '''
            
            if not user:
                raise ValidationError("로그인 실패 (사용자 인증되지 않음)")

            return JsonResponse(
                {
                    "message": "로그인 완료",
                    "user_id": user.username,    # NANOID
                    "user_email": user.email     # 실제 로그인 아이디
                },
                status=200
            )
        except ValidationError as e:
            error_msg = str(e)
            if "필수 항목" in error_msg:
                status_code = 400
            elif "올바르지" in error_msg:
                status_code = 404
            else:
                status_code = 400

            return JsonResponse(
                {"error": error_msg},
                status=status_code
            ) 
            