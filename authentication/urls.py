from django.urls import path
from authentication.views import register, login_user, logout_user, change_user_password

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('change-password/', change_user_password, name='change-password'),
    
]