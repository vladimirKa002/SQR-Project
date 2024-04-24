import streamlit as st
import pandas as pd
from menu import menu_with_redirect

st.set_page_config(page_title="Tier List", layout="wide", initial_sidebar_state="expanded")

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


def tier_manager():
    for tier, items in st.session_state.tiers.items():

        st.write(f"## {tier} Tier")
        if not len(items):
            continue
        columns = st.columns(len(items))
        for col, item in zip(columns, items):
            with col:
                with st.popover(f"{item}", use_container_width=False):
                    delete = st.button("Delete", key=f"{tier}_{item}_delete")
                    # edit = st.button("Edit", key=f"{tier}_{item}_edit")
                    move_up = st.button("Move Up", key=f"{tier}_{item}_move_up")
                    move_down = st.button("Move Down", key=f"{tier}_{item}_move_down")
                    if delete:
                        st.session_state.tiers[tier].remove(item)
                        st.rerun()
                    if move_up:
                        move_item_up(tier, item)
                        st.rerun()
                    if move_down:
                        move_item_down(tier, item)
                        st.rerun()


if 'template' in st.query_params.keys():
    st.query_params["template"]
else:
    st.write("no template param")

if "tiers" not in st.session_state:   # TODO: Try multiselect as tier-list
    st.session_state.tiers = {
        "S": [1, 2, 3, 4],
        "A": [5],
        "B": [],
        "C": [],
        "F": []
    }

data = []
for tier, items in st.session_state.tiers.items():
    items_list = list(items)
    data.append({"Tier": tier, "Items": items_list})

df = pd.DataFrame(data)
st.dataframe(df, hide_index=True, use_container_width=True)

with st.sidebar:
    menu_with_redirect()
    tier_manager()

