from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gym.auth_app'

    def ready(self):
        import gym.auth_app.signals
