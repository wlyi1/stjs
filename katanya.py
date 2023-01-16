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
from PIL import Image
from PIL import ImageDraw
import matplotlib.pyplot as plt

key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="katanya-85289")


def pasangan():
    hari = dt.now() #.strftime('%Y-%m-%d %H:%M:%S')

    st.header("Apakah pasanganmu adalah yang terbaik? 🥰")
    st.caption("Memiliki pasangan bagi kebanyakan orang membuatnya menjadi lebih bahagia dan hidupnya lebih berwarna. \
    Tapi ada yang bilang setelah punya pasangan malah membuat hidupnya makin merana dan tragis dibandingkan ketika masih single\
        Jadi bagaimana denganmu? Bisakah kau ceritakan apa adanya sehingga orang lain dapat belajar dan memahami dari pengalaman kamu?")

    with st.form(key='form1', clear_on_submit=True):
        
        col1 = db.collection('pasangan')
        name = st.text_input('Nama/akronim/samaran/panggilan : ')
        st.write("Apakah pasanganmu adalah yang terbaik? 🥰")
        option = st.radio(' ', ('Iya', 'Engga'), horizontal=True)
        cerita = st.text_area(label='Ceritanya gimana')
        submit_button = st.form_submit_button(label='Kirim')
        if submit_button:
            col1.add({'nama' : name, "option": option, "tanggal": hari, "cerita": cerita})
            st.write('Terimakasih 👍')

    st.subheader('Cerita Terbaru')

    doc = db.collection('pasangan')
    datas = list(doc.stream())
    list_random = list(map(lambda x: x.to_dict(), datas))
    data = pd.DataFrame(list_random)
    data = data.sort_values(by=['tanggal'], ascending=False)
    df = data['option'].value_counts().rename_axis('option').reset_index(name='counts')
    st.write(df)
    fig1, ax1 = plt.subplots()
    ax1.pie(df.counts, labels=df.option)
    st.pyplot(fig1)

    for i,j,k,l in zip(data['nama'], data['cerita'], data['option'], data['tanggal']):
        cerita_list = list(j.split(" "))
        if k == 'Iya':
            st.info(f'**{i.capitalize()}: {" ".join(cerita_list[:7])}**')
        else:
            st.error(f'**{i.capitalize()} : {" ".join(cerita_list[:7])}**')
        st.write(j)

def nikah():
    hari = dt.now() #.strftime('%Y-%m-%d %H:%M:%S')

    st.header("Apakah pernikahanmu bahagia? 🥰")
    st.caption("Katanya pernikahan membuat hidup kita menjadi lengkap dan indah. Ehm tapi ada yang bilang \
    hidupnya hancur setelah menikah. Oke, jadi bagaimana denganmu apakah setelah menikah bahagia?")

    with st.form(key='form1', clear_on_submit=True):
        
        col1 = db.collection('nikah')
        name = st.text_input('Nama/akronim/samaran/panggilan : ')
        st.write("Apakah pernikahanmu bahagia? 🥰")
        option = st.radio(' ', ('Iya', 'Engga'), horizontal=True)
        cerita = st.text_area(label='Cerita dikit disini')
        submit_button = st.form_submit_button(label='Kirim')
        if submit_button:
            col1.add({'nama' : name, "option": option, "tanggal": hari, "cerita": cerita})
            st.write('Terimakasih 👍')

    st.subheader('Cerita Terbaru')

    doc = db.collection('nikah')
    datas = list(doc.stream())
    list_random = list(map(lambda x: x.to_dict(), datas))
    data = pd.DataFrame(list_random)
    data = data.sort_values(by=['tanggal'], ascending=False)

    for i,j,k,l in zip(data['nama'], data['cerita'], data['option'], data['tanggal']):
        cerita_list = list(j.split(" "))
        if k == 'Iya':
            st.info(f'**{i.capitalize()}: {" ".join(cerita_list[:7])}**')
        else:
            st.error(f'**{i.capitalize()} : {" ".join(cerita_list[:7])}**')
        st.write(j)