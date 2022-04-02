from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from django.views.generic import UpdateView

from gym.profile_app.forms import ProfileForm
from gym.profile_app.models import ProfileModel

UserModel = get_user_model()


class UpdateProfileView(UpdateView):
    template_name = 'profile/profile_update.html'
    model = ProfileModel
    success_url = reverse_lazy('index')
    form_class = ProfileForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        if not self.request.user.has_profile:
            self.request.user.has_profile = True
            self.request.user.save()
        self.object = form.save(commit=True)
        return super().form_valid(form)
