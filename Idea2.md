# Idea 2: Detecting Fake Disaster Tweets

## 1) Research Question

How can we develop an accurate machine learning model to classify disaster-related tweets as real or fake?

## 2) Data Source

The primary data source for this project would be the ["Natural Language Processing with Disaster Tweets"](https://www.kaggle.com/competitions/nlp-getting-started/data) dataset from Kaggle. This dataset contains:

- Labeled tweets classified as real disaster tweets or fake/non-disaster tweets
- Tweet text
- Keywords
- Location information (where available)

Additional data could potentially be gathered from Twitter's API to expand the dataset if needed.

## 3) Discussion

This project aims to develop a machine learning model that can accurately distinguish between real disaster-related tweets and fake or non-disaster tweets. This has important applications for disaster response organizations, news agencies, and emergency services who rely on social media for real-time information during crises.

Key steps in the project would include:

1. **Exploratory Data Analysis**
   - Analyze the distribution of real vs fake tweets
   - Examine tweet length, word frequencies, and other text characteristics
   - Visualize common words and n-grams in real and fake tweets

2. **Data Preprocessing**
   - Clean text data (remove URLs, special characters, etc.)
   - Tokenization and lemmatization
   - Remove stop words
   - Convert text to numerical features (e.g., using TF-IDF or word embeddings)

3. **Model Development**
   - Split data into training and test sets
   - Experiment with different algorithms:
     - Traditional ML: Naive Bayes, Random Forest, SVM
     - Deep Learning: LSTM, Bidirectional LSTM, BERT
   - Use techniques like cross-validation and hyperparameter tuning

4. **Model Evaluation**
   - Compare model performance using metrics like accuracy, precision, recall, F1-score
   - Analyze confusion matrix to understand model errors
   - Perform error analysis on misclassified tweets

5. **Deployment**
   - Develop a simple web application to classify new tweets
   - Deploy the model into pickle file

Potential challenges include dealing with class imbalance, handling out-of-vocabulary words, and generalizing to new disaster types. The project could be extended by incorporating additional features like user metadata or tweet engagement metrics.

This project would provide valuable insights into the characteristics of real and fake disaster tweets and contribute to more effective social media monitoring during emergencies.
