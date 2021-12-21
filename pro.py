import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import new3 as button
from data_pro import run_data_pro
from new1 import run_fir_pro

def main():
    menu = ['홈','데이터분석','데이터검색','인공지능']

    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == '홈' :
        st.subheader('계절별 동식물백과')
          
    elif choice == '데이터분석' :
        
        run_data_pro()
        
    elif choice == '데이터검색' :
        run_fir_pro()
    
    elif choice == '인공지능' :
        pass

if __name__ == '__main__' :
    main()