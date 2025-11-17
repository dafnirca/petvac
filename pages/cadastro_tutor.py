import streamlit as st
from backend.services import cadastrar_tutor,  atualizar_tutor
from pages.style import set_css 
set_css()

st.header("🐕 Cadastro de Tutor")

nome = st.text_input("Nome do Tutor")
telefone = st.text_input("Telefone")
email = st.text_input("E-mail")
endereco = st.text_area("Endereço")

if st.button("🐕 Cadastrar Tutor"):
    if nome and telefone and email and endereco:
        msg = cadastrar_tutor(nome, telefone, email, endereco)
        st.success(msg)
    else:
        st.warning("Preencha todos os campos antes de cadastrar.")

st.header("✏️ Atualizar Dados do Tutor")

idTutor = st.number_input("ID do Tutor", min_value=1, step=1)
novo_nome = st.text_input("Novo nome (opcional)")
novo_telefone = st.text_input("Novo telefone (opcional)")
novo_email = st.text_input("Novo email (opcional)")
novo_endereco = st.text_input("Novo endereço (opcional)")

if st.button("🐶 Atualizar Tutor"):
    novos_dados = {}
    if novo_nome: novos_dados["nome"] = novo_nome
    if novo_telefone: novos_dados["telefone"] = novo_telefone
    if novo_email: novos_dados["email"] = novo_email
    if novo_endereco: novos_dados["endereco"] = novo_endereco

    if novos_dados:
        msg = atualizar_tutor(idTutor, novos_dados)
        st.success(msg)
    else:
        st.warning("Preencha ao menos um campo para atualizar.")