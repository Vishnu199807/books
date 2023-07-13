from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("list/", views.PublicView.as_view(), name="book_list"),
    path("create/", views.BookCreateView.as_view(), name="book_create"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("register/", views.Register.as_view(), name="register"),
    path("token/", obtain_auth_token, name="token"),
]