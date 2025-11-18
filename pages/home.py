# pages/home.py  (ou Home.py na raiz)
import streamlit as st
import pandas as pd
from pages.style import set_css
from backend.database import carregar_dados, COLUNAS

set_css()
IMG_URL = "https://i.pinimg.com/1200x/ab/0f/b1/ab0fb125d618485b65f4ed3b64163e3a.jpg"
st.image(IMG_URL, use_container_width=True)

st.markdown("<h1 style='text-align: center;'>🐾 PetVac</h1>", unsafe_allow_html=True)

pets_df = carregar_dados("data/pets.csv", COLUNAS["pets"])
tutores_df = carregar_dados("data/tutores.csv", COLUNAS["tutores"])
vacinas_df = carregar_dados("data/vacinas.csv", COLUNAS["vacinas"])

try:
    pendentes_df = vacinas_df[vacinas_df["status"] == "pendente"]
except Exception:
    pendentes_df = pd.DataFrame()

total_tutores = len(tutores_df)
total_pets = len(pets_df)
total_vacinas = len(vacinas_df)
total_pendentes = len(pendentes_df)

# ==========================
#  RESUMO COM NÚMEROS
# ==========================

st.write("")

colA, colB, colC, colD = st.columns(4)
colA.metric("👤 Tutores cadastrados", total_tutores)
colB.metric("🐶 Pets cadastrados", total_pets)
colC.metric("💉 Vacinas registradas", total_vacinas)
colD.metric("⏳ Pendentes", total_pendentes)
st.write("---")

# ==========================
#   CARDS DA HOME
# ==========================

st.markdown("""
<style>
.feature-card {
    padding: 20px;
    border-radius: 15px;
    background-color: #ffffff10;
    border: 1px solid #ffffff30;
    backdrop-filter: blur(10px);
    box-shadow: 0px 4px 8px #00000025;
    transition: 0.2s ease-in-out;
}
.feature-card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 6px 12px #00000035;
}
.feature-icon {
    font-size: 35px;
    text-align: center;
}
.feature-title {
    font-size: 20px;
    font-weight: bold;
    text-align: center;
}
.feature-desc {
    font-size: 15px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">👤</div>
        <div class="feature-title">Gestão de Tutores</div>
        <p class="feature-desc">Organize informações dos tutores com facilidade.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🐶</div>
        <div class="feature-title">Cadastro de Pets</div>
        <p class="feature-desc">Registre pets de forma prática e rápida.</p>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💉</div>
        <div class="feature-title">Controle de Vacinas</div>
        <p class="feature-desc">Gerencie aplicações e próximas doses.</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📖</div>
        <div class="feature-title">Histórico Completo</div>
        <p class="feature-desc">Visualize o histórico completo de cada pet.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.markdown("<p style='text-align:center; color: gray;'>Navegue pelo menu lateral para acessar as funcionalidades.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color: gray;'>Projeto acadêmico PetVac 🐾</p>", unsafe_allow_html=True)