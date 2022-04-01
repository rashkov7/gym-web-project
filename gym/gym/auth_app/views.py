from django.contrib.auth import logout, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from gym.auth_app.forms import CreateUserForm, LoginForm

UserModel = get_user_model()

class RegisterUser(CreateView):
    template_name = 'user/register.html'
    success_url = reverse_lazy('index')
    model = UserModel
    form_class = CreateUserForm


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