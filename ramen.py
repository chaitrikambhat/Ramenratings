import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Ramen Ratings", page_icon=":ramen:",layout="wide")
def load_lottieurl(url):
	r=requests.get(url)
	if r.status_code !=200:
		return None
	return r.json()

lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_dzfeml7x.json")
with st.container():
	st.title("This page is used to predict Ramen ratings")
	st.write("It also tells whether the ramen is delicious or not based on the reviews received")
	st_lottie(lottie_coding,height=400,key="ramen")
