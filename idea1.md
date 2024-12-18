Project Proposal: Local Temperature and Precipitation Trends Analysis in Cumberland County, PA 

1. Research Question 

How have average annual temperature, the frequency of extreme heat days (above 90°F), and total annual precipitation changed in Cumberland County, PA, over the past 50 years (1973–2023), and how are these trends expected to continue or accelerate in the next 30 years (2024–2054)? 

Specifically, I aim to quantify the rate of change in average annual temperature, the frequency of extreme temperature events, and shifts in precipitation patterns. This project will provide actionable insights for public health officials, local farmers, and water resource managers to adapt to these changing climate conditions. 

2. Data Source 

The primary data source for this project will be the National Oceanic and Atmospheric Administration (NOAA) Climate Data Online portal, which provides access to historical weather data for the United States, including temperature and precipitation records. 

Data Retrieval Process: The data will be accessed by querying the NOAA Climate Data Online portal, specifying Cumberland County, PA, as the location, with a time range from 1973 to 2023. Data will be downloaded in CSV format to then load into Python. 

Variables in the Dataset: 

Temperature Variables: Daily maximum temperature, daily minimum temperature, and daily average temperature. 

Precipitation Variables: Daily total precipitation and the occurrence of extreme precipitation events (e.g., days with precipitation exceeding 1 inch). 

Other Variables: Date, location, and potential weather station data 

Variables to Be Created: 

Annual/Seasonal Averages: Calculate annual and seasonal averages for temperature and precipitation. 

Trends and Anomalies: Create variables that measure the rate of change over time and identify anomalies (unusually hot or wet years, etc.). 

Extreme Event Frequency: Count the number of days per year with temperatures above 90°F and precipitation above 1 inch to identify the frequency of extreme weather events. 

3. Data Analysis and Model Specification 

Exploratory Data Analysis (EDA): 

Initial analysis will involve data cleaning and visualization. Descriptive statistics and plots (line graphs, boxplots) will be used to understand the distribution of temperature and precipitation over time. Temporal trends can be assessed through moving averages and yearly comparisons. 

Model Specification: 

To project future trends, a time series regression model will be employed (thinking of using Ordinary Least Squares regression) with temperature and precipitation as dependent variables and time (year) as the independent variable. I can also explore the use of Autoregressive Integrated Moving Average (ARIMA) models for forecasting future climate patterns. 

Implications for Stakeholders: 

The results of this analysis will provide valuable insights for local stakeholders, such as agricultural managers, public health officials, and municipal planners, to anticipate and mitigate the impacts of climate change on farming and water management. For example, identifying an increasing trend in extreme heat days could prompt local authorities to invest in heat mitigation strategies or guide farmers on crop selection. Dickinson is also very involved with climate initiatives with Carlisle and Cumberland County, some which I have been a part of before. 

Ethical, Legal, and Societal Implications: 

Ethical considerations include ensuring that the data is used in ways that accurately represent the findings. There are no significant legal barriers to using NOAA data, as it is publicly accessible. However, the societal implications of the findings, such as the potential need for adaptation strategies, will be carefully communicated to ensure that stakeholders can make informed decisions. 


