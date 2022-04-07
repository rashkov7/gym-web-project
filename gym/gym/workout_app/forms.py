from django import forms

from gym.workout_app.models import WorkoutModel


class BootstrapFormMixin:
    fields = {}

    def _init_placeholder(self):
        for name, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['placeholder'] = field.label

    def _init_readonly_fields(self):
        for name, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['readonly'] = True


class WorkoutCreateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = WorkoutModel
        fields = ('title', 'type_of_workout', 'description', 'hour', 'date', 'venue', 'img', 'participant', 'team')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_placeholder()
