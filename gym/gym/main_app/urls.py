from django.urls import path

from gym.main_app.views.views import CoachListView, star_coach, search_page, LandingPage

urlpatterns = (
    path('', LandingPage.as_view(), name='index'),
    path('trainers/', CoachListView.as_view(), name='trainers'),
    path('trainers/like/<int:pk>', star_coach, name='star the coach'),
    path('search/', search_page, name='search'),
)
