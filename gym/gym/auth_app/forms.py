from django import forms
from django.contrib.auth import password_validation

from gym.auth_app.models import GymUser


class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html()
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html()
    )

    class Meta:
        model = GymUser
        fields = ('email', 'password1', 'password2')

    def clean_password2(self):
        if not self.cleaned_data['password1'] == self.cleaned_data['password2']:
            raise forms.ValidationError("Passwords didn't match.")
        password_validation.validate_password(self.cleaned_data.get('password1'), None)
        return self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user
