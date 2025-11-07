import streamlit as st
from backend.services import (
    cadastrar_tutor, atualizar_tutor,
    cadastrar_pet, atualizar_pet, listar_pets,
    registrar_vacina, consultar_vacinas_pendentes, consultar_historico_pet,
    
    # Funcões que ainda não foram implementadas no backend (mas estão aqui para evitar erros)
    gerar_notificacoes_pendentes, marcar_notificacao_como_lida,
    login_usuario, logout_usuario
)
import pandas as pd


# Toda logica do frontend está aqui mas o resto do código (backend) ainda não foi implementado, para que esse código rode sem erros.
# O front ainda sera testado e implementado depois que o backend estiver pronto.

st.set_page_config(page_title="PetVac", page_icon="🐾", layout="wide")
st.title("🐾 PetVac – Sistema de Cadastro e Controle de Vacinas")

# ------------------ LOGIN ------------------
if "usuario" not in st.session_state:
    st.session_state["usuario"] = None

if st.session_state["usuario"] is None:
    st.sidebar.header("Login")
    nome = st.sidebar.text_input("Nome de usuário")
    cargo = st.sidebar.selectbox("Cargo", ["recepcionista", "veterinário"])
    if st.sidebar.button("Entrar"):
        msg = login_usuario(nome, cargo)
        st.session_state["usuario"] = {"nome": nome, "cargo": cargo}
        st.sidebar.success(msg)
else:
    st.sidebar.write(f"👤 Usuário: {st.session_state['usuario']['nome']} ({st.session_state['usuario']['cargo']})")
    if st.sidebar.button("Sair"):
        msg = logout_usuario(st.session_state["usuario"]["nome"])
        st.sidebar.success(msg)
        st.session_state["usuario"] = None
        st.rerun()

# Só mostra o sistema se estiver logado
if st.session_state["usuario"]:

    menu = st.sidebar.radio(
        "Menu principal",
        ["Cadastrar Tutor", "Atualizar Tutor",
         "Cadastrar Pet", "Atualizar Pet",
         "Registrar Vacina", "Histórico do Pet",
         "Vacinas Pendentes", "Notificações"]
    )

    # ------------------ CADASTRAR TUTOR ------------------
    if menu == "Cadastrar Tutor":
        st.header("Cadastro de Tutor")
        nome = st.text_input("Nome")
        telefone = st.text_input("Telefone")
        email = st.text_input("Email")
        endereco = st.text_input("Endereço")
        if st.button("Cadastrar Tutor"):
            msg = cadastrar_tutor(nome, telefone, email, endereco)
            st.success(msg)

    # ------------------ ATUALIZAR TUTOR ------------------
    elif menu == "Atualizar Tutor":
        st.header("Atualizar Dados do Tutor")
        idTutor = st.number_input("ID do Tutor", min_value=1, step=1)
        novo_nome = st.text_input("Novo nome (opcional)")
        novo_tel = st.text_input("Novo telefone (opcional)")
        novo_email = st.text_input("Novo email (opcional)")
        novo_endereco = st.text_input("Novo endereço (opcional)")
        if st.button("Atualizar Tutor"):
            novos_dados = {}
            if novo_nome: novos_dados["nome"] = novo_nome
            if novo_tel: novos_dados["telefone"] = novo_tel
            if novo_email: novos_dados["email"] = novo_email
            if novo_endereco: novos_dados["endereco"] = novo_endereco
            if novos_dados:
                msg = atualizar_tutor(idTutor, novos_dados)
                st.success(msg)
            else:
                st.warning("Preencha ao menos um campo para atualizar.")

    # ------------------ CADASTRAR PET ------------------
    elif menu == "Cadastrar Pet":
        st.header("Cadastro de Pet")
        nome = st.text_input("Nome do Pet")
        especie = st.text_input("Espécie")
        raca = st.text_input("Raça")
        dataNascimento = st.date_input("Data de Nascimento")
        idTutor = st.number_input("ID do Tutor", min_value=1, step=1)
        if st.button("Cadastrar Pet"):
            msg = cadastrar_pet(nome, especie, raca, dataNascimento, idTutor)
            st.success(msg)

    # ------------------ ATUALIZAR PET ------------------
    elif menu == "Atualizar Pet":
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

    # ------------------ REGISTRAR VACINA ------------------
    elif menu == "Registrar Vacina":
        st.header("Registrar Vacina")
        pets = listar_pets()
        if pets.empty:
            st.warning("Nenhum pet cadastrado ainda.")
        else:
            idPet = st.selectbox("Selecione o Pet (ID)", pets["idPet"])
            nome = st.text_input("Nome da Vacina")
            dataAplicacao = st.date_input("Data da Aplicação")
            dataProxima = st.date_input("Data da Próxima Dose")
            status = st.selectbox("Status", ["aplicada", "pendente"])
            if st.button("Registrar Vacina"):
                msg = registrar_vacina(idPet, nome, dataAplicacao, dataProxima, status)
                st.success(msg)

    # ------------------ HISTÓRICO DE VACINAS ------------------
    elif menu == "Histórico do Pet":
        st.header("Consultar Histórico de Vacinas")
        idPet = st.number_input("ID do Pet", min_value=1, step=1)
        if st.button("Consultar"):
            historico = consultar_historico_pet(idPet)
            if isinstance(historico, str):
                st.warning(historico)
            else:
                st.dataframe(historico)

    # ------------------ VACINAS PENDENTES ------------------
    elif menu == "Vacinas Pendentes":
        st.header("Vacinas Pendentes")
        df = consultar_vacinas_pendentes()
        if df.empty:
            st.info("Nenhuma vacina pendente.")
        else:
            st.dataframe(df)

    # ------------------ NOTIFICAÇÕES ------------------
    elif menu == "Notificações":
        st.header("Gerenciar Notificações")
        if st.button("Gerar Notificações"):
            msg = gerar_notificacoes_pendentes()
            st.success(msg)
        idNot = st.number_input("ID da Notificação para marcar como lida", min_value=1, step=1)
        if st.button("Marcar como Lida"):
            msg = marcar_notificacao_como_lida(idNot)
            st.success(msg)
