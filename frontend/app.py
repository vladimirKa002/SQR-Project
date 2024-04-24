import streamlit as st
import extra_streamlit_components as stx
from menu import menu
import datetime

st.title("Inno Food Tier list")
menu()

st.write("# Cookie Manager")


@st.cache_resource(experimental_allow_widgets=True)
def get_manager():
    return stx.CookieManager()


cookie_manager = get_manager()

st.subheader("All Cookies:")
cookies = cookie_manager.get_all()
st.write(cookies)

cookie_manager.set('token', 'test_cookie')
st.write(cookie_manager.get('token'))


# Fuck this
# if 'test' not in st.session_state:
#     st.session_state['test'] = 'test'
#     st.write('Created')
# else:
#     st.write('Readed')
