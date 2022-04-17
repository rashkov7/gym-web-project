from django.core.exceptions import ValidationError
from django.test import TestCase

from gym.auth_app.forms import CreateUserForm


class SimpleTest(TestCase):
    user_date = {
        'email': 'sobies@abv.bg',
        'password1': 'ABERSsk451',
        'password2': 'ABERSsk451',
    }
    invalid_user_date = {
        'email': 'sobies@abv.bg',
        'password1': 'ABERSsk451',
        'password2': 'faadsas',
    }

    def test_clean_data2__valid_form_expect__no_exceptions(self):
        form = CreateUserForm(self.user_date)
        self.assertTrue(form.is_valid())

    def test_clean_data2__invalid_form__expect_exceptions(self):
        form = CreateUserForm(data=self.invalid_user_date)
        self.assertEqual(form.errors['password2'], ["Passwords didn't match."])

    def test_user_save_method__expected_save_true(self):
        form = CreateUserForm(self.user_date)
        self.assertTrue(form.save())

#     def setUp(self):
#         # Every test needs access to the request factory.
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(
#             username='jacob', email='jacob@…', password='top_secret')
#
#     def test_details(self):
#         # Create an instance of a GET request.
#         request = self.factory.get('/customer/details')
#
#         # Recall that middleware are not supported. You can simulate a
#         # logged-in user by setting request.user manually.
#         request.user = self.user
#
#         # Or you can simulate an anonymous user by setting request.user to
#         # an AnonymousUser instance.
#         request.user = AnonymousUser()
#
#         # Test my_view() as if it were deployed at /customer/details
#         response = my_view(request)
#         # Use this syntax for class-based views.
#         response = MyView.as_view()(request)
#         self.assertEqual(response.status_code, 200)
