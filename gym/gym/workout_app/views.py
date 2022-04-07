from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from gym.auth_app.models import GymUser
from gym.workout_app.forms import WorkoutCreateForm
from gym.workout_app.models import WorkoutModel


class WorkoutListView(ListView):
    template_name = 'workout/workout-list.html'
    model = WorkoutModel


class AttendeesListView(ListView):
    template_name = 'workout/members-list.html'
    model = GymUser

    # find all participants in this workout
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


def sign_me(request, pk):
    obj = get_object_or_404(WorkoutModel, pk=pk)
    user = request.user
    if user in obj.participant.all():
        obj.participant.remove(user)
    else:
        obj.participant.add(request.user)
    return redirect('workout list')


class CoachWorkoutsListView(ListView):
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


class WorkoutCreateView(CreateView):
    template_name = 'workout/create-workout.html'
    form_class = WorkoutCreateForm
    success_url = reverse_lazy('workout list')
