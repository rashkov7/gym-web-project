from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin, AbstractUser
from django.db import models
from gym.auth_app.managers import GymUserManager


class GymUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True, verbose_name='Email')
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    has_profile = models.BooleanField(default=False)

    use_in_migrations = True

    USERNAME_FIELD = "email"

    objects = GymUserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        swappable = "AUTH_USER_MODEL"
