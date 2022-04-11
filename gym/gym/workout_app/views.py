from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404, redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from gym.auth_app.models import GymUser
from gym.workout_app.forms import WorkoutCreateForm
from gym.workout_app.models import WorkoutModel

UserModel = get_user_model()


class WorkoutListView(LoginRequiredMixin, ListView):
    template_name = 'workout/workout-list.html'
    model = WorkoutModel


class WorkoutCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'workout_app.add_workoutmodel'

    template_name = 'workout/create-workout.html'
    form_class = WorkoutCreateForm
    success_url = reverse_lazy('workout list')


class WorkoutUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'workout_app.add_workoutmodel'

    template_name = 'workout/edit-workout.html'
    model = WorkoutModel
    fields = ('title', 'type_of_workout', 'description', 'hour', 'date', 'venue', 'img', 'team')

    def get_success_url(self):
        return reverse_lazy('workout details', kwargs={'pk': self.object.id})


@login_required
def delete_workout(request, pk):
    obj = get_object_or_404(WorkoutModel, pk=pk)
    obj.delete()
    return redirect('workout list')


# View with all attendees at workout.
class AttendeesListView(LoginRequiredMixin, ListView):
    template_name = 'workout/members-list.html'
    model = GymUser

    def get_queryset(self):
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()

        elif self.model is not None:
            queryset = self.model._default_manager.filter(participants_of_event__id=self.kwargs['pk'])
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


@login_required
def sign_me(request, pk):
    obj = get_object_or_404(WorkoutModel, pk=pk)
    user = request.user
    if user in obj.participant.all():
        obj.participant.remove(user)
    else:
        obj.participant.add(request.user)
    return redirect('workout list')


# View: all coach's workouts that he lead
class CoachWorkoutsListView(LoginRequiredMixin, ListView):
    template_name = 'workout/workout-list.html'
    model = WorkoutModel

    def get_queryset(self):
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model._default_manager.filter(team__id=self.kwargs['pk'])
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


# View: workout's details with coaches who lead it
class WorkoutDetailView(LoginRequiredMixin, DetailView):
    template_name = 'workout/workout-details.html'
    model = WorkoutModel

    def get_context_data(self, **kwargs):
        context = {}
        context['coaches'] = UserModel.objects.filter(team_of_event=self.kwargs['pk'])
        context.update(kwargs)
        return super().get_context_data(**context)
