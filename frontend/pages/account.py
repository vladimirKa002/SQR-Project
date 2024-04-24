import streamlit as st
from menu import menu_with_redirect

st.title('Account')
menu_with_redirect()

st.write(st.session_state['user']['name'])

