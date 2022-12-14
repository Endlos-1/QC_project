from django.urls import path, include
from .import views

app_name = 'accounts'

urlpatterns = [
    path("register", views.register, name="register"),
    path("signin", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
]