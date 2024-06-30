import streamlit as st
import joblib

# Load the model and vectorizer
model = joblib.load('disease_prediction_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Function to make a prediction
def predict_diseases(symptoms, top_n=5):
    # Preprocess the input symptoms
    symptoms_str = ' '.join(symptoms)
    symptoms_tfidf = vectorizer.transform([symptoms_str])
    
    # Make predictions
    probabilities = model.predict_proba(symptoms_tfidf)[0]
    
    # Get the top N predictions
    top_indices = probabilities.argsort()[-top_n:][::-1]
    top_diseases = model.classes_[top_indices]
    top_probabilities = probabilities[top_indices]
    
    return list(zip(top_diseases, top_probabilities))

# Streamlit app
st.title("Disease Prediction Based on Symptoms")
st.write("Enter the symptoms you are experiencing, separated by commas.")

# Input symptoms
symptoms_input = st.text_input("Symptoms", "")

if st.button("Predict"):
    if symptoms_input:
        symptoms_list = [symptom.strip() for symptom in symptoms_input.split(',')]
        predictions = predict_diseases(symptoms_list)
        
        st.write("Possible Diseases and Probabilities:")
        for disease, probability in predictions:
            st.write(f"{disease}: {probability:.2f}")
    else:
        st.write("Please enter symptoms.")
