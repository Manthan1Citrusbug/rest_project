from django.urls import path
from .views import user_login,custom_token



urlpatterns = [
    path('login/',user_login.as_view(),name="login"),
    path('custom_token/',custom_token.as_view(),name="custom_token"),
]