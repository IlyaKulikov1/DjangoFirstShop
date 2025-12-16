from django.urls import path, include
from user_auth.views import register, all_users_view, user_login, me, logout_view
from .views import UserViewSet
from rest_framework import routers
from .views import RegistrationAPIView
from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("register", RegistrationAPIView.as_view(), name="register"),
    path('user', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path("all_users", all_users_view, name="all_users_view"),
    # path("login", user_login, name="my_login"),
    # path("me", me, name="me"),
    # path('logout', logout_view, name="logout")
]
