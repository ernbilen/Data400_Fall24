# Detecting Problematic Internet Usage in Adolescents

## 1) Research Question

How can we develop a machine learning model to accurately detect problematic internet usage patterns in adolescents using smartphone sensor data?

## 2) Data Source

The primary data source for this project is the [dataset](https://www.kaggle.com/competitions/child-mind-institute-problematic-internet-use/data) provided by the Child Mind Institute in their Kaggle competition "Detect Problematic Internet Usage". This dataset includes:

- Accelerometer data
- Gyroscope data
- Screen state (on/off) information
- Timestamps for each data point
- Labels indicating periods of problematic internet usage

## 3) Discussion

This project aims to create a machine learning model that can identify patterns of problematic internet usage in adolescents using smartphone sensor data. This has important applications in mental health, particularly in early intervention and prevention of internet addiction among young people.

Key steps in the project would include:

1. **Exploratory Data Analysis**
   - Analyze the distribution of problematic usage periods
   - Examine patterns in accelerometer and gyroscope data
   - Visualize screen state patterns over time
   - Investigate correlations between sensor data and problematic usage

2. **Data Preprocessing**
   - Handle missing data points
   - Normalize accelerometer and gyroscope readings
   - Create time-based features (e.g., time of day, day of week)
   - Generate rolling statistics (mean, variance) over different time windows

3. **Feature Engineering**
   - Extract relevant features from raw sensor data
   - Create features based on screen state transitions
   - Develop features that capture prolonged periods of inactivity or constant motion
   - Incorporate frequency domain features using Fourier transforms

4. **Model Development**
   - Split data into training and validation sets
   - Experiment with different algorithms:
     - Traditional ML: Random Forest, Gradient Boosting, SVM
     - Deep Learning: LSTM, 1D CNN, Transformer models
   - Implement time series cross-validation
   - Use techniques like hyperparameter tuning and ensemble methods

5. **Model Evaluation**
   - Evaluate models using competition metric (Average Precision)
   - Analyze false positives and false negatives
   - Assess model performance across different times of day and days of week

6. **Interpretability and Insights**
   - Use techniques like SHAP values to understand feature importance
   - Identify key patterns that indicate problematic usage
   - Provide actionable insights for intervention strategies

Potential challenges include dealing with imbalanced data, handling varying smartphone usage patterns across individuals, and ensuring privacy and ethical considerations in model deployment.
.
