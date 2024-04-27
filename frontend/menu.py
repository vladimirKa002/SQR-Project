import streamlit as st
from cookies import logout_cookie, update_cookies


def authenticated_menu():
    st.sidebar.page_link("pages/account.py", label="Account")
    st.sidebar.page_link("pages/tier-lists.py", label="Tier Lists")
    if st.sidebar.button('Logout'):
        logout_cookie()


def unauthenticated_menu():
    st.sidebar.page_link("pages/auth.py", label="Login/Register")


def menu():
    st.sidebar.page_link("app.py", label="Home")
    update_cookies()
    if not st.session_state['authentication_status']:
        unauthenticated_menu()
    else:
        authenticated_menu()


def menu_with_redirect():
    update_cookies()
    if not st.session_state['authentication_status']:
        st.switch_page("pages/auth.py")
    menu()


def menu_with_redirect_auth():
    update_cookies()
    if st.session_state['authentication_status']:
        st.switch_page("pages/account.py")
    menu()

