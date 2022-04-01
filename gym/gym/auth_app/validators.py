from django.core.exceptions import ValidationError


def valid_passwords_are_equals(pass1, pass2):
    if not pass1 == pass2:
        raise ValidationError("Passwords doesn't match !")
    return pass1
