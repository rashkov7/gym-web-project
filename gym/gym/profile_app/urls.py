from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from gym.profile_app.views import UpdateProfileView, ProfilePageView, MyRecipeView, MyWorkoutView

urlpatterns = [
                  path('create/<int:pk>', UpdateProfileView.as_view(), name='update profile'),
                  path('<int:pk>', ProfilePageView.as_view(), name='profile page'),
                  path('workouts/<int:pk>', MyWorkoutView.as_view(), name='my workouts'),
                  path('recipes/<int:pk>', MyRecipeView.as_view(), name='my recipes'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
