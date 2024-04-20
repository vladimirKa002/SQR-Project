import streamlit as st
import requests

st.set_page_config(page_title="Inno Food Tier list")

st.title("Inno Food Tier list")

name = st.text_input("Name")
email = st.text_input("Email")