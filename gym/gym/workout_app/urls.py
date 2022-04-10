from django.urls import path

from gym.workout_app.views import WorkoutUpdateView, WorkoutListView, AttendeesListView, sign_me, \
    CoachWorkoutsListView, WorkoutCreateView, WorkoutDetailView, delete_workout

urlpatterns = (
    path('', WorkoutListView.as_view(), name='workout list'),
    path('create/', WorkoutCreateView.as_view(), name='create workout'),
    path('edit/<int:pk>', WorkoutUpdateView.as_view(), name='update workout'),
    path('delete/<int:pk>', delete_workout, name='delete workout'),
    path('<int:pk>', WorkoutDetailView.as_view(), name='workout details'),

    path('attendees/<int:pk>', AttendeesListView.as_view(), name='attendees list'),
    path('attendees/sign/<int:pk>', sign_me, name='signup workout'),
    path('coach_workouts/<int:pk>', CoachWorkoutsListView.as_view(), name='coach workouts'),
)
