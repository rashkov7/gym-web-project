from django import forms

from gym.helpers.mixins import BootstrapFormMixin
from gym.workout_app.models import WorkoutModel


class WorkoutCreateForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_placeholder()

    class Meta:
        model = WorkoutModel
        fields = ('title', 'type_of_workout', 'description', 'hour', 'date', 'venue', 'img', 'team')


