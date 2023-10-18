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


def load(url,title, key) :
    import webbrowser
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title, key):
        webbrowser.open_new_tab(url)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style.css') 

load('https://expat-scr-app-2023.streamlit.app/', 'EXPAT DATA SCRAPER', '1')

load('https://jumia-scra-app-2023.streamlit.app/', 'JUMIA DATA SCRAPER', '2')
load('https://coinafrica-scr-app-2023.streamlit.app/', 'COINAFRICA DATA SCRAPER', '3')
