import json
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

st.set_page_config(page_title="Student Registration Form")

# Google Sheets setup
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

try:
    uploaded_file=st.file_uploader("upload service_account.json file",type="json")
    if uploaded_file is not None:
        creds=json.load(uploaded_file)
   else:
       st.stop()
    
    
    gc = gspread.authorize(creds)
    sh = gc.open("Student form") # Tumhari sheet ka naam
    worksheet = sh.sheet1
    connection_ok = True
except Exception as e:
    st.error(f"Google Sheet se connect nahi ho pa raha: {e}")
    connection_ok = False

st.title("📝 Student Registration Form")

if connection_ok:
    with st.form("student_form"):
        name = st.text_input("Full Name *")
        roll = st.text_input("Roll No *")
        cnic = st.text_input("CNIC", placeholder="xxxxx-xxxxxxx-x")
        religion = st.selectbox("Religion", ["Islam", "Christianity", "Hinduism", "Other"])
        address = st.text_area("Address")
        email = st.text_input("Email")
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if name == "" or roll == "":
                st.error("Name aur Roll No zaroori hain *")
            else:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                worksheet.append_row([timestamp, name, roll, cnic, religion, address, email])
                st.success("✅ Data Saved Successfully!")
                st.balloons()

