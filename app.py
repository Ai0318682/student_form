import streamlit as st
name=st.text_input("enter your name:")
fname=st.text_input("enter your father name:")
religion=st.text_input("enter your religion:")
adr=st.text_input("enter your address:")
age=st.text_input("enter your age:",step=1)
classdata=st.selectbox("enter your class:",("matric","intermediate","Bachelor","Graduation","M.phil","PHD"))
cnic=st.text_input("Enter your CNIC")

button=st.button("Done")
if button:
    st.success("form submitted successfully")
    st.markdown(f"name:{name},father name:{fname}, religion:{religion},address:{adr},age:{age},class:{classdata},cnic:{CNIC}")
