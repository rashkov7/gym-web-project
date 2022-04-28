from django.contrib.auth import logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, PasswordResetConfirmView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView

from gym.auth_app.forms import CreateUserForm
from gym.auth_app.models import GymUser
from django.contrib import messages

UserModel = get_user_model()


class VerifyEmail(PasswordResetConfirmView):

    def dispatch(self, request, *args, **kwargs):
        self.user = self.get_user(kwargs["uidb64"])
        self.user.has_profile = True
        self.user.save()
        auth_login(self.request, self.user)
        return redirect('index')


class RegisterUser(CreateView):
    template_name = 'user/register.html'
    model = GymUser
    form_class = CreateUserForm
    success_url = reverse_lazy('trainers')

    def post(self, request, *args, **kwargs):
        user_email = request.POST['email']

        if not UserModel.objects.filter(email=user_email):

            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

        return super().post(request, *args, **kwargs)


@login_required
def logout_fbv(request):
    logout(request)
    return redirect('index')


class SignINView(LoginView):
    template_name = 'user/logn.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.get_user()
        if user.has_profile:
            auth_login(self.request, form.get_user())
            return HttpResponseRedirect(self.get_success_url())
        messages.error(self.request, 'You need to verify your e-mail')
        return redirect('login')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()
