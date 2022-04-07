from django.urls import path

from gym.main_app.views import index_test, CoachListView, star_coach

urlpatterns = (
    path('', index_test, name='index'),
    path('trainers/', CoachListView.as_view(), name='trainers'),
    path('trainers/like/<int:pk>', star_coach, name='star the coach'),
)
