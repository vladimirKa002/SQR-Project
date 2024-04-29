import streamlit as st
from pages.modules.menu import menu

# st.set_page_config(layout='wide', page_title="Inno Food Tier list")
st.title("Inno Food Tier List")
menu()

st.markdown("SQR Team Project")

st.markdown("""
    **Inno Food Tier List - A Delicious Journey of Exploration!**

    Welcome to Inno Food Tier List, your one-stop shop for creating, sharing,
    and exploring the tastiest tier lists around! Built with Streamlit, this
    interactive platform empowers you to:

    * **Craft Your Own Tier Lists:** Unleash your inner food critic and curate
    personalized tier lists for any food category imaginable.
    * **Explore User-Generated Lists:** Dive into a vibrant community of food
    enthusiasts and discover diverse tier lists created by others.
    * **Save and Share Your Creations:** Preserve your culinary
    masterpieces for posterity and share them with fellow food lovers.
""")
