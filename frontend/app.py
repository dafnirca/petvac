import streamlit as st
from backend.services import (
    cadastrar_tutor, atualizar_tutor,
    cadastrar_pet, atualizar_pet, listar_pets,
    registrar_vacina, consultar_vacinas_pendentes, consultar_historico_pet
)
import pandas as pd

st.set_page_config(page_title="PetVac", page_icon="🐾", layout="wide")
st.title("🐾 PetVac – Sistema de Cadastro e Controle de Vacinas")