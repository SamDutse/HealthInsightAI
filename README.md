## Health Insight AI: Disease Prediction with Streamlit 

**Live Demo:** [Health Insight AI](https://healthinsightai-oltxsewshkj9dha2ylwd8k.streamlit.app/)

This repository contains the code for Health Insight AI, a machine learning model that predicts potential diseases based on user-provided symptoms. The project is deployed on Streamlit, allowing users to interact with the model and receive disease probabilities.

### Project Description

Health Insight AI utilizes Natural Language Processing (NLP) techniques to process symptom text data. Here's a breakdown of the approach:

1. **Data Preprocessing:** Combines various symptoms into a single text feature for each data point.
2. **TF-IDF Vectorization:** Transforms the symptom text data into numerical features using TF-IDF, a common NLP technique.
3. **Model Training:** Trains a Random Forest Classifier model to identify relationships between symptom patterns and diseases.
4. **Streamlit Deployment:** Creates a user interface using Streamlit for users to input symptoms and view predicted disease probabilities.

**Key Features:**

* **Disease Prediction:** Predicts potential diseases based on user-provided symptoms.
* **User-Friendly Interface:** Streamlit interface allows for easy interaction and result visualization.
* **Privacy Focused:** The model prioritizes user privacy and does not collect any personal health information (if applicable).

### Technologies Used

* Python (programming language)
* Scikit-learn (machine learning library)
* Streamlit (web framework)

###  Model Performance (Optional)

**Accuracy and Classification Report (Optional):**

Accuracy: 1.0
Classification Report:
| Disease | precision | recall | f1-score | support |
|---|---|---|---|---|
| (vertigo) Paroymsal Positional Vertigo | 1.00 | 1.00 | 1.00 | 18 |
| AIDS | 1.00 | 1.00 | 1.00 | 30 |
| Acne | 1.00 | 1.00 | 1.00 | 24 |
| Alcoholic hepatitis | 1.00 | 1.00 | 1.00 | 25 |
| Allergy | 1.00 | 1.00 | 1.00 | 24 |
| Arthritis | 1.00 | 1.00 | 1.00 | 23 |
| Bronchial Asthma | 1.00 | 1.00 | 1.00 | 33 |
| Cervical spondylosis | 1.00 | 1.00 | 1.00 | 23 |
| Chicken pox | 1.00 | 1.00 | 1.00 | 21 |
| Chronic cholestasis | 1.00 | 1.00 | 1.00 | 15 |
| Common Cold | 1.00 | 1.00 | 1.00 | 23 |
| Dengue | 1.00 | 1.00 | 1.00 | 26 |
| Diabetes | 1.00 | 1.00 | 1.00 | 21 |
| Dimorphic hemmorhoids(piles) | 1.00 | 1.00 | 1.00 | 29 |
| Drug Reaction | 1.00 | 1.00 | 1.00 | 24 |
| Fungal infection | 1.00 | 1.00 | 1.00 | 19 |
| GERD | 1.00 | 1.00 | 1.00 | 28 |
| Gastroenteritis | 1.00 | 1.00 | 1.00 | 25 |
| Heart attack | 1.00 | 1.00 | 1.00 | 23 |
| Hepatitis B | 1.00 | 1.00 | 1.00 | 27 |
| Hepatitis C | 1.00 | 1.00 | 1.00 | 26 |
| accuracy | 1.00 |  -  |  -  | 984 |
| macro avg | 1.00 | 1.00 | 1.00 | 984 |
| weighted avg | 1.00 | 1.00 | 1.00 | 984 |
