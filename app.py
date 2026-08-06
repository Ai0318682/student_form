import streamlit as st
import gspread
from google.oauth2.service_account import credentials
from datatime import datatime
#1. Google sheet connect
scope=["https:\\www.googleapis.com\auth\spreadsheets","https:\\www.googleapis.com\auth\drive"]
creds=credentials.form_service_account_file("student-form-app-504712-676cf390c482.json",scopes=scope)
client=gspread.authorize(creds)

Sheet_Id="1XC2VdhAjfwIW8QFZhoNDHE9pY6Zp2aFwXouTck--22Y"
sheet=client.open_by_key(Sheet_Id).sheet1
#2. visitors count wala tab
try:
    counter_sheet=client.open_by_key(Sheet_Id).worksheet("counter")
    counter_sheet.update("A1",0)

# har bar page load ho tu +1 karo
count=int(counter_sheet.acell("A1").value)
counter_sheet.update("A1",count)
# sidebar mn count dikhao
st.sidebar.title("stats")
st.sidebar.metric("total visitors",count)

st.title("student admission form")
with st. form("student_form")
name=st.text_input("enter your name:")
fname=st.text_input("Enter your father name:")
adr=st.text_area("Enter your Address:")
age=st.number_input("Enter your age:", step=1)
classdata=st.selectbox("Enter your class:",("matric","inter","bachelor","graduation","M.phil","PHD"))
cnic=st.text_input("Enter your CNIC:")



submitted=st.form_submit_button("Done")
if submitted:
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp,name,fname,adr,age,classdate,cnic])
    
    st.success("form submitted successfully!")
   
