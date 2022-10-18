import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json
import time

if st.checkbox("Check my location"):
    loc = get_geolocation()
    with st.spinner('waiting'):
        time.sleep(3)
    st.write(f"Your coordinates are {loc}")
    st.write(loc['coords']['latitude'])
    st.write(loc['coords']['longitude'])
