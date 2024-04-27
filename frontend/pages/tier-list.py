import streamlit as st
from menu import menu_with_redirect


menu_with_redirect()


def move_item_up(tier, item):
    prev_tier = None
    for cur_tier in st.session_state.tiers.keys():
        if tier == cur_tier and prev_tier:
            st.session_state.tiers[prev_tier].append(item)
            st.session_state.tiers[tier].remove(item)
            break
        prev_tier = cur_tier


def move_item_down(tier, item):
    prev_tier = None
    for cur_tier in st.session_state.tiers.keys():
        if tier == prev_tier:
            st.session_state.tiers[cur_tier].append(item)
            st.session_state.tiers[tier].remove(item)
            break
        prev_tier = cur_tier


def print_tier_list(objects_, tier_list_):
    st.session_state['objects'] = objects_
    st.session_state['tiers'] = tier_list_

    for tier, items in st.session_state.tiers.items():
        with st.container(border=True):
            tierCol, itemsCol = st.columns([0.2, 0.8])

            with tierCol:
                st.write(tier)

            with itemsCol:
                for i in range(0, len(items), 5):
                    col1, col2, col3, col4, col5 = st.columns(5)
                    cols = [col1, col2, col3, col4, col5]
                    for j in range(0, 5):
                        if i + j < len(items):
                            with cols[j]:
                                with st.popover(items[i + j]['name']):
                                    st.write(items[i + j]['name'])
                                    delete = st.button("Delete", key=f"{tier}{i + j}_delete")
                                    edit = st.button("Edit", key=f"{tier}{i + j}_edit")
                                    move_up = st.button("Move Up", key=f"{tier}{i + j}_move_up")
                                    move_down = st.button("Move Down", key=f"{tier}{i + j}_move_down")
                                    if delete:
                                        st.session_state['objects'].append(items[i + j])
                                        st.session_state['tiers'][tier].remove(items[i + j])
                                        st.rerun()
                                    if move_up:
                                        move_item_up(tier, items[i + j])
                                        st.rerun()
                                    if move_down:
                                        move_item_down(tier, items[i + j])
                                        st.rerun()
    with st.container(border=True):
        objects = st.session_state['objects']
        for i in range(0, len(objects), 6):
            col1, col2, col3, col4, col5, col6 = st.columns(6)
            cols = [col1, col2, col3, col4, col5, col6]
            for j in range(0, 6):
                if i + j < len(objects):
                    with cols[j]:
                        with st.popover(objects[i + j]['name']):
                            st.write(objects[i + j]['name'])
                            edit = st.button("Edit", key=f"{tier}{i + j}_edit")
                            move_to = st.selectbox(
                                "Move To:", ('S', 'A', 'B', 'C', 'F'),
                                index=None,
                                key=f"{tier}{i + j}_move_to")
                            if edit:
                                # st.session_state['objects'][tier].remove(items[i + j])
                                st.rerun()
                            if move_to:
                                item = objects[i + j]
                                st.session_state['tiers'][move_to].append(item)
                                st.session_state['objects'].remove(item)
                                st.rerun()


sample_tier_list = {
    "S": [{'name': 'Кумыс',
           'id': 1,
           'pic': 'somepic1'},
          {'name': 'Melon',
           'id': 2,
           'pic': 'somepic2'}],
    "A": [{'name': 'Apple',
           'id': 3,
           'pic': 'somepic3'}],
    "B": [],
    "C": [{'name': 'Pineapple',
           'id': 4,
           'pic': 'somepic4'}],
    "F": []
}
sample_objects = [
    {'name': 'Watermelon',
     'id': 5,
     'pic': 'somepic5'},
    {'name': 'Banana',
     'id': 6,
     'pic': 'somepic6'}]

print_tier_list(sample_objects, sample_tier_list)
