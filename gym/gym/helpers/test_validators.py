from django.test import TestCase

from django.core.exceptions import ValidationError

from gym.helpers.validators import name_first_letter_validator, validator_name_only_alphabet_and_space


class TestValidators(TestCase):

    def test_valid_name_with_upper_case(self):
        self.assertIsNone(name_first_letter_validator('Valid'))

    def test_invalid_name_without_upper_case(self):
        with self.assertRaises(ValidationError) as ex:
            name_first_letter_validator('invalid')
        self.assertEqual("['The first letter must be upper!']", str(ex.exception))

    def test_validator_name_only_alphabet_and_space_expect_correct(self):
        self.assertIsNone(validator_name_only_alphabet_and_space('Valid Name'))

    def test_validator_name_only_alphabet_and_space_expect_exception(self):
        with self.assertRaises(ValidationError) as ex:
            validator_name_only_alphabet_and_space('Valid N@me')
        self.assertEqual("['The name must contains only alphabetical characters and space.Forbidden: \"@\"']", str(ex.exception))