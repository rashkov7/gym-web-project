from django.apps import AppConfig


class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gym.main_app'

    def ready(self):
        import gym.main_app.signals
