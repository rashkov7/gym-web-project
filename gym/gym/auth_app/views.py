from django.contrib.auth import logout, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from gym.auth_app.forms import CreateUserForm
from gym.auth_app.models import GymUser

UserModel = get_user_model()


class RegisterUser(CreateView):
    template_name = 'user/register.html'
    model = GymUser
    form_class = CreateUserForm

    def get_success_url(self):
        return reverse_lazy('update profile', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        permission = Permission.objects.get(name='Can change profile model')
        user.user_permissions.add(permission)
        return result


@login_required
def logout_fbv(request):
    logout(request)
    return redirect('index')


class SignINView(LoginView):
    template_name = 'user/logn.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()
