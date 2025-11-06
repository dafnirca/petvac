import streamlit as st
from datetime import date
from backend.services import registrar_vacina, consultar_vacinas_pendentes, consultar_historico_pet
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


st.header("📖 Histórico de Vacinas do Pet")

id_pet_historico = st.number_input("Informe o ID do Pet para consultar o histórico", min_value=1, step=1)

if st.button("Consultar Histórico"):
    historico = consultar_historico_pet(id_pet_historico)
    if isinstance(historico, str):
        st.info(historico)
    else:
        st.dataframe(historico, use_container_width=True)
