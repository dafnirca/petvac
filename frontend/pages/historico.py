import streamlit as st
from backend.services import consultar_historico_pet
from frontend.pages.style import set_css

set_css()

st.header("📖 Histórico de Vacinas do Pet")

st.write("Consulte o histórico completo de vacinas aplicadas a um pet específico.")

id_pet = st.number_input("Informe o ID do Pet", min_value=1, step=1)

# botão p/ buscar o histórico
if st.button("🔍 Consultar Histórico"):
    if not id_pet:
        st.warning("Por favor, informe o ID do pet.")
    else:
        resultado = consultar_historico_pet(id_pet)

        if isinstance(resultado, str):
            st.info(resultado)
        else:
            st.success(f"Histórico de vacinas do pet ID {id_pet}:")
            st.dataframe(resultado, use_container_width=True)

            total = len(resultado)
            st.write(f"**Total de vacinas registradas:** {total}")

            if "dataProximaDose" in resultado.columns:
                pendentes = resultado[resultado["dataProximaDose"].notna()]
                if not pendentes.empty:
                    st.subheader("📅 Próximas doses registradas:")
                    st.dataframe(pendentes[["nome", "dataProximaDose"]], use_container_width=True)
