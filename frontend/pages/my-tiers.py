import streamlit as st
from menu import menu_with_redirect, convertImage
from APIs import getTierListsAllApi

st.set_page_config(page_title="My Tier Lists", layout="wide")
menu_with_redirect()


def print_all_tier_lists(tier_lists_):
    num_cols = 5
    for i in range(0, len(tier_lists_), num_cols):
        cols = st.columns(num_cols)
        for j in range(0, num_cols):
            if i + j < len(tier_lists_):
                with cols[j]:
                    with st.container(border=True):
                        st.image(convertImage(tier_lists_[i + j]['template']['picture']))
                        button = st.button(tier_lists_[i + j]['template']['name'])
                        if button:
                            st.session_state['id'] = tier_lists_[i + j]['template']['id']
                            st.switch_page('pages/tier.py')


templates = getTierListsAllApi()
print_all_tier_lists(templates)
# print_all_tier_lists(sample_tier_lists)

