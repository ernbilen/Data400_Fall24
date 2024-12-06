Idea 2 

1. Research Question: 

How do specific ingredients in skincare products correlate with their perceived effectiveness, as measured by consumer reviews and ratings? Specifically, do commonly marketed "active ingredients" like retinol, vitamin C, and hyaluronic acid result in higher consumer satisfaction and ratings compared to products without these ingredients? 

This question aims to provide insight into the actual performance of ingredients, highlighting user experiences. 

 

2. Data Source: 

Primary Data Source: 

Sephora (Scraping Reviews and Product Listings): 

Variables Collected: 

Product name, brand, price 

User ratings (average rating and number of reviews) 

Product description and ingredient lists 

Review texts (for sentiment analysis) 

"Best-seller" or "Clean at Sephora" labels (if available) 

Potential Data Source: 

CosDNA & EWG Skin Deep: 

Variables: 

Ingredient details and safety ratings 

Ingredient classifications  

Data Retrieval Process: 

Scraping Tools: I will use Python libraries to scrape product details from Sephora's website. 

Variables Created: 

Binary features for the presence of specific active ingredients (retinol: yes/no). 

Sentiment scores from reviews using Natural Language Processing. 

Price per unit (price per ounce or mL for skincare products). 

 

3. What I Will Do with the Data: 

Exploratory Data Analysis (EDA): 

Descriptive Statistics: Summarize the distributions of prices, ratings, and key ingredient presence across product categories. 

Correlation Analysis: Explore the relationships between the presence of active ingredients and product ratings, controlling for price and brand. 

Model Specification: 

Model Choice: 

Sentiment Analysis: 

Purpose: Convert review text into sentiment scores to assess overall user satisfaction. 

Clustering Models: 

Model: K-Means Clustering or Hierarchical Clustering to group ingredients based on their impact on ratings and effectiveness. 

Purpose: Identify patterns and groupings among ingredients to analyze their collective influence. 

Regression Models: 

Model: Linear Regression to model the relationship between ingredient presence and ratings. 

Purpose: Predict how individual ingredients impact ratings, controlling for price and product category. 

Stakeholder Implications: 

For consumers: Provide data-backed insights into which ingredients actually improve product satisfaction. 

For brands: Help product developers focus on the most effective ingredients. 

For dermatologists: Insights could help guide patient recommendations based on user experiences. 

Ethical, Legal, and Societal Implications: 

Ethical Considerations: Ensure transparency in the analysis by avoiding biased interpretations of ingredient effectiveness. Address the influence of marketing in reviews.  

Legal Considerations: Scraping terms of use for websites must be reviewed, ensuring no violation of policies. 

Societal Implications: The project can improve consumer decision-making, promoting ingredient awareness and reducing the impact of misleading marketing claims. 

 

1. Research Question: 

How do color and pattern trends in the fashion industry evolve over time, and can historical trend data be used to predict future fashion trends? Specifically, what role do recurring color palettes and patterns play in the popularity of fashion collections in different seasons? 

This project aims to analyze the evolution of fashion trends through color and pattern analysis and provide insights for fashion brands on which aesthetics are likely to become popular in future seasons. 

 

2. Data Source: 

Primary Data Source: 

Fashion Runway Archives: Publicly available images from fashion weeks (e.g., New York, Paris, Milan), accessible via online databases or fashion blogs. 

Variables Collected: 

Image Data: Photos of fashion collections from different designers across various seasons. 

Timestamp: The season and year of the fashion show (e.g., Spring/Summer 2023). 

Designer Name: The designer or fashion house associated with the collection. 

Clothing Type: The category of clothing (e.g., dresses, outerwear, accessories). 

Color and Pattern: Identified using image processing techniques (e.g., dominant colors, pattern types). 

Potential Data Source: 

Online Fashion Retailers: Websites like Net-a-Porter or Farfetch that display collections from top designers. 

Variables Collected: 

Product Descriptions: Text descriptions that may highlight color or pattern features. 

Sales Data (if available): Pricing and sales metrics that could link color trends to commercial success. 

Data Retrieval Process: 

Image Data Collection: Use python web scraping tools to collect fashion week images from public sources like Vogue’s fashion archives. 

Image Processing Tools: Apply computer vision libraries (e.g., OpenCV, PIL) to extract color palettes and patterns from each image. 

Variables Created: 

Dominant Colors: Extracted from images using clustering techniques (K-Means) to identify the most prominent colors in each collection. 

Pattern Detection: Identify repeating patterns (stripes, florals, polka dots) using feature extraction methods such as texture analysis and edge detection. 

 

3. What I Will Do with the Data: 

Exploratory Data Analysis (EDA): 

Descriptive Statistics: Analyze the frequency of different colors and patterns over time, grouped by season and designer. 

Trend Analysis: Identify the most recurring colors and patterns across multiple seasons and designers, and analyze the correlation between these trends and the success of a collection (if sales data is available). 

Model Specification: 

Model Choice: 

Time Series Forecasting: 

Purpose: To predict future fashion trends by modeling the historical popularity of colors and patterns over time. 

Independent Variables: Color, pattern, designer, season, and clothing type. 

Dependent Variable: Trend popularity (measured by frequency or sales performance). 

Clustering Models: 

K-Means Clustering: 

Purpose: To group fashion collections by similar color palettes and patterns, helping to uncover underlying aesthetic trends. 

Evaluation Metrics: Root Mean Squared Error (RMSE) for time series forecasting and silhouette score for clustering to evaluate the model’s performance. 

 

4. Stakeholder Implications: 

For Fashion Designers: The analysis can inform future collection designs by identifying which color and pattern combinations are likely to resonate with consumers in upcoming seasons. 

For Retailers: Retailers can use trend predictions to stock their inventory with trending colors and patterns ahead of time, optimizing sales and reducing unsold stock. 

For Consumers: Trend analysis can help fashion-conscious consumers anticipate what styles will be in demand, allowing them to stay ahead of the curve. 

 

5. Ethical, Legal, and Societal Implications: 

Ethical Considerations: Ensure fair representation of fashion across diverse cultures and designers, avoiding bias toward certain trends based on geographic or demographic factors. 

Legal Considerations: Ensure compliance with copyright laws when scraping and analyzing fashion show images. Review terms of use for image databases and retailer websites. 

Societal Implications: The project could influence the sustainability of fashion by promoting timeless color and pattern choices, reducing the rapid turnover of trends that lead to excessive consumption and waste. 

 

