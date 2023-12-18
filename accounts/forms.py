from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, ModelForm

User = get_user_model()


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]


class UserRegisterForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
