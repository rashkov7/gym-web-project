from django.contrib import admin

from gym.auth_app.models import GymUser


@admin.register(GymUser)
class AdminGymUser(admin.ModelAdmin):
    list_display = ('email', 'date_joined')