
import numpy as np
import utils
import json
import pickle
import os
import streamlit as st
import pandas as pd
import utils

with open('CONFIG.json') as config_file:
    CONFIG = json.load(config_file)
path = CONFIG['raw_data_path']
data = pd.read_csv(path)
_models = utils.load_models()
models = _models
#Title

st.sidebar.header('Navigation')

#Navigation Sidebar
nav =st.sidebar.radio("Go to",['Recommend Crops','Analysis'])

#Inputs
if nav=='Recommend Crops':
	st.title('Crop Recommendation')
	st.write('Fill in the fields below to get crop recommendation best suited to grow in your soil')

	#Inputs
	n = st.slider('Select N (Ratio of Nitrogen content in your soil)', max_value=140)
	st.write(n)
	st.write(" ")

	p = st.slider('Select P (Ratio of Phosphorus content in your soil)', max_value=145)
	st.write(p)
	st.write(" ")

	k = st.slider('Select K (Ratio of Potassium content in your soil)' , max_value=205)
	st.write(k)
	st.write(" ")

	temp = st.number_input('Select Temperature of your area (in °C)' , step=0.01)
	st.write(round(temp,2),"°C")


	hum = st.number_input('Select Relative Humidity of your area (in %)' , step=0.01)
	st.write(round(hum,2))
	if hum > 100:
		st.error('Humidity cannot exceed 100%')
	if hum < 0:
		st.error('Humidity cannot be lower than 0%')
	st.write(" ")

	ph = st.slider('Select pH level', min_value=0.0, max_value=14.0, step=0.1)
	st.write(ph)
	st.write(" ")

	rain = st.number_input('Select Rainfall (in mm) ' , step=0.01)
	st.write(round(rain,2), "mm")

	if rain < 0:
		st.error('Rainfall cannot be lower than 0')
	st.write(" ")

	models_list = [models.keys()]
	st.markdown('## Select to model to use for prediction')
	model_input = st.radio("",
		['LogisticRegression (Accuracy:- 95.70%)',
		'DecisionTreeClassifier (Accuracy:- 98.98%)',
		'AdaBoostClassifier (Accuracy:- 18.48%)',
		'GradientBoostingClassifier (Accuracy:- 98.89%)',
		'RandomForestClassifier (Accuracy:- 99.49%)',
		'ExtraTreesClassifier (Accuracy:- 98.98%)',
		'SupportVectorClassifier (Accuracy:- 97.42%)',
		'KNeighborsClassifier (Accuracy:- 97.52%)',
		'GaussianNB (Accuracy:- 99.34%)'])

	if st.button("Predict"):
            inputs=np.array([n,p,k,temp,hum,ph,rain])
            print(inputs)
            print(inputs[4])
            key = model_input.split('(')[0].strip()+'.pkl'

            prediction = models[key].predict(inputs.reshape(1, -1))
            st.markdown('# Best suited crop for your soil : {0}.'.format(prediction[0]))
            print(prediction)

@st.cache_data
def generate_plots(dframe, _type = 'streamlit'):
    if _type == 'streamlit':
        for i in data.columns[:-1]:
            st.write('mean {0} v/s crop plot'.format(i))
            st.bar_chart(data.groupby('label')[i].mean())
    elif _type == 'seaborn':
        for i in data.columns[:-1]:
            st.pyplot(utils.generate_seaborn_plots(dframe, i))





if nav=='Analysis':
	st.title('Crop wise parameter analysis')

	st.markdown('### Following graphs display average value of respective parameter required to grow that specific crop')
	st.write(" ")
	generate_plots(data, 'streamlit')
