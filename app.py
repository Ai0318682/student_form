import streamlit as st
name=st.text_input("enter your name:")
fname=st.text_input("Enter your father name:")
adr=st.text_area("Enter your Address:")
age=st.number_input("Enter your age:", step=1)
classdata=st.selectbox("Enter your class:",("matric","inter","bachelor","graduation","M.phil","PHD"))
cnic=st.text_input("Enter your CNIC:")



button=st.button("Done")
if button:
    st.success("form submitted successfully!")
    st.markdown(f"name:{name},father name:{fname},address:{adr},age:{age},class:{classdata},cnic:{cnic}")
   
