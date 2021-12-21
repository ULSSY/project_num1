import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from mysql_connection import get_connection
from mysql.connector.errors import Error
 
def run_list_pro():

    bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

    fig1=plt.figure()
    df[selected_column].hist(bins=bins)
    st.pyplot(fig1)

   