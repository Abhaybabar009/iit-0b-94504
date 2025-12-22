import pandas as pd 
import streamlit as st 

st.title("CSV Explorer")

#upload csv file 
data_file=st.file_uploader("Upload a CSV file" , type=["csv"])
#laod it as dataframe
if data_file:
    df - pd.read_csv(data_file)
    #display the dataframe
    st.dataframe(df)
    