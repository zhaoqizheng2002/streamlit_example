'''
Description: 
Author: zhaoqizheng
'''
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def app():

    '''
    年龄[2, 3, 4]、性别[2, 3]、体重（BMI）[1, 2, 5, 6]、
    教育程度[1, 2, 3, 6]、社会关系[1, 2, 7, 8, 9, 10, 11, 12]、社会地位、饮酒[14, 15, 16]、饮食习惯[13, 14]、
    高血压[1, 2, 6, 25, 26, 27, 28, 29]、中年高血脂[2]、2型糖尿病[1, 2, 6, 22, 23, 24]、体育锻炼[1, 2, 14]、
    抑郁[1, 2, 6, 17]、创伤性脑（头部）损伤[1, 2]、吸烟[1, 2, 14]、中风[2, 36, 37]、慢性肠炎[2, 18, 19, 20, 21]、
    高血压以外的心血管疾病[1, 25, 30, 31, 32]（血压异常、心脏代谢疾病、心力衰竭等）、癌症幸存[33]、偏头痛[34]、
    药物使用[35, 36]（包括镇静安眠药、抗抑郁药、化疗药物和心血管药物[6]）
    '''

    st.write('一、基本健康情况')
    age = st.text_input('1.您的年龄是？')
    Gender = genre = st.radio("2.您的性别是？",('男', '女'))
    heigh = st.text_input('3.您的身高是？')
    weigh = st.text_input('4.您的体重是？')
    have_been_diagnosed_options = st.multiselect(
        '5.您是否曾被诊断或目前被诊断为以下疾病？',
        ['高血压', '高血脂', '高血压、高血脂以外的心血管疾病（血压异常、心脏代谢疾病、心力衰竭等）',
         '2型糖尿病', '中风', '慢性肠炎','偏头痛','抑郁','创伤性脑（头部）损伤','癌症幸存'])
    drugs = st.radio("6.您是否有长期（3个月或以上）使用镇静安眠药、抗抑郁药、化疗药物和心血管药物等药物？", ('有', '无'))


    st.write('二、生活习惯状况')
    smoke = st.radio('7.您是否有吸烟习惯？(指吸烟≥1支/天，且持续≥6个月，包括过去吸烟，但现已戒烟）',('有','无'))
    drink_wine = st.radio('8.您是否有饮酒习惯？(指饮酒≥1次/周，且持续≥6个月)',('有','无'))
    fruit_or_vegetable = st.radio('9.您进食蔬菜/水果的频率是？',('小于每周一次','每周1-6次','每天一次或以上'))

    sports = st.radio('10.您参加体育锻炼（每周中高强度运动，持续大于等于1小时）的频率是？',
                                  ('少于每周2次', '每周3-4次', '每周5次及以上'),
                                  help='注：中高强度运动包括快走、慢泡、游泳、太极拳、骑车、爬楼梯等；快跑、篮球、足球、羽毛球等；家务活动如扫地、买菜、陪孩子玩耍等。')

    st.write('三、社会关系状况')
    Highest_education = st.radio('11.您目前的最高学历是？',('初中及以下', '高中/中专', '大学/大专及以上'))
    marriage = st.radio('12.您目前的婚姻状况是？',('未婚','已婚','离异','丧偶'))
    income = st.radio('13.您的家庭月人均收入为？',('小于3000','大于或等于3000'))
    living = st.radio('14.您最近5年的主要居住情况是？',('与他人居住','独居'))
    kids = st.radio('15.您是否有子女?',('有','无'))
    family_members = st.radio('16.您在同市（县、自治县、直辖市）内是否有经常联系的家属、亲戚或朋友？',('有','无'))