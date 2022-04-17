from django.core.exceptions import ValidationError


def name_first_letter_validator(value: str):
    if value[0].islower():
        raise ValidationError('The first letter must be upper!')


def validator_name_only_alphabet_and_space(string: str):
    forbidden = [x for x in string if not (x.isalpha() or x == ' ')]
    for ch in string:
        if not (ch.isalpha() or ch == ' '):
            raise ValidationError(f'The name must contains only alphabetical characters and space.Forbidden: "{",".join(forbidden)}"')
