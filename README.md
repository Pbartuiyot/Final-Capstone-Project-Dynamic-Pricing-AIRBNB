# Final-Capstone-Project-Dynamic-Pricing-AIRBNB
Sentiment Analysis of Airbnb Reviews to Inform Dynamic Pricing for Listings in Paris

# Problem Statement
Airbnb hosts in Paris struggle to attract guests due to poor pricing, limited visibility, and listings that don't highlight local attractions or unique features. Without proper data analytics, many set prices that are either too high, driving away bookings, or too low, hurting profitability. This limits Airbnb’s growth and undermines local economic benefits while missing opportunities to promote Paris’s cultural heritage. Unlike hotels that rely on brand recognition, Airbnb guests depend on user reviews and listing details to gauge value, often willing to pay more for well-rated properties. However, hosts don’t have clear guidance on which features, like location, amenities, or host responsiveness, affect guest satisfaction and pricing. 
I aim to use guest feedback and listing data to identify factors that enhance guest satisfaction and optimize pricing and ratings for Airbnb listings in Paris. By analyzing reviews, proximity to attractions, seasonal demand, and host service quality, we will extract key insights. Natural language processing (NLP) will help identify what guests value, their expectations, and improvement areas. This will enable hosts to set competitive prices that balance occupancy and profitability. - Improve listing quality based on guest preferences. Increase visibility by showcasing unique features and local attractions.

# Source for the data 
To address this issue, I will collect a dataset from an insider website which provides datasets or short-stay rentals across major cities, which offers hosts to list their short-stay rental houses and also allows customers to leave reviews and ratings. The following are characteristics of the data: 
     i) Listing Details: Title, property type (e.g., apartment, house), number of bedrooms/bathrooms, amenities (e.g., Wi-Fi, pool)
     ii) Pricing: Nightly rate, discounts, service fees
     iii) Location: County, city, or specific coordinates
     iv) Reviews: Ratings, number of reviews, guest comments
     v) Host Information: Name, response rate, superhost status
     vi) Availability: Booked/unbooked dates.

# Methodology
I will pre-process the raw Airbnb review data by removing noise (e.g., punctuation, emojis, etc) and standardizing the text through lowercasing and spell-checking. Using natural language processing (NLP) with tools like NLTK or spaCy, I will tokenize the reviews, remove stopwords, and apply lemmatization to normalize words.
Next, I will extract numerical features from the listings (e.g., price, number of bedrooms) and encode categorical variables (e.g., property type) using one-hot encoding. For sentiment analysis, I will employ BERT to classify reviews as positive, negative, or neutral, assigning sentiment scores ranging from -1 to +1, which will be aggregated per listing to inform pricing analysis. I will then build a regression-based pricing model using ensemble techniques like Random Forest or XGBoost, incorporating sentiment scores along with predictors such as location, demand trends, and competitor prices. To optimize the model, I will tune hyperparameters (e.g., tree depth, learning rate) and validate performance with cross-validation. I will also analyze feature importance to pinpoint key pricing influencers.
To evaluate the model’s effectiveness, I will use metrics like Mean Squared Error (MSE) and R-squared (R²) to ensure accurate price predictions. For interpretability, I will leverage SHAP values to illustrate how sentiment and other features affect pricing decisions. Finally, I will deploy the model as a scalable pricing tool, integrating it with Airbnb host dashboards to enable real-time price adjustments.
Data-driven recommendations will help hosts enhance guest experiences, increase revenue, and boost Airbnb’s presence in Paris. This approach will also promote the city’s culture and tourism to a global audience, driving local economic growth.
