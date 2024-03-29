from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("register_company", views.register_company, name="register_company"),
    path("profile/<username>", views.profile, name="profile"),
    path("edit/<username>", views.edit, name="edit"),
    path("delete/<id>", views.delete, name="delete"),
    path("create_post", views.create_post, name="create_post"),
    path("post/<id>", views.post, name="post"),
    path("apply/<id>", views.apply, name="apply"),
    path("applicants", views.applicants, name="applicants"),
    path("message", views.message, name="message"),
    path("interviews", views.interviews, name="interviews"),
    path("posts/<field>/<level>", views.posts, name="posts"),
    path("users/<field>", views.users, name="users"),
    path("reject/<id>", views.reject, name="reject")
]
