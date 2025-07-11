from django.urls import path
from .views import signup_onboarding1, signup_onboarding2 ,signup_onboarding3_submit, login_view, logout_view, delete_CustomUser, update_CustomUser

app_name = 'accounts'

urlpatterns = [    
    # 온보딩 회원가입 흐름
    path('signup/onboarding1/', signup_onboarding1, name="signup_onboarding1"),
    path('signup/onboarding2/', signup_onboarding2, name="signup_onboarding2"),
    path('signup/onboarding3/submit/', signup_onboarding3_submit, name="signup_onboarding3_submit"),

    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('delete/', delete_CustomUser, name="delete_CustomUser"),
    path('update/', update_CustomUser, name="update_CustomUser"),
]