from django.contrib import admin

from gym.auth_app.models import GymUser


@admin.register(GymUser)
class AdminGymUser(admin.ModelAdmin):
    pass