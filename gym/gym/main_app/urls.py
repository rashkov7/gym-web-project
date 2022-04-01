from django.urls import path

from gym.main_app.views import index_test

urlpatterns = (
    path('', index_test, name='index'),
)
