import streamlit as st
from menu import menu_with_redirect

st.set_page_config(page_title="Tier List", layout="wide")
menu_with_redirect()

sample_tier_lists = [
    {'name': 'Minecraft food',
     'id': 1,
     'pic': 'https://random.imagecdn.app/500/500'},
    {'name': 'Magnit food',
     'id': 2,
     'pic': 'https://random.imagecdn.app/540/500'},
    {'name': 'Пятерочка food',
     'id': 3,
     'pic': 'https://random.imagecdn.app/1000/1000'},
    {'name': 'Kazakh food',
     'id': 4,
     'pic': 'https://random.imagecdn.app/501/500'
    }
]


def print_all_tier_lists(tier_lists_):

    for i in range(0, len(tier_lists_), 5):
        col1, col2, col3, col4, col5 = st.columns(5)
        cols = [col1, col2, col3, col4, col5]
        for j in range(0, 5):
            if i + j < len(tier_lists_):
                with cols[j]:
                    with st.container(border=True):
                        st.image(tier_lists_[i + j]['pic'])
                        button = st.button(tier_lists_[i + j]['name'])
                        if button:
                            st.session_state['ID'] = tier_lists_[i + j]['id']
                            st.switch_page('pages/tier-list.py')


print_all_tier_lists(sample_tier_lists)

