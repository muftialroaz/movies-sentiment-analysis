import streamlit as st
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Title and project description
st.title('Movies Sentiment Analysis')
st.text('The Movie Sentiment Analysis project aims to analyze user sentiments or opinions about movies based on a dataset obtained from Kaggle. This dataset consists of a collection of user reviews about various films, which are associated with positive or negative sentiment labels.')

# User input for movie review
label = "Type the reviews"
reviews = st.text_area(label, value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder="Type the reviews", disabled=False, label_visibility="visible")

# Load dataset and model
try:
    preprocess = pd.read_csv('dataset/preprocess_movies_20k.csv')
    target_0 = preprocess[preprocess['label'] == 0].head(5000)
    target_1 = preprocess[preprocess['label'] == 1].head(5000)
    k_samples = pd.concat([target_0, target_1], axis=0)

    # Load the trained model and the vectorizer
    lr_model = pickle.load(open('model/lr_model.pkl', 'rb'))
    vectorizer = pickle.load(open('model/tfidf_vectorizer.pkl', 'rb'))  # Assuming you saved the vectorizer separately

except FileNotFoundError:
    st.error("Dataset or model files are missing. Please check the file paths.")
    st.stop()

# Display sample data for review
# st.dataframe(k_samples)

# Predict sentiment and confidence score if reviews are provided
if reviews:
    if reviews.strip():  # Check if the input is not empty
        tfidf = vectorizer.transform([reviews])  # Transform the user input
        y_pred = lr_model.predict(tfidf)
        y_prob = lr_model.predict_proba(tfidf)  # Get the predicted probabilities
        
        # The probability for class 1 (positive sentiment) is the second column in the output
        positive_prob = y_prob[0][1]
        
        # Display the sentiment result with confidence score
        if y_pred[0] == 1:
            st.success(f"Sentiment: Positive | Confidence: {positive_prob * 100:.2f}%")
        else:
            negative_prob = y_prob[0][0]
            st.error(f"Sentiment: Negative | Confidence: {negative_prob * 100:.2f}%")
    else:
        st.warning("Please enter a review to get the sentiment.")
