from django.urls import path
from .views import main_view, signup_view, login_view, logout_view, delete_CustomUser, update_CustomUser

app_name = 'accounts'

urlpatterns = [
    path('', main_view, name="main"),
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('delete/', delete_CustomUser, name="delete_CustomUser"),
    
    # 사용자 개인 정보 수정이므로 request.user 접근으로 수정
    path('update/', update_CustomUser, name="update_CustomUser")
]

