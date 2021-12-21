import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mysql_connection import get_connection
 

def run_fir_pro():
    df = pd.read_csv('data/OBS_계절관측.csv')
    df.set_index('지점',inplace=True)
    radio_menu=['동물','식물','기상']
    selected_radio=st.radio('선택하세요',radio_menu)
    
    
    if selected_radio=='동물':
       
        radio_menu=['제비','나비','잠자리','뻐꾸기','매미']
        selected_radio=st.radio('선택하세요',radio_menu)

        if selected_radio=='제비':
          
            df=(df['계절관측']=='제비')!='false'
            st.dataframe(df)
        
        elif selected_radio=='나비':
            df=(df['계절관측']=='나비')!='false'
            st.dataframe(df)
        
        elif selected_radio=='잠자리':
            df=(df['계절관측']=='잠자리')!='false'
            st.dataframe(df)
        
        elif selected_radio=='뻐꾸기':
            df=(df['계절관측']=='뻐꾸기')!='false'
            st.dataframe(df)
        
        elif selected_radio=='매미':
            df=(df['계절관측']=='매미')!='false'
            st.dataframe(df)
    
    
        df = pd.read_csv('data/OBS_계절관측.csv')
        df.set_index('지점',inplace=True)
       

    elif selected_radio=='식물':
       
        
        radio_menu=['개나리','매화','코스모스','진달래','벚나무']
        selected_radio=st.radio('선택하세요',radio_menu)

        if selected_radio=='개나리':
            df1=(df['계절관측']=='개나리')!='false'
           
            df['년도':'계절현상']
            pd.concat(df,df1)
         
            # st.dataframe(df1)

    #     elif selected_radio=='매화':
    #         df1=(df['계절관측']=='매화')!='false'
    #         st.dataframe(df1)
    #     elif selected_radio=='코스모스':
    #         df1=(df['계절관측']=='코스모스')!='false'
    #         st.dataframe(df1)
    #     elif selected_radio=='진달래':
    #         df1=(df['계절관측']=='진달래')!='false'
    #         st.dataframe(df1)
    #     elif selected_radio=='벚나무':
    #         df1=(df['계절관측']=='벚나무')!='false'
    #         st.dataframe(df1)

    #     df = pd.read_csv('data/OBS_계절관측.csv')
    #     df.set_index('지점',inplace=True)
   
    # elif selected_radio=='기상':
       
    #     radio_menu=['서리','얼음','눈']
    #     selected_radio=st.radio('선택하세요',radio_menu)

    #     if selected_radio=='서리':
    #         df2=(df['계절관측']=='서리')!='false'
    #         st.dataframe(df2)
    #     elif selected_radio=='얼음':
    #         df2=(df['계절관측']=='얼음')!='false'
    #         st.dataframe(df2)
    #     elif selected_radio=='눈':
    #         df2=(df['계절관측']=='눈')!='false'
    #         st.dataframe(df2)