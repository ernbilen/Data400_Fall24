# Analysis of Consumer Preferences and Trends for Foundation at Sephora

## Project Overview
This project focuses on understanding and analyzing foundation products in the beauty industry. The analysis includes:

**Price Prediction:** Leveraging regression techniques to predict the price of foundation products based on their features.

**Product Clustering:** Grouping products based on their price and reviews to identify patterns and similarities.

**Popularity Classification:** Classifying products as popular or not based on reviews, ratings, and other relevant features.

## Table of Contents
* Installation
* Dataset
* Exploratory Data Analysis (EDA)
* Methods
* Results
* Conclusion
* Future Work

## Installation
To run the analysis, ensure you have the following installed:
* Python 3.8+
* Jupyter Notebook

### Libraries:
* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* xgboost

## Dataset
The dataset consists of foundation product details, including:
* Product name
* Price
* Ratings
* Number of reviews
* Brand name
* Number of colors available
* Whether the product is Sephora Exclusive
* Whether the product is Limited Edition
* Whether the product is Natural
* Whether the product is Organic
* Whether the product is Sponsored

## Exploratory Data Analysis (EDA)
### Key insights from the data:
**Price Distribution:** Most foundation products fall within the 10 - 50 (dollars) range. There is an outlier of > 100 dollars.

**Ratings & Reviews:** Higher-rated products tend to have more reviews, but price does not always correlate with rating.

**Popular Brands:** Certain brands dominate the market, influencing pricing and popularity trends.

EDA visualizations are available in the notebook and include:

* Histograms for price and review distributions.

* Heatmaps for feature correlations.

## Methods
### Price Prediction
**Objective:** Predict product prices using features like brand, reviews, and ratings.

**Techniques:** Applied Random Forest Regressor model.

**Metrics:** Evaluated using RMSE and R².

### Product Clustering
**Objective:** Identify groups of similar products based on price and reviews.

**Techniques:**

K-Means Clustering to segment products.

Elbow method to determine the optimal number of clusters.

### Popularity Classification
**Objective:** Classify products into "Popular" and "Not Popular" categories.

**Techniques:**

Binary classification model: Random Forest Classifier.

Feature engineering to create popularity metrics.

Performance measured with Precision, Recall, and F1 Score.

## Results
### Price Prediction
**Best model:** RMSE of 3.93 and R² of 0.88.

Features such as rating, brand name, and reviews were highly predictive of price.

### Product Clustering
**Optimal clusters:** 2 distinct groups, visualized through scatter plots.

**Observations:**

Cluster 0: Wider price range with low to moderate number of reviews.

Cluster 1: Lower price range with higher review counts.

### Popularity Classification
Best model: Random Forest Classifier achieving accuracy of 0.96.

Features such as review count and rating were highly predictive of popularity.

## Conclusion
This project provides actionable insights into the beauty industry's foundation product segment. The models accurately predict prices, group similar products, and identify popular items, aiding brands and consumers in decision-making.

## Future Work
* Incorporate additional product features such as ingredients and packaging information.
* Expand the dataset to include a wider range of beauty products.
* Develop a web application for real-time price prediction and popularity analysis.


```python

```
