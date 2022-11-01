import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json
import time

st.title('Polling Kehidupan')
st.caption("polling kehidupan merupakan platform untuk ngasih tau ke masyarakat tentang fenomena kehidupan apa adanya")
st.subheader("Apakah pasanganmu saat ini adalah yang terbaik?")
col1, col2 = st.columns(2)
ya = 0
tidak = 0
with col1:
    ya_but = st.button('Ya')
    st.text_area('Kenapa bisa iya')
    if ya_but:
        ya +=1
with col2:
    tidak_but = st.button('Tidak')
    st.text_area('Kenapa bisa tidak')
    if tidak_but:
        tidak += 1
       
    
st.write(ya)
st.write(tidak)
