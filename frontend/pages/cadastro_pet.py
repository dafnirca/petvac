import streamlit as st
from backend.services import cadastrar_pet_service

st.header("Cadastro de Pet")
nome = st.text_input("Nome do Pet")
especie = st.text_input("Espécie")
raca = st.text_input("Raça")
dataNascimento = st.date_input("Data de Nascimento")
idTutor = st.number_input("ID do Tutor", min_value=1, step=1)
if st.button("Cadastrar Pet"):
    msg = cadastrar_pet(nome, especie, raca, dataNascimento, idTutor)
    st.success(msg)
    
    
st.header("Atualizar Dados do Pet")
idPet = st.number_input("ID do Pet", min_value=1, step=1)
novo_nome = st.text_input("Novo nome (opcional)")
nova_especie = st.text_input("Nova espécie (opcional)")
nova_raca = st.text_input("Nova raça (opcional)")
nova_data = st.date_input("Nova data de nascimento (opcional)")
novo_tutor = st.number_input("Novo ID do tutor (opcional)", min_value=0, step=1)
if st.button("Atualizar Pet"):
    novos_dados = {}
    if novo_nome: novos_dados["nome"] = novo_nome
    if nova_especie: novos_dados["especie"] = nova_especie
    if nova_raca: novos_dados["raca"] = nova_raca
    if nova_data: novos_dados["dataNascimento"] = str(nova_data)
    if novo_tutor != 0: novos_dados["idTutor"] = novo_tutor
    if novos_dados:
        msg = atualizar_pet(idPet, novos_dados)
        st.success(msg)
    else:
        st.warning("Preencha ao menos um campo para atualizar.")
