import streamlit as st

st.set_page_config(page_title="PetVac", page_icon="🐾", layout="wide")

from backend.services import login_usuario, logout_usuario
from frontend.pages.style import set_css

set_css()

st.title("🐾 PetVac – Login")

# ------------------ LOGIN ------------------
if "usuario" not in st.session_state:
    st.session_state["usuario"] = None

if st.session_state["usuario"] is None:

    st.write("")  
    st.write("")  

    col1, col2, col3 = st.columns([1, 1.5, 1])

    with col2:
        st.markdown("### 🔐 Acesse sua conta")
        nome = st.text_input("Nome de usuário")
        cargo = st.selectbox("Cargo", ["recepcionista", "veterinário", "tutor"])

        if st.button("Entrar", use_container_width=True):
            msg = login_usuario(nome, cargo)
            if msg.startswith("✅"):
                st.session_state["usuario"] = {"nome": nome, "cargo": cargo}
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)

    st.stop()  # impede de mostrar o resto antes de logar


# ==================== ÁREA LOGADA ====================
st.sidebar.write(
    f"👤 Usuário: **{st.session_state['usuario']['nome']}** "
    f"({st.session_state['usuario']['cargo']})"
)

if st.sidebar.button("Sair"):
    msg = logout_usuario(st.session_state["usuario"]["nome"])
    st.sidebar.info(msg)
    st.session_state["usuario"] = None
    st.rerun()

# ------------------ MENU DO SISTEMA ------------------
menu = st.sidebar.radio(
    "Menu principal",
    [
        "Cadastrar Tutor", "Atualizar Tutor",
        "Cadastrar Pet", "Atualizar Pet",
        "Registrar Vacina", "Histórico do Pet",
        "Vacinas Pendentes", "Notificações"
    ]
)

st.write(f"📌 **Você está no menu:** {menu}")
