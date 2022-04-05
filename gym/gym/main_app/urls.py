from django.urls import path

from gym.main_app.views import index_test,CoachListView

urlpatterns = (
    path('', index_test, name='index'),
    path('trainers/', CoachListView.as_view(), name='trainers'),
)
