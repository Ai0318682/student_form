import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Student Form", page_icon="📝")
st.title("📝 Student Registration Form")

# CSV file ka naam
CSV_FILE = "student_data.csv"

# Agar file nahi hai to header bana do
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["Timestamp", "Name", "Roll No", "CNIC", "Phone", "Address"])
    df.to_csv(CSV_FILE, index=False)

with st.form("student_form", clear_on_submit=True):
    st.write("Form Fill Karein")
    
    name = st.text_input("**Name**")
    roll = st.text_input("**Roll No**")
    cnic = st.text_input("**CNIC**")
    phone = st.text_input("**Phone**")
    address = st.text_area("**Address**")
    
    # Yahi hai Save button ✅
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        if name and roll and cnic:
            # Naya data
            new_data = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": name,
                "Roll No": roll,
                "CNIC": cnic,
                "Phone": phone,
                "Address": address
            }
            
            # CSV me add kar do
            df = pd.read_csv(CSV_FILE)
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(CSV_FILE, index=False)
            
            st.success("✅ Data Saved Successfully! 🎈")
        else:
            st.error("❌ Name, Roll No aur CNIC zaroori hain")

st.markdown("---")
st.subheader("📊 Saved Data")
df = pd.read_csv(CSV_FILE)
st.dataframe(df, use_container_width=True)

# Download ka button bhi de dete hain
st.download_button(
    label="📥 Download CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name='student_data.csv',
    mime='text/csv'
)
