##  Running the Application:
0.  Install the python and pip on the system.
Python 3.10.13
pip 24.2 
git bash
1.  Navigate to the correct project/application folder
cd forecastProphet2
2.   Create the virtual environment
python -m venv myenv
3.  Activate the local virtual environment
myenv\Scripts\activate
4.  Install the dependencies from the requirements.txt file
pip install -r requirements.txt
5.  Run the server
python manage.py runserver
6.  Navigate to Url to run the application
http://127.0.0.1:8000/forecast/


## Chosen dataset and the forecasting model used:
1.  Source: The dataset is sourced from Kaggle, a popular platform for data science and machine learning datasets.
2.  Format: The dataset is provided in CSV (Comma-Separated Values) format, which is easy to read and process using Python libraries like pandas.
3.  Content: The dataset includes historical data relevant to the forecasting task. Depending on the selected dataset, it may contain:
-   Sales Data: Historical sales data for a retail store, including dates and sales figures.
-   Temperature Data: Monthly average temperatures for a specific location, including dates and temperature readings.
-   Stock Prices: Historical stock prices for a specific company, including dates and closing prices.
4.  Preprocessing: The dataset is preprocessed to handle missing values, outliers, and normalization. This ensures that the data is clean and suitable for accurate forecasting.
5.  Renaming and Adjustments: The dataset has been renamed, and the columns used have been adjusted to fit the requirements of this project.


##  Reasons for Selecting the Prophet Model
1.  Ease of Use:
Prophet is designed to be easy to use for both experts and non-experts in time series forecasting.
It provides a simple interface for fitting and predicting time series data.
2.  Handling Missing Data:
Prophet can handle missing data and outliers effectively, making it robust for real-world datasets.
3.  Automatic Seasonality Detection:
Prophet automatically detects and models daily, weekly, and yearly seasonality.
It allows for custom seasonalities to be added if needed.
4.  Flexibility:
Prophet allows for the inclusion of holidays and special events, which can significantly impact the forecast.
It supports custom seasonalities and changepoints, providing flexibility in modeling complex time series.
5.  Scalability:
Prophet is scalable and can handle large datasets efficiently.
It is designed to work well with both short and long time series data.
6.  Interpretability:
The model provides interpretable parameters, making it easier to understand the underlying patterns in the data.
It offers clear visualizations of the forecast components (trend, seasonality, holidays).
7.  Robustness:
Prophet is robust to missing data and shifts in the trend, making it suitable for various types of time series data.
It can handle outliers and anomalies in the data without significant impact on the forecast.
8.  Open Source and Well-Maintained:
Prophet is an open-source library developed and maintained by Facebook.
It has a strong community and extensive documentation, making it a reliable choice for time series forecasting.


##  Selection of Forecasting Model Based on Dataset
1.	Daily Sales Data for a Retail Store:
o	Characteristics:
	High frequency (daily data).
	Potential for strong seasonality (weekly, monthly, yearly).
	Possible presence of holidays and special events affecting sales.
o	Recommended Models:
	Prophet:
	Reason: Prophet is well-suited for handling daily data with multiple seasonalities and holidays. It automatically detects and models daily, weekly, and yearly seasonality.
	ARIMA:
	Reason: ARIMA can be effective for time series data with strong autocorrelation. It is suitable for data with a clear trend and seasonality.
	LSTM:
	Reason: LSTM can capture complex patterns and dependencies in the data. It is useful for modeling non-linear relationships and long-term dependencies.
2.	Monthly Average Temperatures:
o	Characteristics:
	Lower frequency (monthly data).
	Strong yearly seasonality.
	Potential for long-term trends due to climate change.
o	Recommended Models:
	Prophet:
	Reason: Prophet is effective for handling yearly seasonality and long-term trends. It can model the yearly cycle of temperature changes.
	ARIMA:
	Reason: ARIMA can be used for time series data with strong autocorrelation and seasonality. It is suitable for modeling the monthly temperature data.
	LSTM:
	Reason: LSTM can capture complex patterns and dependencies in the data. It is useful for modeling non-linear relationships and long-term trends.
3.	Historical Stock Prices for a Specific Company:
o	Characteristics:
	High frequency (daily data).
	Potential for high volatility and noise.
	Influence of external factors (market trends, economic indicators).
