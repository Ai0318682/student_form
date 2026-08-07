import json
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Google Sheets setup
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

creds = Credentials.from_service_account_info(
    json.loads(st.secrets["gcp_service_account_json"]), scopes=scope
)
gc = gspread.authorize(creds)

# Open your sheet
sh = gc.open("Student form") # <-- Tumhari sheet ka naam "Student form" hai
worksheet = sh.sheet1

st.title("Student Registration Form")

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
            st.success("Data Saved Successfully!")
            st.balloons()
