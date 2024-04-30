import streamlit as st
import joblib

# Load the trained model
model = joblib.load("sentiment-model.pkl")
#define sentiment labels
sentiment_labels ={'1': 'Positive', '0':'Negative'}
# Create streamlit app
st.title("Sentiment Analysis")
# input tyext area
user_input = st.text_area("Enter your text here:")
#prediction button
if st.button("predict"):
    #perform sentiment prediction
    print(user_input)
    predicted_sentiment = model.predict([user_input])[0]
    print("predicted Label:" + str(predicted_sentiment))
    predicted_sentiment_label = sentiment_labels[str(predicted_sentiment)]

    #display predicted sentiment
    st.info(f"predicted Sentiment: {predicted_sentiment_label}")