o	Recommended Models:
	LSTM:
	Reason: LSTM is well-suited for capturing complex patterns and dependencies in financial data. It can model non-linear relationships and long-term dependencies.
	ARIMA:
	Reason: ARIMA can be effective for time series data with strong autocorrelation. It is suitable for modeling the trend and seasonality in stock prices.
	Prophet:
	Reason: Prophet can handle daily data with multiple seasonalities. It is useful for modeling long-term trends and seasonality in stock prices.


##  Forecasted Values with Confidence Intervals
1.  Definition:
-   Forecasted Values: These are the predicted values generated by the forecasting model for future time periods based on historical data.
-   Confidence Intervals: These are the ranges within which the true values are expected to fall with a certain level of confidence (e.g., 95%). They provide an estimate of the uncertainty associated with the forecasted values.
2.  Importance:
-   Uncertainty Quantification: Confidence intervals help quantify the uncertainty in the predictions, providing a range of possible outcomes rather than a single point estimate.
-   Decision Making: By understanding the range of possible future values, stakeholders can make more informed decisions and plan for different scenarios.
-   Model Evaluation: Confidence intervals can be used to evaluate the reliability and robustness of the forecasting model.
3.  Calculation:
-   The Prophet model generates confidence intervals by simulating future values based on the historical data and the model's parameters.
-   The width of the confidence intervals depends on the variability in the historical data and the model's assumptions about future trends and seasonality.
4.  Interpretation:
-   A narrower confidence interval indicates higher confidence in the forecasted values, while a wider interval indicates greater uncertainty.
-   If the actual future values fall within the confidence intervals, it suggests that the model's predictions are reliable.
5.  Visualization:
-   Confidence intervals are typically visualized as shaded areas around the forecasted values in a time series plot.
-   This visualization helps to clearly communicate the range of possible future values and the associated uncertainty.


## Challenges faced during implementation:
Usual coding issue were there like handing of decrapeted libraries, finding of the required dataset, selecting the prophet model, date coverting issue, handling dollar sign along with string which needs to be converted to float


##  Project Structure
sales_forecasting/
├── manage.py
├── sales_forecasting/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── forecast_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│       └── __init__.py
└── templates/
    └── forecast.html


## Files Description:-
forms.py: Contains the form for user input.
views.py: Contains the view logic for handling form submission and generating forecasts.
forecast.html: Template for displaying the form and forecast results.
urls.py: Contains URL routing for the forecast view.


##   Commonly Used Metrics for Time Series Forecasting
1.  Mean Squared Error (MSE):
-   Definition: The average of the squared differences between the actual and predicted values.
-   Formula: ( \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 )
-   Usage: MSE is useful for penalizing larger errors more than smaller ones due to the squaring of differences.

2.  Root Mean Squared Error (RMSE):
-   Definition: The square root of the mean squared error.
-   Formula: ( \text{RMSE} = \sqrt{\text{MSE}} )
-   Usage: RMSE provides a measure of the average magnitude of the errors in the same units as the original data.

3.  Mean Absolute Error (MAE):
-   Definition: The average of the absolute differences between the actual and predicted values.
-   Formula: ( \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| )
-   Usage: MAE is useful for understanding the average magnitude of the errors without considering their direction.

4.  R-squared (R²) or Coefficient of Determination:
-   Definition: A statistical measure that represents the proportion of the variance for a dependent variable that's explained by an independent variable or variables in a regression model.
-   Formula: ( R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}i)^2}{\sum{i=1}^{n} (y_i - \bar{y})^2} )
-   Usage: R² indicates how well the model's predictions approximate the actual data points. An R² of 1 indicates perfect predictions, while an R² of 0 indicates that the model does not explain any of the variability in the response data.

##  Choosing the Right Metric
-   MSE and RMSE: These metrics are useful when you want to penalize larger errors more heavily. RMSE is particularly useful when you want the error metric to be in the same units as the original data.
-   MAE: This metric is useful when you want to understand the average magnitude of the errors without considering their direction. It is less sensitive to outliers compared to MSE and RMSE.
-   R-squared: This metric is useful when you want to understand how well the model explains the variability in the data. It provides a measure of the goodness of fit of the model.


#	Code quality and organization
1.  Consistent Indentation: Ensure consistent indentation throughout the file.
2.  Remove Unnecessary Comments: Remove commented-out code that is not needed.
3.  Use Functions for Repeated Code: Extract repeated code into functions to avoid redundancy.
4.  Add Comments and Docstrings: Add comments and docstrings to explain the purpose of the code.
5.  Organize Imports: Ensure imports are organized and grouped logically.
6.  Add Comments and Docstrings: Added a docstring to explain the purpose of the ForecastForm class.
