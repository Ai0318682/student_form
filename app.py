import streamlit as st
import gspread
import pandas as pd 
from google.oauth2.service_account import Credentials
st.set_page_config(page_title="student form",page_icon="", layout="centered")
#===color+design====
st.markdown("""
<style>
/*pora page ka background*/
.stApp{
background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);
}
/*form ka white box*/
[data-testid="stForm"]{
background-color:white;
padding:30px;
border-radius: 20px;
box-shadow:0 10px 30px rgba(0,0,0.03);
}
/*Title*/
h1{
color:white;
text-align:center;
font-weight:700;
}
/*Input box*/
.stTextInput>div>div>input,.stSelectbox>div>div>select {
     border-radius:20px;
     border:2px solid #185a9d;
     }
     </style>
     """,unsafe_allow_html=True)


#=====1. Google sheet sa connect
scope=["http://spreadsheets.google.com/feeds","http://www.googleapis.com/auth/drive"]
creds=credentials.from_service-account-info(st.secrets["gcp_service_account"],scopes=scope)
client=gspread.authorize(creds)
SHEET_NAME="student_data"
sheet=client.open(SHEET_NAME).sheet1

st.title("student registration form")
with st.form("student_form"):
      name=st.text_input("enter your name:")
     fname=st.text_input("enter your father name:")
     religion=st.selectbox("enter your religion:",("Islam","Christian","Hindu","other"))
     adr=st.text_input("enter your address:")
     age=st.text_input("enter your age:")
     classdata=st.selectbox("enter your class:",("matric","intermediate","Bachelor","Graduation","M.phil","PHD"))
     cnic=st.text_input("Enter your cnic:")
     email=st.text_input("enter your email:")
     phone=st.text_input("enter your phone number:")

     button=st.form_submit_button("Done")
if button:
     st.success("form submitted successfully")
     st.markdown("### student detail")
     st.markdown(f"name:{name}")
     st.markdown(f"father name:{fname}")   
     st.markdown(f"religion:{religion}")   
     st.markdown(f"age:{age}")
    st.markdown(f"class:{classdata}") 
    st.markdown(f"cnic:{cnic}")
    st.markdown(f"email:{email}")
    st.markdown(f"phone:{phone}") 

    st.write("### ### All saved entries")
    data=sheet.get_all_records()
    df=pd.DataFrame(data)
    st.dataframe(df,use_container_width=True)
    st.write(f"**Total Entries:** {len(df)"}
