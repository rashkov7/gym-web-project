from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from gym.profile_app.views import UpdateProfileView, DeleteProfileView, ProfilePageView, MyRecipeView, MyWorkoutView, \
    UpdateProfilePhotoView

urlpatterns = [
                  path('<int:pk>', ProfilePageView.as_view(), name='profile page'),
                  path('update/<int:pk>', UpdateProfileView.as_view(), name='update profile'),
                  path('update_photo/<int:pk>', UpdateProfilePhotoView.as_view(), name='update photo profile'),
                  path('delete/<int:pk>', DeleteProfileView.as_view(), name='delete profile'),

                  path('workouts/<int:pk>', MyWorkoutView.as_view(), name='my workouts'),
                  path('recipes/<int:pk>', MyRecipeView.as_view(), name='my recipes'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
