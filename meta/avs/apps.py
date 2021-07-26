from django.apps import AppConfig


class AvsConfig(AppConfig):
    name = 'avs'

    def ready(self):
        import avs.signals
