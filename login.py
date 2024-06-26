# login.py
import streamlit as st
import hashlib



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Predefined users (Add your credentials here)
users = {
    "user1": hash_password("password123"),
    "admin": hash_password("mk"),
    "janak": hash_password("Janak"),
    "manthan": hash_password("Manthan"),
    "pk": hash_password("Pk"),
    "vraj": hash_password("Vraj"),
    "prathmesh": hash_password("Prathmesh"),
}

def check_credentials(username, password):
    if username in users and users[username] == hash_password(password):
        return True
    return False


def login():
    st.title("Login")
    if st.session_state.get('login_message'):
        st.success(st.session_state['login_message'])
        st.session_state['login_message']=''

    with st.form(key='login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button(label='Login')

    if submit_button:
        if check_credentials(username, password):
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            # st.experimental_rerun()
            st.rerun()
        else:
            st.error("Invalid username or password")

