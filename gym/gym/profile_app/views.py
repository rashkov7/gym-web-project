from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import UpdateView, ListView, DetailView

from gym.profile_app.forms import ProfileForm
from gym.profile_app.models import ProfileModel
from gym.recipe_app.models import RecipeModel
from gym.workout_app.models import WorkoutModel

UserModel = get_user_model()


class UpdateProfileView(UpdateView):
    template_name = 'profile/profile-update.html'
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


class ProfilePageView(DetailView):
    template_name = 'profile/profile_details.html'
    model = ProfileModel


class MyWorkoutView(ListView):
    template_name = 'profile/my_events.html'
    model = WorkoutModel

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
            queryset = self.model._default_manager.filter(participant=user)
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset


class MyRecipeView(ListView):
    template_name = 'profile/my_recipes.html'
    model = RecipeModel

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            a = 5
            user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
            queryset = self.model._default_manager.filter(favorites=user)
            b = 5
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset
