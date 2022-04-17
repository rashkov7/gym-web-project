from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import UpdateView, ListView, DetailView, DeleteView

from gym.helpers.mixins import UserAuthorizedMixin
from gym.profile_app.forms import ProfileUpdateForm
from gym.profile_app.models import ProfileModel
from gym.recipe_app.models import RecipeModel
from gym.workout_app.models import WorkoutModel

UserModel = get_user_model()

""" ProfilePageView. Simple view with extra content. OWNER is needed for authorization. """


class ProfilePageView(LoginRequiredMixin, DetailView):
    template_name = 'profile/profile_details.html'
    model = ProfileModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        user = self.request.user
        profile = get_object_or_404(ProfileModel, pk=self.kwargs['pk'])

        if user.profilemodel == profile:
            context['owner'] = True
        return context


# BASE UPDATE VIEW - update profile separately( photo / context)
class UpdateProfileBaseView(UserAuthorizedMixin, UpdateView):
    permission_required = 'profile_app.change_profilemodel'

    model = ProfileModel
    template_name = None
    form_class = None

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        if not self.request.user.has_profile:
            self.request.user.has_profile = True
            self.request.user.save()
        self.object = form.save(commit=True)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile page', kwargs={'pk': self.object.pk})


class UpdateProfileView(UpdateProfileBaseView):
    template_name = 'profile/profile-update.html'
    form_class = ProfileUpdateForm


class UpdateProfilePhotoView(UpdateProfileBaseView):
    template_name = 'profile/profile-update-photo.html'
    fields = ('photo',)


class DeleteProfileView(UserAuthorizedMixin, DeleteView):
    permission_required = 'profile_app.change_profilemodel'

    model = UserModel
    template_name = 'profile/delete-user.html'
    success_url = reverse_lazy('index')


# Customer, workouts View. Queryset with all his sign workouts.
class MyWorkoutView(UserAuthorizedMixin, ListView):
    permission_required = 'profile_app.change_profilemodel'

    template_name = 'profile/my_events.html'
    model = WorkoutModel

    def get_queryset(self):
        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        queryset = self.model._default_manager.filter(participant=user)

        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset


""" Customer - recipes View. Queryset with all his fav recipe. """


class MyRecipeView(UserAuthorizedMixin, ListView):
    permission_required = 'profile_app.change_profilemodel'

    template_name = 'profile/my_recipes.html'
    model = RecipeModel

    def get_queryset(self):
        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        queryset = self.model._default_manager.filter(favorites=user)

        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset
