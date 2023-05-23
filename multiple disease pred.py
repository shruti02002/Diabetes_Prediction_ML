# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 21:39:07 2023

@author: KIIT
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open("C:/Users/KIIT/Documents/Multiple Disease Prediction System/MINOR PROJECT/diabetes_model.sav", 'rb'))

#sidebar for navigate
with st.sidebar:
    selected = option_menu('Disease Prediction System',
                           ['Diabetes Prediction'],
                           icons=['activity'],
                           default_index = 0)
    


#Diabetes prediction Page
if(selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    

    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
   
    if st.button('Diabetes Test Result'):
       diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
       
       if (diab_prediction[0] == 1):
         diab_diagnosis = 'The person is diabetic'
       else:
         diab_diagnosis = 'The person is not diabetic'
       
    st.success(diab_diagnosis)