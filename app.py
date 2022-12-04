'''
Description: 
Author: zhaoqizheng
'''
import streamlit as st
from multipage import MultiPage
from pages import META_update, personal_forecast2, home_page

st.set_page_config(page_title="阿尔兹海默症及相关认知障碍疾病风险预测系统", page_icon=":tiger:", layout="wide")
st.title('阿尔兹海默症及相关认知障碍疾病风险预测系统')

# 实例化multipage对象：
app = MultiPage()

# add applications
app.add_page('-', home_page.app)
app.add_page('人工智能预测', personal_forecast2.app)
app.add_page('数据反馈', META_update.app)

# Run application
if __name__ == '__main__':
    app.run()