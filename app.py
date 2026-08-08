import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Student Form", page_icon="📝")
st.title("📝 Student Registration Form")
st.caption("Your data is private. It will not be stored anywhere.")

st.write("**Please Fill The Form**")

with st.form("student_form", clear_on_submit=True):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("**Full Name**")
        roll = st.text_input("**Roll Number**")
        cnic = st.text_input("**CNIC Number**")
        email = st.text_input("**Email Address**")

    with col2:
        phone = st.text_input("**Phone Number**")
        religion = st.selectbox("**Religion**", ["", "Islam", "Christianity", "Hinduism", "Other"])
        qualification = st.selectbox("**Qualification**", ["", "Matric", "Intermediate", "Bachelor", "Master", "M.phil","PHD"])

    address = st.text_area("**Address**")

    submitted = st.form_submit_button("Submit & Download")

    if submitted:
        if name and roll and cnic and email:
            # Sirf isi student ka data
            student_data = {
                "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                "Full Name": [name],
                "Roll Number": [roll],
                "CNIC Number": [cnic],
                "Email": [email],
                "Phone Number": [phone],
                "Religion": [religion],
                "Qualification": [qualification],
                "Address": [address]
            }

            df_single = pd.DataFrame(student_data)
            csv = df_single.to_csv(index=False).encode('utf-8')

            st.success(f"✅ Done {name}!")
            st.info("Download your file below. We don't save your data.")

            st.download_button(
                label="📥 Download Your Data as CSV",
                data=csv,
                file_name=f'{name}_{roll}.csv',
                mime='text/csv'
            )
        else:
            st.error("❌ Full Name, Roll Number, CNIC and Email are required")
