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

hari = dt.today().strftime('%Y-%m-%d')

st.title('Katanya?!')
st.write("Ehh tau ga sih katanya bla bla bla ahh coba lo buktiin di mari dah! 😮‍💨 ")

with st.form(key='form1'):
    #database references
    #db1 = firestore.Client(credentials=creds, project="katanya-85289")
    col1 = db.collection('pasangan')

    st.subheader("Apakah pasanganmu adalah yang terbaik? 🫢")
    option = st.radio(' ', ('Iya', 'Engga'), horizontal=True)
    cerita = st.text_area(label='Ceritanya gimana')
    submit_button = st.form_submit_button(label='Kirim')
    if submit_button:
        col1.add({"option": option, "tanggal": hari, "cerita": cerita})
        st.write('Terimakasih 👍')

st.subheader('Cerita Terbaru')

doc = db.collection('pasangan')
datas = list(doc.stream())
list_random = list(map(lambda x: x.to_dict(), datas))
data = pd.DataFrame(list_random)
st.write(data)
for i in data['cerita'].values():
    st.write(i)