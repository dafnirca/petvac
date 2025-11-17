import streamlit as st

def check_login():
    if "usuario" not in st.session_state or st.session_state["usuario"] is None:
        st.error("Você precisa fazer login para acessar esta página.")
        st.stop()
