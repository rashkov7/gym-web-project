from django import forms

from gym.profile_app.models import ProfileModel


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name,field in self.fields.items():
            if name == 'user':
                field.widget = forms.HiddenInput()
                field.required = False


    class Meta:
        model = ProfileModel
        fields = '__all__'
        # exclude = ('user',)

