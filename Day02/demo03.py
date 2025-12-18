#you are building a small website usingh python, without html,css or javascripts

import streamlit as st

st.title("Hello, Abhay!")           #biggest text
st.header("Welcome to GenAI Training Program!")     # little small test than st.title

st.write("Hello student, I hope you are enjoying tech stuff here....")      #st.write can print text, numbers,lists,dataframes,varibales


if st.button("click me!", type="primary"):      #type="primary" makes the button blue (highlighted)
    st.toast("you clicked me ...")