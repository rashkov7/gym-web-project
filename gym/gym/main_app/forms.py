from django import forms

from gym.main_app.models import GymInfoModel
from gym.mixins import BootstrapFormMixin


class GymInfoForm(forms.ModelForm, BootstrapFormMixin):

    def __init__(self):
        super().__init__()
        self._init_bootstrap_placeholder()

    class Meta:
        model = GymInfoModel
        exclude = ('data', 'author', 'likes')

