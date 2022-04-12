from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

UserModel = get_user_model()


@shared_task
def successful_registration_email(user):
    subject = 'Welcome Email'
    message = " Congratulations! We've become a part of our family "
    our_mail = 'somemail@gmail.com'
    to_customer = UserModel.object.get(pk=user)

    send_mail(
        subject=subject,
        message=message,
        from_email=our_mail,
        recipient_list=[to_customer]
    )
