import streamlit as st
import pandas as pd
from backend.services import consultar_historico_pet, listar_pets, listar_tutores
from pages.style import set_css

import pandas as pd
from datetime import datetime

set_css()

st.header("📖 Histórico de Vacinas do Pet")
st.write("Consulte o histórico completo de vacinas aplicadas a um pet específico.")


# ----- CARREGAR PETS E TUTORES -----
pets_df = listar_pets()
tutores_df = listar_tutores()

if pets_df.empty or tutores_df.empty:
    st.warning("Não há pets ou tutores cadastrados.")
else:
    # Renomear colunas para evitar conflitos
    pets_df = pets_df.rename(columns={"nome": "nome_pet"})

    tutores_df = tutores_df.rename(columns={"nome": "nome_tutor"})

    # Merge pet -> tutor
    pets_df = pets_df.merge(
        tutores_df[["idTutor", "nome_tutor"]],
        on="idTutor",
        how="left"
    )

    # Criar label completo do pet
    pets_df["label"] = pets_df.apply(
        lambda r: f"{r['idPet']} - {r['nome_pet']} ({r['raca']}) — Tutor: {r['nome_tutor']}",
        axis=1
    )

    # ----- SELEÇÃO DO PET -----
    pet_escolhido = st.selectbox(
        "Selecione o Pet",
        pets_df["label"]
    )

    id_pet = int(pet_escolhido.split(" - ")[0])

    # ----- CONSULTAR HISTÓRICO -----
    if st.button("🔍 Consultar Histórico"):
        resultado = consultar_historico_pet(id_pet)

        if isinstance(resultado, str):
            st.info(resultado)
        else:
            st.success(f"Histórico de vacinas do pet {pets_df[pets_df['idPet']==id_pet]['nome_pet'].iloc[0]}:")

            st.dataframe(resultado, use_container_width=True)

            total = len(resultado)
            st.write(f"**Total de vacinas registradas:** {total}")

            # Exibir próximas doses
            if "dataProximaDose" in resultado.columns:

                # Converter para datas reais (evita erro de comparação)
                resultado["dataProximaDose"] = pd.to_datetime(
                    resultado["dataProximaDose"], errors="coerce"
                ).dt.date

                hoje = datetime.now().date()

             # Filtrar apenas doses com futura aplicação e não aplicadas
                proximas = resultado[
                    (resultado["dataProximaDose"].notna()) &
                    (resultado["dataProximaDose"] > hoje) &
                    (resultado["status"] != "aplicada")
                ]

                if not proximas.empty:
                    st.subheader("📅 Próximas doses futuras:")
                    st.dataframe(
                        proximas[["nome", "dataProximaDose"]],
                        use_container_width=True
                    )
                else:
                    st.info("Nenhuma dose futura pendente.")
            
                