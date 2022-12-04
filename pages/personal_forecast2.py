
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import numpy as np


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)







lr = joblib.load('lr.pkl')
#
def get_target_type(clf_predict):
    if clf_predict == 1:
        type = 'AD Dementia'
    if clf_predict == 0:
        type = 'uncertain dementia'
    if clf_predict == -1:
        type = 'No dementia'
    return type

#

def app():

    with st.container():
        Gender = st.radio('您的性别',('男','女'))
        mmse = st.number_input('MMSE：简易智力状态检查量表评分', value=16)
        ageAtEntry = st.number_input('您的年龄', value=68.00)
        cdr = st.number_input('CDR:临床医学痴呆症量表评分', value=1)
        memory = st.number_input('MEMORY:韦氏记忆量表评分', value=1)
        if Gender=='男':
            Gender=1
        if Gender=='女':
            Gender=0
        data = pd.DataFrame(
            {'Gender': [Gender], 'mmse': [mmse], 'ageAtEntry': [ageAtEntry], 'cdr': [cdr], 'memory': [memory]})
        data_re = pd.read_csv('大创阿兹海默数据_处理后.csv')
        data_re = data_re.drop('Unnamed: 0', axis=1)
        y = data_re["dx1"]
        x = data_re.drop('dx1', axis=1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)
        transfer = StandardScaler()
        x_train = transfer.fit_transform(x_train)
        x_test = transfer.transform(data)
        st.write("---")
        st.header('健康情况预测')
        lr_predict = lr.predict(x_test)
        lr_predict_proba = lr.predict_proba(x_test)
        if get_target_type(lr_predict) == 'AD Dementia':
            st.subheader('阿尔兹海默症型痴呆')
            st.subheader('患病几率为：')
            st.subheader(max("{:.4f}".format(float(lr_predict_proba.tolist()[0][0])),
                             "{:.4f}".format(float(lr_predict_proba.tolist()[0][1])),
                             "{:.4f}".format(float(lr_predict_proba.tolist()[0][2]))))
        if get_target_type(lr_predict) == 'uncertain dementia':
            st.subheader('其他痴呆类型')
            st.subheader('患病几率为：')
            st.subheader(max("{:.4f}".format(float(lr_predict_proba.tolist()[0][0])),
                             "{:.4f}".format(float(lr_predict_proba.tolist()[0][1])),
                             "{:.4f}".format(float(lr_predict_proba.tolist()[0][2]))))
            if get_target_type(lr_predict) == 'No dementia':
                st.subheader('没有罹患痴呆')
                st.subheader('几率为：')
                st.subheader(max("{:.4f}".format(float(lr_predict_proba.tolist()[0][0])),
                                 "{:.4f}".format(float(lr_predict_proba.tolist()[0][1])),
                                 "{:.4f}".format(float(lr_predict_proba.tolist()[0][2]))))
        st.write("数据来自 ADNI阿尔茨海默症权威数据中心的临床数据集")


#
# def app():
#     with st.container():
#         lr_predict = lr.predict(x_test)
#         lr_predict_proba = lr.predict_proba(x_test)
#         data = pd.DataFrame(
#             {'Gender': [Gender], 'mmse': [mmse], 'ageAtEntry': [ageAtEntry], 'cdr': [cdr], 'memory': [memory]})
#         st.subheader('预测为')
#         st.subheader(lr_predict)




