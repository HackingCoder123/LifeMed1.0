import streamlit as st
import pandas as pd
import pickle
import numpy as np


st.title('Disease Prediction app')

st.sidebar.header('Heart')
def predict_disease(input_df):
    prediction = load_clf.predict(input_df)
    return prediction

# Collects user input features into dataframe
def user_input_features():
    age = st.sidebar.number_input('Enter your age: ')

    sex  = st.sidebar.selectbox('Sex', ('Male', 'Female'))
    cp = st.sidebar.selectbox('Chest pain type', ('Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'))
    trestbps = st.sidebar.number_input('Resting blood pressure: ')
    chol = st.sidebar.number_input('Serum cholestoral in mg/dl: ')
    fbs = st.sidebar.selectbox('Fasting blood sugar', ('Lower Than 120mg/dl', 'Higher Than 120mg/dl'))
    restecg = st.sidebar.selectbox('Resting electrocardiographic results', ('Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'))
    thalach = st.sidebar.number_input('Maximum heart rate achieved: ')
    exang = st.sidebar.selectbox('Exercise induced angina', ('Yes', 'No'))
    oldpeak = st.sidebar.number_input('ST Depression induced by exercise relative to rest: ')
    slope = st.sidebar.selectbox('The slope of the peak exercise ST segment', ('Upsloping', 'Flat', 'Downsloping'))
    ca = st.sidebar.number_input('Number of major vessels (0-3): ')
    thal = st.sidebar.selectbox('Thalassemia', ('Normal', 'Fixed Defect', 'Reversible Defect'))



    # Map string values to numerical values
    sex_mapping = {'Male': 1, 'Female': 0}
    cp_mapping = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-Anginal Pain': 2, 'Asymptomatic': 3}
    fbs_mapping = {'Lower Than 120mg/dl': 0, 'Higher Than 120mg/dl': 1}
    restecg_mapping = {'Normal': 0, 'ST-T Wave Abnormality': 1, 'Left Ventricular Hypertrophy': 2}
    exang_mapping = {'Yes': 1, 'No': 0}
    slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
    thal_mapping = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2}

    data = {
        'age': age,
        'sex': sex_mapping[sex],
        'cp': cp_mapping[cp],
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs_mapping[fbs],
        'restecg': restecg_mapping[restecg],
        'thalach': thalach,
        'exang': exang_mapping[exang],
        'oldpeak': oldpeak,
        'slope': slope_mapping[slope],
        'ca': ca,
        'thal': thal_mapping[thal]
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Load the trained model
load_clf = pickle.load(open('Random_forest_model.pkl', 'rb'))

# Define a function to predict disease

input_df = user_input_features()

if st.sidebar.button('Predict'):
    prediction = predict_disease(input_df)
    st.sidebar.subheader('Prediction')
    st.sidebar.write(prediction)
    if prediction==0:
        st.balloons()

chart_data=pd.read_csv('heart.csv')

st.bar_chart(chart_data)

#################


# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ',
				('cms', 'meters', 'feet'))

# compare status value
if(status == 'cms'):
	# take height input in centimeters
	height = st.number_input('Centimeters')

	try:
		bmi = weight / ((height/100)**2)
	except:
		st.text("Enter some value of height")

elif(status == 'meters'):
	# take height input in meters
	height = st.number_input('Meters')

	try:
		bmi = weight / (height ** 2)
	except:
		st.text("Enter some value of height")

else:
	# take height input in feet
	height = st.number_input('Feet')

	# 1 meter = 3.28
	try:
		bmi = weight / (((height/3.28))**2)
	except:
		st.text("Enter some value of height")





# check if the button is pressed or not
if(st.button('Calculate BMI')):
	# print the BMI INDEX
	st.text("Your BMI Index is {}.".format(bmi))

	# give the interpretation of BMI index
	if(bmi < 16):
		st.error("You are Extremely Underweight")
	elif(bmi >= 16 and bmi < 18.5):
		st.warning("You are Underweight")
	elif(bmi >= 18.5 and bmi < 25):
		st.success("Healthy")
	elif(bmi >= 25 and bmi < 30):
		st.warning("Overweight")
	elif(bmi >= 30):
		st.error("Extremely Overweight")
