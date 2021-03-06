from django import forms

from gym.helpers.mixins import BootstrapFormMixin
from gym.profile_app.models import ProfileModel


class ProfileUpdateForm(forms.ModelForm, BootstrapFormMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_placeholder()

    class Meta:
        model = ProfileModel
        fields = ('first_name', 'last_name', 'birth_date', 'gender', 'description')


class ProfilePhotoUpdate(forms.ModelForm,  BootstrapFormMixin):
    BootstrapFormMixin.excluded_fields = ('photo',)
    BootstrapFormMixin.bootstrap_class = 'invisible'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_readonly_fields()
        self._init__fields_class_attach()

    class Meta:
        model = ProfileModel
        fields = (
            'first_name',
            'last_name',
            'birth_date',
            'gender',
            'description',
            'photo',
        )
