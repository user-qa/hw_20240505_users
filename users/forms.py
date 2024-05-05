from django import forms

from users.models import UserModel


class UserModelForms(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['full_name', 'age', 'phone_number', 'email', 'region', 'certificate']
