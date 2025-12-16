import streamlit as st

# resgitration form
with st.form(key="reg_form"):
   username = st.text_input("Enter Your Name")
   last_name = st.text_input("Enter Your Last Name")
   age = st.slider("Age",10, 100 , 25 , 1)
   addr = st.text_area("Adrress")
   submit_btn = st.form_submit_button("Submit")

   if submit_btn:
      err = ""
      if not username:
         is_err = True
         err += "please enter your name,     "
      if not last_name:
         is_err = True
         err += "please enter your last_name, "
      if not addr:
         is_err = True
         err += "please enter your address"
      if is_err:
         st.error(err)
      st.success("Saved successfully")

