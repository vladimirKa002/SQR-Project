import streamlit as st
from menu import menu_with_redirect, convertImage
from APIs import getItemByIdApi, getTierListByIdApi, rankItemApi


menu_with_redirect()

if 'id' not in st.query_params:
    st.query_params['id'] = st.session_state['id']


def move_item_up(tier, item):
    prev_tier = None
    for cur_tier in st.session_state.tiers.keys():
        if tier == cur_tier and prev_tier:
            st.session_state.tiers[prev_tier].append(item)
            st.session_state.tiers[tier].remove(item)
            rankItemApi(item['id'], st.query_params['id'], prev_tier)
            break
        prev_tier = cur_tier


def move_item_down(tier, item):
    prev_tier = None
    for cur_tier in st.session_state.tiers.keys():
        if tier == prev_tier:
            st.session_state.tiers[cur_tier].append(item)
            st.session_state.tiers[tier].remove(item)
            rankItemApi(item['id'], st.query_params['id'], cur_tier)
            break
        prev_tier = cur_tier


def move_item_to_tier(tier, item):
    st.session_state['tiers'][tier].append(item)
    st.session_state['objects'].remove(item)
    rankItemApi(item['id'], st.query_params['id'], tier)


def delete_from_tier(tier, item):
    st.session_state['objects'].append(item)
    st.session_state['tiers'][tier].remove(item)
    rankItemApi(item['id'], st.query_params['id'], '_')


def print_tier_list(objects_, tier_list_):
    if 'objects' not in st.session_state:
        st.session_state['objects'] = objects_
    if 'tiers' not in st.session_state:
        st.session_state['tiers'] = tier_list_

    for tier, items in st.session_state.tiers.items():
        with st.container(border=True):
            tierCol, itemsCol = st.columns([0.2, 0.8])

            with tierCol:
                st.write(tier)

            with itemsCol:
                num_cols = 8
                for i in range(0, len(items), num_cols):
                    cols = st.columns(num_cols)
                    for j in range(0, num_cols):
                        if i + j < len(items):
                            with cols[j]:
                                st.image(convertImage(items[i + j]['picture']))
                                with st.popover(items[i + j]['name']):
                                    st.write(items[i + j]['name'])
                                    st.write(items[i + j]['description'])
                                    delete = st.button("Delete", key=f"{tier}{i + j}_delete")
                                    move_up = st.button("Move Up", key=f"{tier}{i + j}_move_up")
                                    move_down = st.button("Move Down", key=f"{tier}{i + j}_move_down")
                                    if delete:
                                        delete_from_tier(tier, items[i + j])
                                        st.rerun()
                                    if move_up:
                                        move_item_up(tier, items[i + j])
                                        st.rerun()
                                    if move_down:
                                        move_item_down(tier, items[i + j])
                                        st.rerun()
    with st.container(border=True):
        objects = st.session_state['objects']
        num_cols = 8
        for i in range(0, len(objects), num_cols):
            cols = st.columns(num_cols)
            for j in range(0, num_cols):
                if i + j < len(objects):
                    with cols[j]:
                        st.image(convertImage(objects[i + j]['picture']))
                        with st.popover(objects[i + j]['name']):
                            st.write(objects[i + j]['name'])
                            st.write(objects[i + j]['description'])
                            st.write(objects[i + j]['price'])
                            move_to = st.selectbox(
                                "Move To:", ('S', 'A', 'B', 'C', 'F'),
                                index=None,
                                key=f"  {i + j}_move_to")
                            apply = st.button('Apply', key=f"{i + j}_apply")
                            if move_to and apply:
                                move_item_to_tier(move_to, objects[i + j])
                                st.rerun()


tier_list = {
    "S": [],
    "A": [],
    "B": [],
    "C": [],
    "F": []
}
data = getTierListByIdApi(st.query_params['id'])
for item in data['items']:
    getItem = getItemByIdApi(item['item_id'])
    tier_list[item["tier"]].append(getItem)

item_ids = [item["item_id"] for item in data['items']]
objects = [item for item in data['template']['items'] if item not in item_ids]

print_tier_list(objects, tier_list)
