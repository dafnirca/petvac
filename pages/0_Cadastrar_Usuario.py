import streamlit as st
from backend.services import cadastrar_usuario
from pages.style import set_css

set_css()

st.title("Cadastrar novo usuário")

with st.form("form_cadastro"):
    nome = st.text_input("Nome")
    senha = st.text_input("Senha")
    cargo = st.selectbox("Cargo", ["recepcionista", "veterinario"])
    btn = st.form_submit_button("Cadastrar")

if btn:
    sucesso, msg = cadastrar_usuario(nome, senha, cargo)
    if sucesso:
        st.success(msg)
        st.info("Volte ao login para entrar.")
    else:
        st.error(msg)