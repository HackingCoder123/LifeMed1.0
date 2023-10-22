import streamlit as st
import time  # to simulate a real time data, time loop
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


def main():
    st.set_page_config(
        page_title='LifeMed',
        page_icon='⛑️',
        layout='wide',
    )
    col1, col2, col3= st.columns(3)
    
    

    col2.markdown("""
                <style>
                .big-font {
                font-size:90px !important;
                }
                </style>
                """, unsafe_allow_html=True)
    col2.markdown('<p class="big-font">LifeMed</p>', unsafe_allow_html=True)
    col3.image('logo.png',width=130)
    
    col2.info('Your Health, Our Priority: LifeMed in Motion')

    
    st.image('deathscaused.svg',width=500)

    st.image('wwm.svg')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')
    col1.write('                ')

    col1.write('Embark on a journey to optimal well-being with LifeMed, the all-in-one health app that empowers you to take charge of your health. Our cutting-edge technology seamlessly combines symptom analysis, disease prediction, and easy access to vital medical resources.Experience the future of healthcare in your hands')
    col1.button('💵1 dollar💵')
    col1.success('Help those in need')
    col2.image('32.png')

    st.info('This app allows users to build a connection towards a brighter , healthier future')









if __name__ == '__main__':
    main()