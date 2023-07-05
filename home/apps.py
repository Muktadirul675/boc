from django.apps import AppConfig
from django.core.signals import request_finished


class HomeConfig(AppConfig):
    name = 'home'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        # from . import signals
        import home.signals
        # Explicitly connect a signal handler.
        # request_finished.connect(signals.my_callback)