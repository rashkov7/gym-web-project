from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin

UserModel = get_user_model()


class BootstrapFormMixin:
    fields = {}
    excluded_fields = ()
    bootstrap_class = ''

    def _init_bootstrap_placeholder(self, *args, **kwargs):
        for name, field in self.fields.items():
            if name not in self.excluded_fields:
                if not hasattr(field.widget, 'attrs'):
                    setattr(field.widget, 'attrs', {})
                field.widget.attrs['placeholder'] = field.label

    def _init_readonly_fields(self):
        for name, field in self.fields.items():
            if name not in self.excluded_fields:
                if not hasattr(field.widget, 'attrs'):
                    setattr(field.widget, 'attrs', {})
                field.widget.attrs['readonly'] = True

    def _init__fields_class_attach(self):
        for name, field in self.fields.items():
            if name not in self.excluded_fields:
                if not hasattr(field.widget, 'attrs'):
                    setattr(field.widget, 'attrs', {})
                if 'class' not in field.widget.attrs and name not in self.excluded_fields:
                    field.widget.attrs['class'] = ''
                field.widget.attrs['class'] = self.bootstrap_class

    def _init_required_disabled_fields(self):
        for name, field in self.fields.items():
            if name not in self.excluded_fields:
                field.required = False

    def _init_hidden_fields(self):
        for name, field in self.fields.items():
            if name not in self.excluded_fields:
                field.required = False
                field.widget.is_hidden = True


class UserAuthorizedMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):

        user = request.user
        profile_user = UserModel.objects.get(profilemodel__user_id=kwargs['pk'])

        if not user == profile_user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
