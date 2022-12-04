'''
Description:
Author: zhaoqizheng
'''
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

def app():
    st.subheader('亲爱的用户:')
    st.subheader(
        '本系统是由中山大学公共卫生学院（深圳）的本科生研究团队开发的、一个可预测您或家人患阿尔兹海默症及相关认知障碍疾病风险的系统，可以方便您或家人了解自身健康情况，并收集数据为系统改进和相关疾病研究提供参考。请您协助回答以下问题，需要耽误您约10-15分钟的时间，感谢您的配合与支持。')
    st.subheader('本系统不用填写姓名，也不会涉及您的具体隐私。各种答案没有正确与错误之分，请您根据自己的实际情况填写。')
    st.subheader('本系统所预测的结果和患病概率仅供参考，并不代表您的真实健康情况，也不能作为疾病诊断结果，如有不适请及时就医。')
    st.subheader('我们保证，系统所采集的数据仅用于研究分析，绝不会泄露您的隐私。再次感谢您的配合，祝您生活顺利！')
    st.write('如同意以上协议，请点击下方按钮以进入系统：')
    st.button('我已知晓以上内容并同意使用此系统')
