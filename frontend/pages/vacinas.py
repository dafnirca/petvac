import streamlit as st
from datetime import date
from backend.services import registrar_vacina, consultar_vacinas_pendentes
from frontend.pages.style import set_css

set_css()

st.header("💉 Registro de Vacina")

idPet = st.number_input("ID do Pet", min_value=1, step=1)
nome_vacina = st.text_input("Nome da Vacina")
data_aplicacao = st.date_input("Data de Aplicação", value=date.today())
data_proxima_dose = st.date_input("Data da Próxima Dose (opcional)")

if st.button("Registrar Vacina"):
    if not nome_vacina.strip():
        st.warning("Por favor, insira o nome da vacina.")
    else:
        msg = registrar_vacina(
            idPet,
            nome_vacina,
            str(data_aplicacao),
            str(data_proxima_dose) if data_proxima_dose else None
        )
        st.success(msg)


st.header("📋 Vacinas Pendentes")

if st.button("Consultar Vacinas Pendentes"):
    pendentes = consultar_vacinas_pendentes()
    if pendentes.empty:
        st.info("Nenhuma vacina pendente encontrada.")
    else:
        st.dataframe(pendentes, use_container_width=True)

