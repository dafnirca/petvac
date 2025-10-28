import streamlit as st

def set_css():
    st.markdown("""
        <style>
            /* Fundo principal */
            .stApp {
                background-color: #FAFAFA; /* Cinza claro */
                font-family: 'Arial', sans-serif;
                color: #2A2E5F; /* Azul escuro p textos */
            }

            /* Cabeçalhos */
            h1, h2, h3 {
                color: #2A2E5F;
                font-weight: bold;
            }

            /* Inputs e Textarea */
            .stTextInput > div > div > input,
            .stTextArea > div > div > textarea,
            .stNumberInput input,
            .stDateInput input {
                background-color: #FFFFFF; /* Fundo branco */
                border: 2px solid #A0B3A8; /* Verde */
                border-radius: 10px;
                padding: 10px;
                color: #2A2E5F; /* Texto dentro do campo */
            }

            /* Labels dos inputs */
            label {
                color: #000000 !important;
                font-weight: 600;
            }

            /* === Sidebar === */
            section[data-testid="stSidebar"] {
                background-color: #00B3AD; /* Turquesa personalizada */
                color: #2A2E5F;
            }

            /* Links da sidebar */
            section[data-testid="stSidebar"] a {
                color: #2A2E5F !important;
                font-weight: 500;
            }

            section[data-testid="stSidebar"] a:hover {
                background-color: #C1D3C1 !important;
                border-radius: 6px;
                color: #1E3A5F !important;
            }

            /* === Barra superior (Header) === */
            header[data-testid="stHeader"] {
                background-color: #2A2E5F; /* Azul escuro */
                color: white;
                transition: background-color 0.3s ease;
            }

            /* === Botões principais === */
            .stButton button {
                background-color: #D1747B; /* Rosa */
                color: white;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px 22px;
                border: none;
                transition: 0.3s;
            }

            .stButton button:hover {
                background-color: #33C1C1; /* Turquesa */
                transform: scale(1.05);
            }

            /* Caixas de formulário */
            .form-box {
                background-color: #D1747B; /* Rosa */
                color: white;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0px 2px 6px rgba(0,0,0,0.08);
                margin-bottom: 20px;
            }

            /* Divisores */
            hr {
                border: 1px solid #D1747B;
            }

        </style>
    """, unsafe_allow_html=True)