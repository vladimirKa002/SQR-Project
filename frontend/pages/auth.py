import streamlit as st
import extra_streamlit_components as stx
from menu import menu
from requests import Session

session = Session()

API_URL = "http://127.0.0.1:8000"

st.title("Login/Register")
login, register = st.tabs(["Login", "Register"])


@st.cache_resource(experimental_allow_widgets=True)
def get_manager():
    return stx.CookieManager()


cookie_manager = get_manager()

skip = True

with login:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:

        if skip:
            st.session_state['authentication_status'] = True
            st.session_state['user'] = {'name': 'Default username'}
            st.switch_page('pages/account.py')
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

with register:
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

menu()
