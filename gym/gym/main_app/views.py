from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormMixin

from gym.main_app.models import StarCoach
from gym.profile_app.models import ProfileModel
from gym.recipe_app.forms import SearchForm
from gym.recipe_app.models import RecipeModel
from gym.workout_app.models import WorkoutModel

UserModel = get_user_model()


class LandingPage(FormMixin, TemplateView):
    template_name = 'index.html'
    form_class = SearchForm
    success_url = reverse_lazy('index')


@login_required
def search_page(request):
    searched = request.POST['search']
    a = WorkoutModel.objects.filter(title__contains=searched)
    b = RecipeModel.objects.filter(title__contains=searched)
    c = ProfileModel.objects.filter(first_name__contains=searched).filter(user__trainer=True)
    context = {
        'workouts': a,
        'recipes': b,
        'coaches':c
    }
    return render(request, 'searched-list.html', context)


class CoachListView(LoginRequiredMixin, ListView):
    model = ProfileModel
    template_name = 'coaches-list.html'
    paginate_by = 3

    def get_queryset(self):
        if self.queryset is None:
            if self.model:
                return self.model._default_manager.filter(user__trainer=True)
            else:
                raise ImproperlyConfigured(
                    "%(cls)s is missing a QuerySet. Define "
                    "%(cls)s.model, %(cls)s.queryset, or override "
                    "%(cls)s.get_queryset()." % {
                        'cls': self.__class__.__name__
                    }
                )
        return self.queryset.all()


@login_required
def star_coach(request, pk):
    coach = get_object_or_404(ProfileModel, pk=pk)
    user = request.user
    star = StarCoach.objects.filter(owner__user_id=pk)
    if star:
        star.delete()
    else:
        StarCoach.objects.create(owner=coach, sender=user)
    return redirect('trainers')
