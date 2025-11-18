import streamlit as st
from backend.services import cadastrar_pet, atualizar_pet, listar_pets, listar_tutores
from pages.style import set_css 

set_css()

def tutor_label(row):
    return f"{row['idTutor']} - {row['nome']} ({row['telefone']})"

def pet_label(row):
    return f"{row['idPet']} - {row['nome']} ({row['raca']}) — Tutor: {row['nome_tutor']}"

tutores_df = listar_tutores()
pets_df = listar_pets()


# ------------------ CADASTRO DE PET ------------------
st.header("🐕 Cadastro de Pet")

nome = st.text_input("Nome do Pet")
especie = st.text_input("Espécie")
raca = st.text_input("Raça")
dataNascimento = st.date_input("Data de Nascimento")

# SELECTBOX de tutor
if not tutores_df.empty:
    tutor_pet = st.selectbox(
        "Tutor do Pet",
        tutores_df.apply(tutor_label, axis=1)
    )
    idTutor_pet = int(tutor_pet.split(" - ")[0])
else:
    st.warning("Cadastre um tutor antes de cadastrar pets.")
    idTutor_pet = None

if st.button("Cadastrar Pet"):
    if idTutor_pet:
        msg = cadastrar_pet(nome, especie, raca, dataNascimento, idTutor_pet)
        st.success(msg)
    else:
        st.warning("Selecione um tutor válido.")


# ------------------ ATUALIZAÇÃO DE PET ------------------
st.header("✏️ Atualizar Dados do Pet")

pets_df = listar_pets()

# 🔥 Merge pets + tutores para incluir nome do tutor no label
if not pets_df.empty and not tutores_df.empty:
    pets_df = pets_df.merge(
        tutores_df[['idTutor', 'nome']],
        on='idTutor',
        how='left',
        suffixes=('', '_tutor')
    )
else:
    st.info("Nenhum pet cadastrado.")
    pets_df = pd.DataFrame()

if not pets_df.empty:
    pet_escolhido = st.selectbox(
        "Selecione o Pet",
        pets_df.apply(pet_label, axis=1)
    )
    idPet = int(pet_escolhido.split(" - ")[0])

    novo_nome = st.text_input("Novo nome (opcional)")
    nova_especie = st.text_input("Nova espécie (opcional)")
    nova_raca = st.text_input("Nova raça (opcional)")
    nova_data = st.date_input("Nova data de nascimento (opcional)")

    tutor_novo = st.selectbox(
        "Novo tutor (opcional)",
        ["Não alterar"] + list(tutores_df.apply(tutor_label, axis=1))
    )

    novos_dados = {}
    if novo_nome: novos_dados["nome"] = novo_nome
    if nova_especie: novos_dados["especie"] = nova_especie
    if nova_raca: novos_dados["raca"] = nova_raca
    if nova_data: novos_dados["dataNascimento"] = str(nova_data)
    if tutor_novo != "Não alterar":
        novos_dados["idTutor"] = int(tutor_novo.split(" - ")[0])

    if st.button("🐶 Atualizar Pet"):
        if novos_dados:
            msg = atualizar_pet(idPet, novos_dados)
            st.success(msg)
        else:
            st.warning("Preencha ao menos um campo para atualizar.")
