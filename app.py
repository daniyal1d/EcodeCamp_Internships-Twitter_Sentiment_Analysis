import streamlit as st
import pickle
import time

st.title("Twitter Sentiment Analysis")

# load model
model = pickle.load(open('trained_model.sav', 'rb'))

tweet = st.text_input("Enter Your Tweet")

submit = st.button('Predict')

if submit:
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()
    st.write('Prediction Time Taken :', round(end-start, 2), 'Seconds')
    print(prediction[0])
    st.write("Predicted Sentiment is: ", prediction[0])
