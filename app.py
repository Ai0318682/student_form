import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Student Registration Form", page_icon="📝")
st.title("📝 Student Registration Form")
st.caption("Your data is 100% private. Nothing is stored on server.")

# Session state
if 'csv_data' not in st.session_state:
    st.session_state.csv_data = None
    st.session_state.file_name = None

st.write("**Please Fill The Form Carefully**")

with st.form("student_form", clear_on_submit=True):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("**Full Name** *")
        roll = st.text_input("**Roll Number** *")
        age = st.number_input("**Age**", min_value=10, max_value=100, step=1)
        gender = st.selectbox("**Gender**", ["", "Male", "Female", "Other"]) # Naya field
        cnic = st.text_input("**CNIC Number** *")

    with col2:
        email = st.text_input("**Email Address** *")
        phone = st.text_input("**Phone Number**")
        religion = st.selectbox("**Religion**", ["", "Islam", "Christianity", "Hinduism", "Other"])
        qualification = st.selectbox("**Qualification**", ["", "Matric", "Intermediate", "Bachelor", "Master", "PHD"])

    address = st.text_area("**Address**")

    submitted = st.form_submit_button("Submit")

    if submitted:
        if name and roll and cnic and email and gender: # Gender ko bhi required kar diya
            student_data = {
                "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                "Full Name": [name],
                "Roll Number": [roll],
                "Age": [age],
                "Gender": [gender], # Naya field CSV me
                "CNIC Number": [cnic],
                "Email": [email],
                "Phone Number": [phone],
                "Religion": [religion],
                "Qualification": [qualification],
                "Address": [address]
            }

            df_single = pd.DataFrame(student_data)
            csv = df_single.to_csv(index=False).encode('utf-8')

            st.session_state.csv_data = csv
            st.session_state.file_name = f'{name}_{roll}.csv'
            st.success(f"Done {name}! Your data is ready to download.")
        else:
            st.error("Full Name, Roll Number, Gender, CNIC and Email are required *")

# Download button form ke bahar
if st.session_state.csv_data is not None:
    st.info("Note: Please download your file. We don't save your data.")
    st.download_button(
        label="Download Your Data as CSV",
        data=st.session_state.csv_data,
        file_name=st.session_state.file_name,
        mime='text/csv'
    )
