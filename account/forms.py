from django.forms import ModelForm
from django.contrib.auth import forms, get_user_model

User = get_user_model()


class RegisterForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password1",
            "password2",
            "last_name",
            "first_name",
        ]
