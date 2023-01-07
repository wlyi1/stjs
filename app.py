import streamlit as st
#from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json
import time


st.title('Katanya?!')
st.write("ehh tau ga sih katanya ini? katanya itu? ahh coba lo buktikan dah di sini")
st.subheader("Apakah pasanganmu saat ini adalah yang terbaik?")
col1, col2 = st.columns(2)

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
