import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Student Form", page_icon="📝")
st.title("📝 Student Registration Form")

# CSV file ka naam
CSV_FILE = "student_data.csv"

# Agar file nahi hai to header bana do - naye columns add kar diye
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["Timestamp", "Full Name", "Roll Number", "CNIC Number", "Email", "Phone Number", "Religion", "Qualification", "Address"])
    df.to_csv(CSV_FILE, index=False)

with st.form("student_form", clear_on_submit=True):
    st.write("**Please Fill The Form**")
    
    col1, col2 = st.columns(2) # 2 column me kar diya taake form chota lage
    
    with col1:
        name = st.text_input("**Full Name**")
        roll = st.text_input("**Roll Number**")
        cnic = st.text_input("**CNIC Number**")
        email = st.text_input("**Email Address**")
    
    with col2:
        phone = st.text_input("**Phone Number**")
        religion = st.selectbox("**Religion**", ["", "Islam", "Christianity", "Hinduism", "Other"]) # Dropdown
        qualification = st.selectbox("**Qualification**", ["", "Matric", "Intermediate", "Bachelor", "Master", "Other"]) # Dropdown
    
    address = st.text_area("**Address**")
    
    # Submit button
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        if name and roll and cnic and email:
            # Naya data
            new_data = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Full Name": name,
                "Roll Number": roll,
                "CNIC Number": cnic,
                "Email": email,
                "Phone Number": phone,
                "Religion": religion,
                "Qualification": qualification,
                "Address": address
            }
            
            # CSV me add kar do
            df = pd.read_csv(CSV_FILE)
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(CSV_FILE, index=False)
            
            st.success("✅ Data Saved Successfully!")
        else:
            st.error("❌ Full Name, Roll Number, CNIC and Email are required")

st.markdown("---")
st.subheader("📊 Saved Data")
df = pd.read_csv(CSV_FILE)
st.dataframe(df, use_container_width=True)

# Download ka button
st.download_button(
    label="📥 Download CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name='student_data.csv',
    mime='text/csv'
)
