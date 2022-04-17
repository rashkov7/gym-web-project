from django.contrib import admin

from gym.main_app.models import GymInfoModel


@admin.register(GymInfoModel)
class AdminSiteInfo(admin.ModelAdmin):
    pass