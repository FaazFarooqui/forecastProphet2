# forecast_app/apps.py

from django.apps import AppConfig

class ForecastAppConfig(AppConfig):
    """Configuration for the Forecast application."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forecast_app'