# forecast_app/forms.py

from django import forms

class ForecastForm(forms.Form):
    """Form for selecting forecast horizon and dataset."""
    
    forecast_horizon = forms.IntegerField(
        label='Forecast Horizon (days)', 
        min_value=1,
        help_text='Enter the number of days for the forecast horizon.'
    )
    
    dataset_choice = forms.ChoiceField(
        choices=[
            ('sales', 'Daily sales data for a retail store'),
            ('temperature', 'Monthly average temperatures'),
            ('stock', 'Historical stock prices for a specific company')
        ],
        widget=forms.RadioSelect,
        label='Select Dataset',
        help_text='Choose the dataset for forecasting.'
    )