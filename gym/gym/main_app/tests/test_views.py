from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory

from gym.main_app.views.views import CoachListView

UserModel = get_user_model()


class TestCoachListView(TestCase):
    data_coach_A = {
        'email': 'test@mail.bg',
        'password': '123',
        'trainer': True

    }
    data_coach_B = {
        'email': 'test_2@mail.bg',
        'password': '123',
        'trainer': True
    }
    data_coach_C = {
        'email': 'test_3@mail.bg',
        'password': '123',
        'trainer': False
    }


    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user_A = UserModel.objects.create_user(**self.data_coach_A)
        self.user_B = UserModel.objects.create_user(**self.data_coach_B)
        self.user_C = UserModel.objects.create_user(**self.data_coach_C)

    def test_queryset_with_2_coaches(self):
        request = self.factory.get('/coach-list//')
        request.user = self.user_A
        response = CoachListView.as_view()(request)
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(response.context_data['object_list']))

