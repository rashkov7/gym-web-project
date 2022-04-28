from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


# Use token generator for verification link
class AppTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return text_type((user.is_active + user.pk + timestamp))


token_generator = AppTokenGenerator()
