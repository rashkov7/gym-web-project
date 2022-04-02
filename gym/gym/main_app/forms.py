from django import forms

from main_app.models import GymInfoModel


class GymInfoForm(forms.ModelForm):
    class Meta:
        model = GymInfoModel
        fields = '__all__'
