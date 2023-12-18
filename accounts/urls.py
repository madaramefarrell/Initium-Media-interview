from django.urls import path

from accounts.views import HomePage, RegistrationView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", RegistrationView.as_view(), name="signup"),
]
