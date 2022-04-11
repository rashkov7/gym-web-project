from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver

from gym.profile_app.models import ProfileModel

UserModel = get_user_model()


@receiver(signals.post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(first_name='Anonymous', last_name='Anonymous', user=instance)
