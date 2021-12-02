import pandas 
import streamlit as st
import streamlit.components.v1 as components

import glob


path1 = glob.glob("LSTM/*.html")
dict_lstm_files = {var[6:-5]:var for var in path1}

path2 = glob.glob("LSTM_AE/*.html")
dict_lstm_ae_files = {var[9:-5]:var for var in path2}

# Main Window
st.header("Inspect Predictions")

# Side-bar
#model_options = st.sidebar.selectbox('Select Model:',options=['LSTM','LSTM_AE'],help='List of Models for evaluation')
options = st.sidebar.selectbox('Select Sensor/Pollutant:',options=[var[6:-5] for var in path1])

with st.container():
    st.header("Baseline: LSTM")
    # Display on main window
    HtmlFile = open(dict_lstm_files[options], 'r', encoding='utf-8') 
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, height = 1000,width=1500,scrolling=True)

with st.container():
    st.header("Alternative: LSTM Heterogenous")
    # Display on main window
    HtmlFile = open(dict_lstm_ae_files[options], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, height = 1000,width=1500,scrolling=True)


