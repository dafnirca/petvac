import streamlit as st
from backend.services import cadastrar_pet_service

st.title("Cadastro de Pets")

nome = st.text_input("Nome do pet")
especie = st.text_input("Espécie")
raca = st.text_input("Raça")
data_nasc = st.date_input("Data de nascimento")
id_tutor = st.number_input("ID do tutor", min_value=1)

if st.button("Cadastrar"):
    msg = cadastrar_pet_service(nome, especie, raca, data_nasc, id_tutor)
    st.success(msg)
