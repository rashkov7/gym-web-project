from django.urls import path

from gym.auth_app.views import RegisterUser, logout_fbv, SignINView

urlpatterns = (
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', SignINView.as_view(), name='login'),
    path('logout/', logout_fbv, name='logout'),
)