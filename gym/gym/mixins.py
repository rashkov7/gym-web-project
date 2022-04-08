from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin

UserModel = get_user_model()


class UserAuthorizedMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        profile_user = UserModel.objects.get(profilemodel__user_id=kwargs['pk'])
        if not user == profile_user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)