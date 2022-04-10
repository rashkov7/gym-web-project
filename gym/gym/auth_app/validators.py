from django.core.exceptions import ValidationError


def name_first_letter_validator(value: str):
    if value[0].islower():
        raise ValidationError('The name must star with upper letter !')


def validate_string_only_alphabet(string: str):
    for ch in string:
        if not ch.isalpha() and not ' ':
            raise ValidationError('The name must contains only alphabetical characters')
