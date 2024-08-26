import streamlit as st
import streamlit.components.v1 as components
import json 
import supabase
from supabase import create_client, Client

st.title("Anonymous Test")   

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

def anonymous_login():
    data = supabase.auth.sign_in_anonymously()
    if data.user:
        st.session_state.user = data.user
        st.success("welcome")
    else:
        st.warning("Login failed. check your credentials.")
      
st.button('Anonymous Login ', on_click=anonymous_login, help='click on this button to login anonymously')

