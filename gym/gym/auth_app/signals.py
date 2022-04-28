from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db.models import signals
from django.dispatch import receiver

from gym.auth_app.tasks import successful_registration_email
from gym.profile_app.models import ProfileModel

UserModel = get_user_model()


# using POST_SAVE to listen for EVENT when the user was created
# using CELERY to sent email asynchronous
@receiver(signals.post_save, sender=UserModel)
def user_created(instance, created, **kwargs):
    if created:
        successful_registration_email.delay(instance.email)
        ProfileModel.objects.create(first_name='Anonymous', last_name='Anonymous', user=instance)
        user = UserModel.objects.get(pk=instance.pk)
        permission = Permission.objects.get(name='Can change profile model')
        user.user_permissions.add(permission)
