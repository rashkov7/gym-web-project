from django.urls import path

from gym.workout_app.views import WorkoutListView, AttendeesListView, sign_me, CoachWorkoutsListView, WorkoutCreateView,WorkoutDetailView

urlpatterns = (
    path('', WorkoutListView.as_view(), name='workout list'),
    path('attendees/<int:pk>', AttendeesListView.as_view(), name='attendees list'),
    path('<int:pk>', WorkoutDetailView.as_view(), name='workout details'),
    path('attendees/sign/<int:pk>', sign_me, name='signup workout'),
    path('create/', WorkoutCreateView.as_view(), name='create workout'),
    path('coach_workouts/<int:pk>', CoachWorkoutsListView.as_view(), name='coach workouts'),
)
