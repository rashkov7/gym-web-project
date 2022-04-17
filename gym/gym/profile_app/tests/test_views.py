from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.core.exceptions import PermissionDenied
from django.test import TestCase, RequestFactory

from gym.profile_app.views import ProfilePageView, UpdateProfileView

UserModel = get_user_model()


class TestProfilePageView(TestCase):
    data_user_A = {
        'email': 'test@mail.bg',
        'password': '123',
        'trainer': True

    }
    data_user_B = {
        'email': 'test_2@mail.bg',
        'password': '123',
        'trainer': True
    }
    data_user_C = {
        'email': 'test_3@mail.bg',
        'password': '123',
        'trainer': False
    }

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user_A = UserModel.objects.create_user(**self.data_user_A)
        self.user_B = UserModel.objects.create_user(**self.data_user_B)

    def test_page_whe_user_is_owner(self):
        request = self.factory.get('/profile//1')
        request.user = self.user_A
        response = ProfilePageView.as_view()(request, pk=1)

        self.assertEqual(200, response.status_code),
        self.assertEqual(True, response.context_data['owner'])

    def test_page_whe_user_not_owner(self):
        request = self.factory.get('/profile//1')
        request.user = self.user_B
        response = ProfilePageView.as_view()(request, pk=1)

        self.assertEqual(200, response.status_code),
        self.assertIsNone(response.context_data.get('owner'))


class TestProfileUpdateView(TestCase):
    data_user_A = {
        'email': 'test@mail.bg',
        'password': '123',
        'trainer': True
    }
    data_user_B = {
        'email': 'test_2@mail.bg',
        'password': '123',
        'trainer': True
    }

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user_A = UserModel.objects.create(**self.data_user_A)
        self.user_B = UserModel.objects.create(**self.data_user_B)

    def test_page_whe_user_is_owner(self):
        request = self.factory.get('/profile//update//1')
        request.user = self.user_A
        permission = Permission.objects.get(name='Can change profile model')
        request.user.user_permissions.add(permission)
        response = UpdateProfileView.as_view()(request, pk=1)
        self.assertEqual(200, response.status_code)

    def test_page_whe_user_is_not_owner_except_permissionerror(self):
        request = self.factory.get('/profile//update//1')
        request.user = self.user_B
        permission = Permission.objects.get(name='Can change profile model')
        request.user.user_permissions.add(permission)
        with self.assertRaises(PermissionDenied):
            UpdateProfileView.as_view()(request, pk=1)

