import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# st.title('BEST DATA SCRAPER APP')
st.markdown("<h1 style='text-align: center; color: black;'>BEST DATA SCRAPER APP</h1>", unsafe_allow_html=True)

st.markdown("""
This app is built to help you scrape and download data from any senegalese online sale 
web site. For a simple click, you have the data you want in a minute!

""")


# Background function
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('img_file.jpg') 

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.markdown(f'''
            <a href={'https://expat-scr-app-2023.streamlit.app/'}><button style="background-color:#facfd2;">  EXPAT DATA SCRAPER  </button></a>
            ''', unsafe_allow_html=True)
with col3:
        st.write(' ')


col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.markdown(f'''
            <a href={'https://jumia-scra-app-2023.streamlit.app/'}><button style="background-color:#facfd2;">  JUMIA DATA SCRAPER  </button></a>
            ''', unsafe_allow_html=True)
with col3:
        st.write(' ')

col1, col2, col3 = st.columns([3,3,3.8])
with col1:
    st.write(' ')
with col2:
    st.markdown(f'''
            <a href={'https://coinafrica-scr-app-2023.streamlit.app/'}><button style="background-color:#facfd2;">COINAFRICA DATA SCRAPER</button></a>
            ''', unsafe_allow_html=True)
with col3:
        st.write(' ')
