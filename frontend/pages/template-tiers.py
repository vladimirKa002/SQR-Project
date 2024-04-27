import streamlit as st
from menu import menu_with_redirect, convertImage
from APIs import getTemplateAllApi

st.set_page_config(page_title="Template Tier Lists", layout="wide")
menu_with_redirect()


def print_all_tier_lists(templates_):
    num_cols = 5
    for i in range(0, len(templates_), num_cols):
        cols = st.columns(num_cols)
        for j in range(0, 5):
            if i + j < len(templates_):
                with cols[j]:
                    with st.container(border=True):
                        st.image(convertImage(templates_[i + j]['picture']))
                        button = st.button(templates_[i + j]['name'])
                        if button:
                            st.session_state['id'] = templates_[i + j]['id']
                            st.switch_page('pages/tier.py')


templates = getTemplateAllApi()
print_all_tier_lists(templates)
# print_all_tier_lists(sample_tier_lists)

