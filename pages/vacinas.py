import streamlit as st
import pandas as pd
from datetime import date
from backend.services import registrar_vacina, consultar_vacinas_pendentes, aplicar_dose, listar_tutores, listar_pets
from pages.style import set_css

set_css()

def tutor_label(row):
    return f"{row['idTutor']} - {row['nome']} ({row['telefone']})"

def pet_label(row):
    return f"{row['idPet']} - {row['nome_pet']} ({row['raca']}) — Tutor: {row['nome_tutor']}"

tutores_df = listar_tutores()
pets_df = listar_pets()

# ---------- REGISTRO DE VACINA ----------
st.header("💉 Registro de Vacina")

if pets_df.empty or tutores_df.empty:
    st.info("Cadastre pets e tutores antes de registrar vacinas.")
    pets_df = pd.DataFrame()
else:
    pets_df = pets_df.merge(
        tutores_df.rename(columns={"nome": "nome_tutor"})[["idTutor", "nome_tutor"]],
        on="idTutor",
        how="left"
    )

    pets_df = pets_df.rename(columns={"nome": "nome_pet"})

if not pets_df.empty:

    pet_escolhido = st.selectbox(
        "Selecione o Pet",
        pets_df.apply(pet_label, axis=1)
    )
    
    idPet = int(pet_escolhido.split(" - ")[0])
else:
    idPet = None


nome_vacina = st.text_input("Nome da Vacina")
data_aplicacao = st.date_input("Data de Aplicação", value=None)
data_proxima_dose = st.date_input("Data da Próxima Dose (opcional)", value=None)

if st.button("Registrar Vacina"):
    if idPet:
        msg = registrar_vacina(
            idPet,
            nome_vacina,
            str(data_aplicacao) if data_aplicacao else None,
            str(data_proxima_dose) if data_proxima_dose else None
        )
        st.success(msg)
    else:
        st.warning("Selecione um pet válido.")


# ------------------ PENDENTES ------------------
st.header("📋 Vacinas Pendentes")

if st.button("Consultar Vacinas Pendentes"):
    pendentes = consultar_vacinas_pendentes()
    if pendentes.empty:
        st.info("Nenhuma vacina pendente encontrada.")
    else:
        st.dataframe(pendentes, use_container_width=True)


# ------------------ APLICAR DOSE ------------------
st.header("💉 Aplicar Dose de Vacina")

pend = consultar_vacinas_pendentes()

if not pend.empty:

    pets_df = listar_pets().rename(columns={"nome": "nome_pet"})
    tutores_df = listar_tutores().rename(columns={"nome": "nome_tutor"})

    # Merge vacina -> pet
    pend = pend.merge(
        pets_df[["idPet", "nome_pet", "raca", "idTutor"]],
        on="idPet",
        how="left"
    )

    # Merge pet -> tutor
    pend = pend.merge(
        tutores_df[["idTutor", "nome_tutor"]],
        on="idTutor",
        how="left"
    )

    pend["label"] = pend.apply(
        lambda r: (
            f"{r['idVacina']} - {r['nome_pet']} "
            f"(Tutor: {r['nome_tutor']}) — Vacina: {r['nome']}"
        ),
        axis=1
    )

    vacina_sel = st.selectbox("Selecione uma vacina pendente", pend["label"])
    idVacina = int(vacina_sel.split(" - ")[0])

    dataAplicacao = st.date_input("Data da aplicação")
    dataProximaDose = st.date_input("Próxima dose (opcional)", value=None)

    if st.button("Aplicar Dose"):
        prox = str(dataProximaDose) if dataProximaDose else None
        msg = aplicar_dose(idVacina, dataAplicacao, prox)
        st.success(msg)

else:
    st.info("Nenhuma vacina pendente para aplicar.")