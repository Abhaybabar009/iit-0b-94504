import streamlit as st 

#Create memory for chat (session state)
if 'messages' not in st.session_state:
    st.session_state.messages = []
#Why this is needed ❓
#Streamlit refreshes the app on every action
#Without session state, chat history will be lost
#What it does:
#Checks if messages list exists
#If not, creates an empty list to store chat messages
#sidebar section 
with st.sidebar:

#sidebar header
    st.header("Settings")
# displays the settings title in sidebar 

#mode selection 
Choices = ["Uppercase", "Lowercase", "Toggle"]
mode = st.selectibox("Select Mode", Choices)
#Shows a dropdown
#User selects how the chatbot should reply:
#Upper → HELLO
#Lower → hello
#Toggle → hELLO

count = st.slider("Message Count", min_value=2, max_value=10, value=6, step=2)
#shows a slider
#lets  user choose number between 2 and 10 
#in this code it is only for display/demo purpose


#show config as json
st.subheader("Config")
st.json({"mode" : mode, "count" : count})
#display selected settings in json format
#helpful for debugginh and understanding state

