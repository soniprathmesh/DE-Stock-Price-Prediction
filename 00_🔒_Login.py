import streamlit as st
from login import login

st.set_page_config(
    page_title="Stock Prediction App",
    page_icon="😎",
)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def main_app():
    st.sidebar.title(f"Welcome, {st.session_state['username']}!")
    st.sidebar.write("Use the navigation to switch between pages.")
    st.sidebar.button("Logout", on_click=logout)

    st.write("## Main Application")
    st.write("Content of the main application goes here.")

    # Placeholder for navigation to other pages
    st.write("Navigate to other pages from the sidebar.")

def logout():
    st.session_state['logged_in'] = False
    st.session_state['username'] = None
    st.experimental_rerun()

# Check if user is logged in
if st.session_state['logged_in']:
    main_app()
else:
    login()