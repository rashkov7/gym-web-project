from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory

from gym import settings
from gym.auth_app.views import RegisterUser
from gym.profile_app.models import ProfileModel

UserModel = get_user_model()


class TestRegisterView(TestCase):
    user_data = {
        'email': 'sobies@abv.bg',
        'password1': 'ABERSsk451',
        'password2': 'ABERSsk451',
    }
    invalid_user_data = {
        'email': 'sobies@abv.bg',
        'password1': 'ABERSsk451',
        'password2': 'faadsas',
    }
    data_user_A = {
        'email': 'test@mail.bg',
        'password': '123',
        'trainer': True
    }

    def test_login_url(self):
        login_url = "login"
        self.assertEqual(settings.LOGIN_URL, login_url)

    def test_register_view_with_correct_data__expect_success_with_new_user(self):
        response = self.client.post('/auth/register/', {**self.user_data}, follow=True)
        status_code = response.status_code
        self.assertEqual(200, status_code)
        self.assertTemplateUsed(response, 'profile/profile-update.html')
        new_user = UserModel.objects.all().count()
        self.assertEqual(1, new_user)

    def test_register_view_with_invalid_data__expect_no_user_same_page(self):
        response = self.client.post('/auth/register/', {**self.invalid_user_data}, follow=True)
        status_code = response.status_code
        self.assertEqual(200, status_code)
        self.assertTemplateUsed(response, 'user/register.html')
        new_user = UserModel.objects.all().count()
        self.assertEqual(0, new_user)

    def test_does_new_user_create_new_profile(self):
        UserModel.objects.create(**self.data_user_A)
        factory = RequestFactory()
        request = factory.get('/create//')
        response = RegisterUser.as_view()(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(ProfileModel.objects.first())
