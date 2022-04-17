from django import forms
from django.test import TestCase

from gym.helpers.mixins import BootstrapFormMixin
from gym.profile_app.models import TestModel


class TestForm(forms.ModelForm, BootstrapFormMixin):
    BootstrapFormMixin.excluded_fields = ('photo',)
    BootstrapFormMixin.bootstrap_class = 'invisible'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_readonly_fields()
        self._init__fields_class_attach()
        self._init_bootstrap_placeholder()

    class Meta:
        model = TestModel
        fields = ('test',)


class TestBootstrapMixins(TestCase):
    class DummyForm(TestForm):
        pass

    class DummyFormClassAdded(TestForm):
        BootstrapFormMixin.bootstrap_class = 'test-class'

    def test_placeholder_mixins_all_fields(self):
        dummy_view = self.DummyForm()
        self.assertEqual('Test', dummy_view.fields['test'].widget.attrs['placeholder'])

    def test_readonly_mixin_all_fields(self):
        dummy_view = self.DummyFormClassAdded()
        self.assertEqual('test-class', dummy_view.fields['test'].widget.attrs['class'])

