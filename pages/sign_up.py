import streamlit as st
from auth_db import conn, csr

st.title("SIGNUP HERE")

col1 , col2 = st.columns(2)

with col1:
    username= st.text_input("Username : ")
with col2:
    name= st.text_input("Fullname : ")

phone= st.number_input("Phone : ", min_value=0000000000)
email= st.text_input("E-Mail : ")
password=st.text_input("Set Password : ", type="password")
confirm=st.text_input("Confirm Password : ", type="password")

btn= st.button("Sign Up")

if btn:
    if username==""or name=="" or phone=="" or email=="" or password=="" or confirm=="":
        st.error("Fill all fields!")
        st.snow()

    else:
        try:
            if password!= confirm:
                st.warning("Password doesn't match with Confirm Password!")
                st.image(r"C:\Users\Dell\OneDrive\Desktop\streamlit\lec 2 project1\images\dontmatch.jpeg")

            else:
                csr.execute(f"insert into signup(username, fullname, phone_number, email, passwordd) values('{username}','{name}','{phone}','{email}','{password}')")

                conn.commit()
                st.success("SIGN UP Successfully")
                st.balloons()

                st.markdown("[Go to Login Page](./login)")



        except Exception as e:
            st.error("Please check username must be unique!")