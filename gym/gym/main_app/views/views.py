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
    context = {
        'workouts': WorkoutModel.objects.filter(title__contains=searched),
        'recipes': RecipeModel.objects.filter(title__contains=searched),
        'coaches': ProfileModel.objects.filter(first_name__contains=searched).filter(user__trainer=True)
    }
    if searched in 'workouts':
        context['workouts'] = WorkoutModel.objects.all()
    elif searched in 'recipes':
        context['recipes'] = RecipeModel.objects.all()
    elif searched in 'coaches':
        context['coaches'] = ProfileModel.objects.all().filter(user__trainer=True)
    find = {True for key,value in context.items() if value}
    if not find:
        context = {'no_matches': f'Sorry, there is no results with "{searched}".'}

    return render(request, 'searched-list.html', context)


class CoachListView(LoginRequiredMixin, ListView):
    model = ProfileModel
    template_name = 'coaches-list.html'
    paginate_by = 3

    def get_queryset(self):
        qry = super(CoachListView, self).get_queryset().filter(user__trainer=True)
        return qry


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
