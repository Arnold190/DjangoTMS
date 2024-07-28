from django.apps import AppConfig


class CheckpointConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Checkpoint'

class MyAppConfig(AppConfig):
    name = 'Checkpoint'

    def ready(self):
        import Checkpoint.signals