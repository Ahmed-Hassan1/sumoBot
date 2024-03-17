from django.apps import AppConfig


class IndicatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'indicator'

    def ready(self):
        from jobs import updater
        updater.start()