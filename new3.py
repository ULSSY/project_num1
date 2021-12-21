import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from mysql_connection import get_connection
from mysql.connector.errors import Error
 
def button():
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
        #     #4쿼리문을 커서에 넣어서 실행한다
            cursor.execute(query,record)
        #     #5커넥션을 커밋한다->디비에 영구적으로 반영하라는 뜻
            connection.commit()
        except Error as e:
            print('Error',e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print('MySQL connection is closed')
                st.write('회원정보가 잘 저장됐습니다.')