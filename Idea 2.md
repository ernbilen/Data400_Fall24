# Idea 2
### Research Question:
How can Formula 1 teams optimize race strategies (pit stops, tire choices, and lap timings) based on track conditions (temperature, weather, etc.) to improve performance and outcomes?

### Data Source:
Data will be retrieved using the Ergast Developer API (the API is deprecated, but it will still be updated until the end of the 2024 season. For alternative options there are F1 databases on Kaggle, and the open source database f1db), which provides access to detailed historical F1 race data. The project will utilize data from the last 10 F1 World Championships (from 2014 - V6 engine era). Key variables include:
* Pit Stop Data: Time of pit stop according to the race (pit on which lap), tire type on each stint, and number of pit stops.
* Track Conditions: Temperature, wind speed, humidity, and rain data.
* Race Results: Starting and finishing positions, lap times, race duration.
* Tire Strategy: The type of tire used during the race (soft, medium, hard) and the order in which they are used.
* Driver Performance: Driver lap times and overall performance in the race as well as in the championships.

### Data Processing and Model Specification:
I will perform exploratory data analysis (EDA) to identify correlations between track conditions and race outcomes. Based on the insights, I will employ a combination of regression models and classification algorithms:
* Linear Regression to predict optimal pit stop times.
* Decision Trees to recommend the best tire strategies based on weather patterns.

### Implications for Stakeholders:
This project will help F1 teams optimize their race strategies by predicting the best possible outcomes given specific track conditions. It can:
* Minimize pit stop times and avoid unnecessary stops.
* Optimize tire choices to suit the conditions, thus improving lap times.
* Provide teams with a data-driven approach to enhance performance.

### Ethical, Legal, and Societal Implications:
* Environmental Impact: Optimizing tire usage reduces waste, which aligns with FIA’s sustainability goals.
* Fan Experience: Help F1 fans gain a deeper understanding of race strategy and how different factors of a race can affect which strategy is optimal. This will highlight a much underrated interesting aspect of the sport, which might appeal to new groups of fans, thus create opportunity for the sport to expand to new markets.
* Data Privacy: Ensure all data retrieval follows the API's and the FIA's legal guidelines, protecting driver and team information.
