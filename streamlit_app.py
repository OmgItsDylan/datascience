import streamlit as st 
import pandas as pd
import numpy as np
import os
import pickle
import warnings

def main():
	st.title('Crop Prediction')
	n = st.number_input("nitrogen", 1,10000)
	p = st.number_input("phosporus", 1,10000)
	k = st.number_input("potassium", 1,10000)
	temp = st.number_input("temperature",0.0,100000.0)
	humid = st.number_input("humidity in %", 0.0,100000.0)
	ph = st.number_input("ph", 0.0,100000.0)
	rain = st.number_input("rainfall in mm",0.0,100000.0)
	features = [n, p, k, temp, humid, ph, rain]
	input = np.array(features).reshape(1,-1)
	
	if st.button("FOO"):
		model = pickle.load(open("model.pkl", 'rb'))
		prediction = model.predict(input)
		st.write(f"{prediction.item().title()} are recommended by the A.I for your farm.")

if __name__ == '__main__':
	main()
