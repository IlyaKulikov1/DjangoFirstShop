from django.urls import path
from user.views import register, all_users_view, user_login, me, logout_view

urlpatterns = [
    path("register", register, name="register"),
    path("all_users", all_users_view, name="all_users_view"),
    path("login", user_login, name="my_login"),
    path("me", me, name="me"),
    path('logout', logout_view, name="logout")
]
