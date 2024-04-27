import streamlit as st
from menu import menu_with_redirect_auth
from cookies import login
from requests import Session

session = Session()

API_URL = "http://127.0.0.1:8000"

st.set_page_config(layout='centered')
st.title("Login/Register")
login_tab, register_tab = st.tabs(["Login", "Register"])


skip = True

with login_tab:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:

        if skip:
            login('some-token')
        else:
            login_response = session.post(
                API_URL + "/users/login", json={"username": username, "password": password}
            )

            if login_response.status_code == 200:
                # access_token = login_response.json()["access_token"]
                st.success("Login successful!")

                # headers = {"Authorization": f"Bearer {access_token}"}

            else:
                st.error("Login failed!")
                st.error(login_response)
                st.error(login_response.json())

with register_tab:
    name = st.text_input("Name", key=2)
    email = st.text_input("Email", key=3)
    password = st.text_input("Password", type="password", key=4)

    register_button = st.button("Register")

    if register_button:
        register_response = session.post(
            API_URL + "/users/register",
            json={"name": username, "email": email, "password": password},
        )

        if register_response.status_code == 200:
            st.success("Registration successful! Please login.")
        else:
            st.error("Registration failed!")
            st.error(register_response)
            st.error(register_response.json())

menu_with_redirect_auth()
