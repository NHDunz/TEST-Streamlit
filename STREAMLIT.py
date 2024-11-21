import streamlit as st
import time

st.title("TEST Streamlit")
name = st.text_input("Name: ")
if st.button('Next'):
    bar = st.progress(0)
    for percent in range (100):
        time.sleep(0.005)
        bar.progress(percent + 1)
    st.balloons()
    st.write('\n\nThay ',name,' dep trai tang em chiec SH nhe :3!')