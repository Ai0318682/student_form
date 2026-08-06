import streamlit as st
name=st.text_input("enter your name:")
fname=st.text_input("Enter your father name:")
adr=st.text_area("Enter your Text:")
classdata=st.selectbox("Enter your class:",("matric","inter","bachelor","graduation","M.phil","PHD"))


button=st.button("Done")
if button:
    st.markdown(f"name:{name},father name:{fname},address:{adr},class:{classdata}")
   