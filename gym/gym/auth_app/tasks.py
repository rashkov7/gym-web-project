from celery import shared_task
from django.contrib.auth import get_user_model

from django.core.mail import send_mail
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from gym.auth_app.utils import token_generator
from gym.auth_app.views import RegisterUser

UserModel = get_user_model()


@shared_task
def successful_registration_email(user_email):
    user = UserModel.objects.filter(email=user_email).first()
    domain = '127.0.0.1:8000'
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token_generator.make_token(user)})
    activate_link = 'http://' + domain + link

    subject = 'Verification mail'
    message = f"To verify your email use this link\n {activate_link}"
    our_mail = 'somemail@gmail.com'
    print(f'Email was send to {user_email}!')
    send_mail(
        subject=subject,
        message=message,
        from_email=our_mail,
        recipient_list=[user_email],
        fail_silently=True
    )
