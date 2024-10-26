__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import sqlite3

import streamlit as st

from helpers.utility import check_password
from helpers.model_processing import process_user_input
from helpers.hdb_model_processing import process_user_input_hdb



if not check_password():  
    st.stop()
    
    
st.set_page_config(
    layout="centered",
    page_title="HDB Resale Helpdesk"
)

st.markdown("""
    <style>
        .reportview-container {
            background: #f0f2f5;
        }
        .stButton > button {
            background-color: #007bff;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Buying Procedure", "Terms and Conditions"])

if page == "Buying Procedure":

    st.title('Buying Procedure of a Resale HDB Flat')
    form_hdb_price = st.form(key="form_hdb")
    form_hdb_price.subheader("General Enquiries on Buying Procedure of Resale HDB Flats")
    user_prompt = form_hdb_price.text_area("Insert prompt here: ", height=200)

    if form_hdb_price.form_submit_button("Submit"):

        st.divider()
        response = process_user_input_hdb(user_prompt)
        #print(response)
        st.write(response)

        st.divider()
    
elif page == "Terms and Conditions":
    form_tnc = st.form(key="form")
    form_tnc.subheader("Terms and Conditions of Buying a Resale HDB Flat")

    user_prompt = form_tnc.text_area("What terms and conditions would you like to know about buying a resale HDB flat?", height=200)

    if form_tnc.form_submit_button("Submit"):   
        
        st.divider()
        response = process_user_input(user_prompt)
        #print(response)
        st.write(response)

        st.divider()


with st.expander("Disclaimer"):
    st.write("""
             IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. 
             The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, 
             especially those related to financial, legal, or healthcare matters.
             
             Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.
             
             Always consult with qualified professionals for accurate and personalized advice.
             """)