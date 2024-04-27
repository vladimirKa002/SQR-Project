import streamlit as st
from menu import menu_with_redirect
from cookies import get_user

st.title('Account')
menu_with_redirect()

get_user()
st.write(st.session_state['user']['name'])
