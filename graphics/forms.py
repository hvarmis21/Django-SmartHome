from django import forms
from .models import FormUser


class UserForm(forms.ModelForm):
    class Meta:
        model = FormUser

        fields = [
            "title",
            "content",
            "user",
        ]
