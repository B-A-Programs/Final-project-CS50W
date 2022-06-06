from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<username>", views.profile, name="profile"),
    path("edit/<username>", views.edit, name="edit"),
    path("delete/<id>", views.delete, name="delete")
]
