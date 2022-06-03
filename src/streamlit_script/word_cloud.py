import streamlit as st
import pandas as pd
import numpy as np
import math
import os
import sys
import time
import re
import json
path = os.getcwd()
sys.path.append(path)
from src.utils.helper_function import *
# Libraries for worcloud
import nltk
from wordcloud import WordCloud, STOPWORDS
from PyDictionary import PyDictionary
import matplotlib.pyplot as plt

def convert_df(df):
    # return df.to_csv().encode('utf-8')
    return df.to_csv()



html_temp = """
<div style ="background-color:lightblue;padding:13px">
<h1 style ="color:black;text-align:center;">Streamlit-example</h1>
</div>
"""
st.write(html_temp, unsafe_allow_html=True)
st.write("#")

if uploaded_file is not None:
    try:
        df1 = pd.read_csv(uploaded_file)
    except Exception:
        df1 = pd.read_excel(uploaded_file)
    st.components.v1.html("""
<h1 style ="color:black;text-align:center">Preview of Data from Input File</h1>
""", height=60)
    st.dataframe(df1)
    my_data = convert_df(df1)
    col = df1.select_dtypes(['object']).columns
    st.write("----")
