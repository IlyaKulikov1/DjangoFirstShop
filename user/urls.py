from django.urls import path

from user.views import register, all_users_view

urlpatterns = [
    path("register", register, name="register"),
    path("all_users", all_users_view, name="all_users_view"),
]
