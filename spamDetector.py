import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from win32com.client import Dispatch
import pandas as pd




model = pickle.load(open('spam.pkl','rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))

def main():
	st.title(":green[SMS Spam Classification]")
	st.subheader(":violet[Team:]")
	st.subheader(":violet[Kevin Shajy 21BAI1497]")
	st.subheader(":violet[Aditya Sai Veligatla 21BAI1552]")

	
	st.header(":violet[Classification]")
	msg=st.text_input("Enter a text")
	print(msg)
	print(type(msg))
	data=[msg]
	print(data)
	vec=cv.transform(data).toarray()
	result=model.predict(vec)
	if result[0]==0:
			st.success("This is Not A Spam Email/SMS")
				
			st.metric(label="HAM", value="SAFE")
				
	else:
			st.error("This is A Spam Email/SMS",icon="🚨")
				
			st.metric(label="SPAM", value="NOT SAFE")	
		

main()



