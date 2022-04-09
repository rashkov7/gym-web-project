from django import forms

from gym.mixins import BootstrapFormMixin
from gym.workout_app.models import WorkoutModel


class WorkoutCreateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = WorkoutModel
        fields = ('title', 'type_of_workout', 'description', 'hour', 'date', 'venue', 'img', 'participant', 'team')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_placeholder()
