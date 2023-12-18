from typing import Any

from django.http.request import HttpRequest
from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from accounts.forms import UserRegisterForm


class HomePage(TemplateView):
    template_name = "home.html"

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        username = self.request.user.username
        context["username"] = username
        return context


class RegistrationView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
