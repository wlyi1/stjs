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
from katanya import pasangan, nikah

image1 = 'https://raw.githubusercontent.com/wlyi1/stjs/main/tema.png'
st.image(image1)

opt = st.selectbox('Pilih katanya: ', ['pasangan', 'nikah'])
match opt:
    case 'pasangan' : pasangan()
    case "nikah" : nikah()

"""if opt == 'pasangan':
    pasangan()
elif opt == 'nikah':
    nikah()"""

