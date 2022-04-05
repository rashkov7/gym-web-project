from django import forms

from gym.profile_app.models import ProfileModel


class ProfileForm(forms.ModelForm):

    HIDDEN_INPUTS = (
        'user', 'crossfit_coach',
        'yoga_coach', 'combat_coach',
        'fitness_coach', 'dance_coach'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.HIDDEN_INPUTS:
                field.widget = forms.HiddenInput()
                field.required = False

    class Meta:
        model = ProfileModel
        fields = '__all__'
