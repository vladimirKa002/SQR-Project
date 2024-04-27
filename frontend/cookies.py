import extra_streamlit_components as stx
import streamlit as st


@st.cache_resource(experimental_allow_widgets=True)
def get_manager():
    return stx.CookieManager()


cookie_manager = get_manager()
cookies = cookie_manager.get_all()


def get_token():
    return cookies.get('token')


def update_cookies():
    st.session_state['cookies'] = cookies
    if 'token' in st.session_state['cookies']:
        st.session_state['authentication_status'] = True
    else:
        st.session_state['authentication_status'] = False


def login_cookie(token):
    cookie_manager.set('token', token)


def logout_cookie():
    cookie_manager.delete('token')
    del st.session_state['user']


def get_user():
    if 'cookies' not in st.session_state:
        st.error("No cookies to find user")
    elif 'token' not in st.session_state['cookies']:
        st.error("No token in cookies to find user")
    else:
        # TODO: replace with API request
        st.session_state['user'] = {'name': 'Default username'}