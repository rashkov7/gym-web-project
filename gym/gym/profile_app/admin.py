from django.contrib import admin

from gym.profile_app.models import ProfileModel


@admin.register(ProfileModel)
class AdminProfile(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'user')