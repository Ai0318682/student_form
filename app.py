import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Page setup
st.set_page_config(page_title="Student Registration Form", page_icon="📝")

# Google Sheets connect
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
import json
creds = Credentials.from_service_account_info(
 json.loads(st.secrets)["gcp_service_account_json"], scopes=scope
)
client = gspread.authorize(creds)

# Apni Google Sheet ka naam yahan likho
SHEET_NAME = "StudentData" 

try:
    sheet = client.open(SHEET_NAME).sheet1
except:
    st.error(f"'{SHEET_NAME}' naam ki sheet nahi mili. Pehle Google Drive me bana lo.")
    st.stop()


st.title("📝 Student Registration Form")
st.write("Neeche apni details fill karein")

with st.form("student_form"):
    name = st.text_input("Full Name")
    roll_no = st.text_input("Roll Number")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    course = st.selectbox("Course", ["BSSE", "BSCS", "BSIT", "Other"])
    
    submitted = st.form_submit_button("Submit")

    if submitted:
        if name and roll_no and email:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_row = [timestamp, name, roll_no, email, phone, course]
            sheet.append_row(new_row)
            st.success(f"Shukriya {name}! Aapka data save ho gaya ✅")
            st.balloons()
        else:
            st.warning("Name, Roll No aur Email zaroori hain")


st.write("---")
st.caption("Made with Streamlit")

