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
st.write("Ehh tau ga sih katanya bla bla bla ahh coba lo buktiin di mari dah! 😮‍💨 ")

with st.form(key='form1'):
    #database references
    db1 = firestore.Client(credentials=creds, project="testrandom1-6cf06")
    col1 = db.collection('story')

    st.subheader("Apakah pasanganmu adalah yang terbaik? 🫢")
    cols1, cols2 = st.columns(2)
    st.radio(' ', ('Iya', 'Engga'))
    agree = cols1.checkbox('Iya')
    disagree = cols2.checkbox('Engga')
    text_input = st.text_area(label='Ceritanya gimana')
    submit_button = st.form_submit_button(label='Kirim')
    if submit_button:
        col1.add({"Option": nama, "tanggal": tgl_random, "cerita": cerita})
        st.write('Terimakasih 👍')
