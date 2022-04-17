from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

UserModel = get_user_model()


class TestUserModel(TestCase):
    correct_user_data = {
        "email": "sobies@abv.bg",
        'password': 'ASDzxc11'
    }

    def test_correct_instance_of_model(self):
        user = UserModel(**self.correct_user_data)
        user.full_clean()
        user.save()
        self.assertIsNotNone(user)
        self.assertEqual("sobies@abv.bg", user.email)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.has_profile)
        self.assertFalse(user.trainer)

    def test_invalid_date_expect_validation_error(self):
        self.correct_user_data['email'] = 'asdasd'
        user = UserModel(**self.correct_user_data)
        with self.assertRaises(ValidationError) as ex:
            user.full_clean()
            user.save()

