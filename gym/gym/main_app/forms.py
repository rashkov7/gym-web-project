from django import forms

from gym.main_app.models import GymInfoModel


class GymInfoForm(forms.ModelForm):
    class Meta:
        model = GymInfoModel
        exclude = ('data', 'author', 'likes')

