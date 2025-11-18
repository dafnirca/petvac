import streamlit as st
from backend.services import login_usuario, logout_usuario, cadastrar_usuario
from pages.style import set_css

set_css()

st.set_page_config(page_title="PetVac", page_icon="🐾", layout="wide")

if "usuario" not in st.session_state:
    st.session_state["usuario"] = None

# -----------------------------------------------------------
# Tela de login
# -----------------------------------------------------------

def pagina_login():
    st.title("🐾 PetVac")
    st.subheader("Acesso ao sistema")

    if "mostrar_cadastro" not in st.session_state:
        st.session_state["mostrar_cadastro"] = False
    if "erro_login" not in st.session_state:
        st.session_state["erro_login"] = None

    nome = st.text_input("Nome completo")
    senha = st.text_input("Senha", type="password")
    cargo = st.selectbox("Cargo", ["recepcionista", "veterinario"])

    # ------ EXIBE ERRO DO LOGIN (se houver) ------
    if st.session_state["erro_login"]:
        st.error(st.session_state["erro_login"])

    # ------ BOTÃO LOGIN ------
    if st.button("Entrar"):
        sucesso, msg = login_usuario(nome, senha, cargo)

        if sucesso:
            st.success(msg)
            st.session_state["usuario"] = {"nome": nome, "senha": senha, "cargo": cargo}
            st.session_state["erro_login"] = None
            st.session_state["mostrar_cadastro"] = False
            st.rerun()

        else:
            st.session_state["erro_login"] = msg
            st.session_state["mostrar_cadastro"] = True
            st.rerun()

    # ------ MOSTRAR CADASTRO SE LOGIN FALHOU ------
    if st.session_state["mostrar_cadastro"]:
        st.divider()
        st.subheader("Cadastrar novo usuário")

        nome_cad = st.text_input("Nome", key="nome_cad")
        senha_cad = st.text_input("Senha", type="password", key="senha_cad")
        cargo_cad = st.selectbox("Cargo", ["recepcionista", "veterinario"], key="cargo_cad")

        if st.button("Cadastrar usuário"):
            sucesso, msg = cadastrar_usuario(nome_cad, senha_cad, cargo_cad)
            if sucesso:
                st.success(msg)
                st.info("Agora faça o login com suas credenciais.")
                st.session_state["mostrar_cadastro"] = False
                st.session_state["erro_login"] = None
                st.rerun()
            else:
                st.error(msg)



if st.session_state["usuario"] is None:
    pagina_login()
    st.stop()   # <-- IMPORTANTE (bloqueia a criação das páginas)



# -----------------------------------------------------------
# A PARTIR DAQUI, ele está logado
# As páginas SÓ são criadas agora!!
# -----------------------------------------------------------

# Botão de logout
st.sidebar.write(f"👤 {st.session_state['usuario']['nome']}")
if st.sidebar.button("Sair"):
    usuario = st.session_state["usuario"]
    logout_usuario(usuario["nome"], usuario["senha"], usuario["cargo"])
    st.session_state["usuario"] = None
    st.rerun()


pages = [
    st.Page("pages/home.py", title="Início"), 
    st.Page("pages/cadastro_tutor.py", title="Tutores"),
    st.Page("pages/cadastro_pet.py", title="Pets"),
    st.Page("pages/vacinas.py", title="Vacinas"),
    st.Page("pages/historico.py", title="Histórico do Pet"),
    st.Page("pages/0_Cadastrar_Usuario.py", title="Cadastrar Usuário")
]

navigator = st.navigation(pages)
navigator.run()