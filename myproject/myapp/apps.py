from django.apps import AppConfig


class MyappConfig(AppConfig):
    """
    Configuration class for the 'myapp' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
