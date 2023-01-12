import streamlit as st
import json
import time
import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account
from google.cloud.firestore import Client
import random
import datetime
from datetime import datetime as dt
import pandas as pd
import streamlit.components.v1 as components
from streamlit.components.v1 import html

key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="katanya-85289")


st.title('Katanya?!')
st.write("Ehh tau ga sih katanya ini? katanya itu? ahh coba lo buktiin di mari dah! 😮‍💨 ")

with st.form(key='form1'):
    st.subheader("Apakah pasanganmu saat ini adalah yang terbaik? 🫢")
    cols1, cols2 = st.columns(2)
    agree = cols1.checkbox('Iya')
    disagree = cols2.checkbox('Engga')
    text_input = st.text_area(label='Ceritanya gimana')
    submit_button = st.form_submit_button(label='Kirim')

    


'''col1, col2 = st.columns(2)

if 'ya' not in st.session_state:
    st.session_state.ya = 0
    
if 'tidak' not in st.session_state:
    st.session_state.tidak = 0

with col1:
    ya_but = st.button('Ya')
    st.text_area('Kenapa bisa iya')
    if ya_but:
        st.session_state.ya +=1
with col2:
    tidak_but = st.button('Tidak')
    st.text_area('Kenapa bisa tidak')
    if tidak_but:
        st.session_state.tidak += 1
       
    
st.write(st.session_state.ya)
st.write(st.session_state.tidak)
'''