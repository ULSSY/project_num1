import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mysql_connection import get_connection
from new1 import run_fir_pro
from mysql.connector.errors import Error

def run_data_pro() :
    st.subheader('데이터분석')

    df = pd.read_csv('data/OBS_계절관측.csv')
    df.set_index('지점',inplace=True)
    radio_menu=['데이터프레임','관측자료']
    selected_radio=st.radio('선택하세요',radio_menu)

    if selected_radio=='데이터프레임':
        
      sns.countplot(data=df)
       
       
        
    elif selected_radio=='관측자료':
        st.write('지점은 인천입니다.')
    
        year=st.number_input('년도',min_value=df['년도'].min(), max_value=df['년도'].max())
    
        date=st.text_input('날짜')
        season=st.text_input('계절관측')
    
    if st.button('저장하기'):
      
        try : 
            #DB에 연결
            connection=get_connection()

            #2.쿼리문 만들고
            query='''insert into new_table
                    (spot,year,date,season)
                    values
                    (%s,%s,%s,%s);'''
            #튜플 데이터 한개 있을때 콤마를 꼭 
            #써주자
            record=(spot,year,date,season)
            #3.커넥션으로부터 커서를 가져온다
            cursor=connection.cursor()
            #4쿼리문을 커서에 넣어서 실행한다
            cursor.execute(query,record)
            #5커넥션을 커밋한다->디비에 영구적으로 반영하라는 뜻
            connection.commit()
        except Error as e:
            print('Error',e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print('MySQL connection is closed')
                st.write('회원정보가 잘 저장됐습니다.')
        
    # radio_menu=['동물','식물','기상']

    # selected_radio=st.radio('선택하세요',radio_menu)

     
 
  

        # phenon=st.text_input('계절현상')
    
        # print(spot,year,date,season,phenon)

    # if st.button('저장'):
    #     try : 
    #         #DB에 연결
    #         connection=get_connection()
            
        
    #         #2.쿼리문 만들고
            
    #         query='''update test_user
    #                 set name=%s
    #                 where id=%s'''
    #         #튜플 데이터 한개 있을때 콤마를 꼭 
    #         #써주자
    #         record=(age,id)
    #         #3.커넥션으로부터 커서를 가져온다
    #         cursor=connection.cursor()
    #         #4쿼리문을 커서에 넣어서 실행한다
    #         cursor.executemany(query,record)
    #         #5커넥션을 커밋한다->디비에 영구적으로 반영하라는 뜻
    #         connection.commit()
    #     except Error as e:
    #         print('Error',e)
    #     finally:
    #         if connection.is_connected():
    #             cursor.close()
    #             connection.close()
    #             print('MySQL connection is closed')
    #             st.write('변경이 완료 되었습니다.')