from django.urls import path
from user.views import register, all_users_view, user_login, me

urlpatterns = [
    path("register", register, name="register"),
    path("all_users", all_users_view, name="all_users_view"),
    path("login", user_login, name="login"),
    path("me", me, name="me"),
]
