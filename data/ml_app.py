import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

def run_ml_app() :
    st.subheader('Machine Learning 예측')

    df = pd.read_csv('data/도로교통.csv', encoding='CP949')
    df = df.loc[:,'발생건수':'부상신고']
    # 1. 유저한테, 데이터를 입력받습니다.
    gender = st.radio('시도를 입력하세요.', ['인천', '경기','강원','서울','세종','충북','충남','광주','대전','전북','전남','대구','부산','울산','경북','경남'])
    if gender == '인천' :
        st.selectbox('시군구를 입력하세요.', ['중구', '동구','남구','부평구','남동구','서구','연수구','계양구'])
        
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())

    elif gender == '경기' :
        st.selectbox('시군구를 입력하세요.', ['수원시', '성남시','의정부시','안양시','부천시','안산시','평택시','광명시','구리시','양주시','여주시','화성시','시흥시','고양시','광주시','포천시','가평군','양평군','이천시','용인시','안성시','김포시','군포시','남양주시','오산시','의왕시','하남시'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '강원' :
        st.selectbox('시군구를 입력하세요.', ['춘천시', '원주시','동해시','강릉시','속초시','홍천군','횡성군','평창군','인제군','양양군'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '서울' :
        st.selectbox('시군구를 입력하세요.', ['성북구', '강서구','강남구','강동구','송파구','서초구','양천구','중랑구','노원구','금천구'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '세종' :
        st.selectbox('시군구를 입력하세요.', ['세종'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '충북' :
        st.selectbox('시군구를 입력하세요.', ['청주시', '충주시','제천시','보은군','옥천군','영동군','진천군','괴산군','음성군','단양군','증평군'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '충남' :
        st.selectbox('시군구를 입력하세요.', ['천안시', '보령시','공주시','서산시','금산군','논산시','부여군','서천군','청양군','홍성군','예산군','당진시','계룡시'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '광주' :
        st.selectbox('시군구를 입력하세요.', ['북구', '광산구'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '대전' :
        st.selectbox('시군구를 입력하세요.', ['동구', '중구','서구'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '충북' :
        st.selectbox('시군구를 입력하세요.', ['수원시', '성남시'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())
    elif gender == '충북' :
        st.selectbox('시군구를 입력하세요.', ['수원시', '성남시'])
        st.subheader('각 컬럼별 히스토그램 확인')

        selected_column=st.selectbox('컬럼을 선택하세요',df.columns)

        bins=st.slider('bin의 갯수 조절',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('각 컬럼별 통계치')
        st.dataframe(df.describe())

    # # 2. 모델에 예측한다.

    # # 2-1. 신규데이터를 넘파이로 만든다.
    # new_data = np.array([gender_number, age, salary, debt, worth])
    # new_data = new_data.reshape(1, 5)

    # # 2-2. 스케일러와 인공지능을 변수로 불러온다.
    # scaler_X = joblib.load('data/scaler_X.pkl')
    # scaler_y = joblib.load('data/scaler_y.pkl')
    # regressor = joblib.load('data/regressor.pkl')

    # # 2-3. 신규데이터를 피쳐스케일링 한다.
    # new_data = scaler_X.transform(new_data)

    # # 2-4. 인공지능에게 예측을 하게 한다.
    # y_pred = regressor.predict(new_data)
    
    # # 2-5. 예측한 결과는, 다시 원래대로 복구해 줘야 한다. 
    # print(y_pred)

    # y_pred = scaler_y.inverse_transform(y_pred.reshape(1,1))
    # print(y_pred)

    # # 3. 예측 결과를 웹 대시보드에 표시한다.

    # btn = st.button('예측 결과 보기')
    # # 결과가 소수점으로 나오는데, 소수점 뒤 한자리까지만 나오도록
    # # 코드 수정하세요.
    # if btn :
    #     st.write('예측 결과! {:.1f} 달러의 차를 살 수 있습니다.'.format(y_pred[0,0]))
    #     st.write('예측 결과! {} 달러의 차를 살 수 있습니다.'.format( round(y_pred[0,0], 1) ))