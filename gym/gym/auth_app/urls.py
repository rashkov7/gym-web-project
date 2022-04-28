from django.urls import path

from gym.auth_app.views import RegisterUser, logout_fbv, SignINView, VerifyEmail

urlpatterns = (
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', SignINView.as_view(), name='login'),
    path('email_verify/<uidb64>/<token>', VerifyEmail.as_view(), name='activate'),
    path('logout/', logout_fbv, name='logout'),
)
