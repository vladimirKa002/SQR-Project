import streamlit as st


def authenticated_menu():
    st.sidebar.page_link("pages/account.py", label="Account")
    st.sidebar.page_link("pages/tier-lists.py", label="Tier Lists")


def unauthenticated_menu():
    st.sidebar.page_link("pages/auth.py", label="Login/Register")


def menu():
    if "authentication_status" not in st.session_state or not st.session_state['authentication_status']:
        if 'test' not in st.session_state:
            st.session_state['test'] = 'test'
            st.write('Created')
        else:
            st.write('Readed')

        unauthenticated_menu()
    else:
        authenticated_menu()


def menu_with_redirect():
    if "authentication_status" not in st.session_state or not st.session_state['authentication_status']:
        st.switch_page("pages/auth.py")
    menu()
