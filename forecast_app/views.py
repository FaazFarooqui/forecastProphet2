# forecast_app/views.py

import os
import io
import pandas as pd
import matplotlib.pyplot as plt
from django.conf import settings
from django.shortcuts import render
from .forms import ForecastForm
from prophet import Prophet
import base64
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from dateutil import parser
import numpy as np

def parse_dates(date_str):
    try:
        return parser.parse(date_str)
    except ValueError:
        return None
    
def load_and_preprocess_data(data_file_path, ds_col, y_col, dataset_choice):
    """Load and preprocess the data."""
    # Load the data
    df = pd.read_csv(data_file_path, encoding='ISO-8859-1')
    df['ds'] = df[ds_col].apply(parse_dates)
    
    # Handle different formats for the 'y' column
    if dataset_choice == 'stock':
        df['y'] = df[y_col].str.replace('[\$,]', '', regex=True).astype(float)
    else:
        df['y'] = df[y_col].astype(float)
    
    # Handle missing values
    df = df.dropna(subset=['ds', 'y'])
    
    # Normalize the 'y' values
    scaler = MinMaxScaler()
    df['y'] = scaler.fit_transform(df[['y']])
    
    return df, scaler

def forecast_view(request):
    xlabel_val, ylabel_val, title_label, ds_col, y_col  = '', '', '', '', ''
    if request.method == 'POST':
        form = ForecastForm(request.POST)
        if form.is_valid():
            forecast_horizon = form.cleaned_data['forecast_horizon']
            dataset_choice = form.cleaned_data['dataset_choice']

            # Determine the data file path based on the selected dataset
            if dataset_choice == 'sales':
                data_file_path = os.path.join(settings.BASE_DIR, 'sales_forecasting', 'data', 'sales_data_sample.csv')
                xlabel_val, ylabel_val, title_label, ds_col, y_col = 'Time', 'Sales', 'Historical Data Trends', 'ORDERDATE', 'SALES'
            elif dataset_choice == 'temperature':
                data_file_path = os.path.join(settings.BASE_DIR, 'sales_forecasting', 'data', 'temperature_data_sample.csv')
                xlabel_val, ylabel_val, title_label, ds_col, y_col = 'Date', 'Temperature', 'Historical Data Trends', 'time', 'new_york'
            elif dataset_choice == 'stock':
                data_file_path = os.path.join(settings.BASE_DIR, 'sales_forecasting', 'data', 'stock_data_sample.csv')
                xlabel_val, ylabel_val, title_label, ds_col, y_col = 'Date', 'Last Price', 'Historical Data Trends', 'Date', 'Close/Last'

            else:
                raise ValueError("Invalid dataset choice")

            # Check if the file exists
            if not os.path.exists(data_file_path):
                raise FileNotFoundError(f"The data file was not found: {data_file_path}")
            
            # Load and preprocess the data
            df, scaler = load_and_preprocess_data(data_file_path, ds_col, y_col, dataset_choice)
            
            # Split the data into training and testing sets
            train_df, test_df = train_test_split(df, test_size=0.3, shuffle=False)

            # Fit the Prophet model
            model = Prophet()
            model.fit(train_df)
            
            # Make future dataframe
            future = model.make_future_dataframe(periods=len(test_df))
            forecast = model.predict(future)
            
            # Inverse transform the forecasted 'y' values to original scale
            forecast[['yhat', 'yhat_lower', 'yhat_upper']] = scaler.inverse_transform(forecast[['yhat', 'yhat_lower', 'yhat_upper']])
            test_df['y'] = scaler.inverse_transform(test_df[['y']])

            # Evaluate the model
            y_true = test_df['y'].values
            y_pred = forecast['yhat'].values[-len(test_df):]
            mse = mean_squared_error(y_true, y_pred)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(y_true, y_pred)
            r2 = r2_score(y_true, y_pred)

            # Plot the historical data
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(df['ds'], scaler.inverse_transform(df[['y']]), label='Historical Data')
            ax.set_xlabel(xlabel_val)
            ax.set_ylabel(ylabel_val)
            plt.title(title_label)
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            historical_data_image = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()
            
            # Plot the forecast with confidence intervals
            fig, ax = plt.subplots(figsize=(10, 6))
            model.plot(forecast, ax=ax)
            ax.set_xlabel(xlabel_val)
            ax.set_ylabel(ylabel_val)
            plt.title('Forecasted Values with Confidence Intervals')
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            forecast_image = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()
            
            # Plot comparison between actual and forecasted values
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(df['ds'], scaler.inverse_transform(df[['y']]), label='Actual')
            ax.plot(forecast['ds'], forecast['yhat'], label='Forecast')
            ax.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='gray', alpha=0.2)
            ax.set_xlabel(xlabel_val)
            ax.set_ylabel(ylabel_val)
            plt.title('Comparison between Actual and Forecasted Values')
            plt.legend()
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            comparison_image = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()

            return render(request, 'forecast.html', {
                'form': form,
                'historical_data_image': historical_data_image,
                'forecast_image': forecast_image,
                'comparison_image': comparison_image,
                'forecast_data': forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_html(),
                'mse': mse,
                'rmse': rmse,
                'mae': mae,
                'r2': r2,
            })
    else:
        form = ForecastForm()
    
    return render(request, 'forecast.html', {'form': form})# views.py
