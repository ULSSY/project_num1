import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from mysql_connection import get_connection
from mysql.connector.errors import Error
from new4 import run_list_pro

def run_fir_pro():
    df = pd.read_csv('data/OBS_계절관측.csv')
    df.set_index('지점',inplace=True)
    radio_menu=['동물','식물','기상']
    selected_radio=st.radio('선택하세요',radio_menu)
    
    
    if selected_radio=='동물':
       
        radio_menu=['제비','나비','잠자리','뻐꾸기','매미']
        selected_radio=st.radio('컬럼을 선택하세요',radio_menu)
        if selected_radio=='제비':
            
            radio_menu_1=['년도','날짜','계철관측','계절현상']
            df1=selected_column=st.selectbox('컬럼을 선택하세요',radio_menu_1)
            if radio_menu_1=='년도':
                year=st.number_input('연도입력하기')

                if st.button('저장하기'):
                        try : 
                               
                            connection=get_connection()

                            #2.쿼리문 만들고
                            query='''insert into test_user
                                    (email,password,age)
                                    values
                                    (%s,%s,%s);'''
                            #튜플 데이터 한개 있을때 콤마를 꼭 
                            #써주자
                            record=(email,password,age)
                            #3.커넥션으로부터 커서를 가져온다
                            cursor=connection.cursor()
                            #4쿼리문을 커서에 넣어서 실행한다
                            cursor.execute(query,record)
                            #5커넥션을 커밋한다->디비에 영구적으로 반영하라는 뜻
                            connection.commit()
                        except mysql.connector.Error as e:
                            print('Error',e)
                        finally:
                            if connection.is_connected():
                                cursor.close()
                                connection.close()
                                print('MySQL connection is closed')
                                st.write('회원정보가 잘 저장됐습니다.')

                             
        
       



    
    #     df = pd.read_csv('data/OBS_계절관측.csv')
    #     df.set_index('지점',inplace=True)
       

    # elif selected_radio=='식물':
       
        
    #     radio_menu=['개나리','매화','코스모스','진달래','벚나무']
    #     selected_radio=st.radio('선택하세요',radio_menu)

    #     if selected_radio=='개나리':
    #         run_list_pro()
           
           
          
         
            

    #     elif selected_radio=='매화':
    #         run_list_pro()
            
    #     elif selected_radio=='코스모스':
    #         run_list_pro()
          
    #     elif selected_radio=='진달래':
    #         run_list_pro()
            
    #     elif selected_radio=='벚나무':
    #         run_list_pro()
            

    #     df = pd.read_csv('data/OBS_계절관측.csv')
    #     df.set_index('지점',inplace=True)
   
    # elif selected_radio=='기상':
       
    #     radio_menu=['서리','얼음','눈']
    #     selected_radio=st.radio('선택하세요',radio_menu)

    #     if selected_radio=='서리':
    #         run_list_pro()
          
    #     elif selected_radio=='얼음':
    #         run_list_pro()
            
    #     elif selected_radio=='눈':
           
    #         run_list_pro()