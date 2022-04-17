from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver

from gym import settings
from gym.auth_app.tasks import successful_registration_email
from gym.profile_app.models import ProfileModel

UserModel = get_user_model()


@receiver(signals.post_save, sender=UserModel)
def user_created(instance, created, **kwargs):
    if created:
        if settings.DEBUG:
            successful_registration_email(instance.id)
        else:
            successful_registration_email.delay(instance.id)
        ProfileModel.objects.create(first_name='Anonymous', last_name='Anonymous', user=instance)

