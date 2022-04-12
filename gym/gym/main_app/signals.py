from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver

from gym.main_app.tasks import successful_registration_email
from gym.profile_app.models import ProfileModel

UserModel = get_user_model()


@receiver(signals.post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        successful_registration_email.delay(instance.id)
        ProfileModel.objects.create(first_name='Anonymous', last_name='Anonymous', user=instance)

