from django.apps import apps as django_apps
from django.apps import AppConfig


class PredictorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testapp'
    verbose_name = "Personality Predictor"