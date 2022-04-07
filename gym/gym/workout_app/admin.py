from django.contrib import admin


from gym.workout_app.models import WorkoutModel


@admin.register(WorkoutModel)
class AdminWorkout(admin.ModelAdmin):
    pass