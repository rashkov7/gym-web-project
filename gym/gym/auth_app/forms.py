from django import forms

from auth_app.validators import valid_passwords_are_equals
from gym.auth_app.models import GymUser, LoginFormModel


class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = GymUser
        fields = ('email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        confirm_password = valid_passwords_are_equals(password1, password2)
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user


class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginFormModel
        fields = ('email', 'password')

    def save(self, commit=True):
        super().save(commit=False)
        a=5
        c=5