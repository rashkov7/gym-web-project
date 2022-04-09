from django.core.exceptions import ValidationError


def valid_passwords_are_equals(pass1, pass2):
    if not pass1 == pass2:
        raise ValidationError("Passwords doesn't match !")
    return pass1


def name_first_letter_validator(value: str):
    if value[0].islower():
        raise ValidationError('The name must star with upper letter !')


def validate_string_only_alphabet(string: str):
    if not string.isalpha():
        raise ValidationError('The name must contains only alphabetical characters')
