import streamlit as st
from st_pages import get_nav_from_toml

# Definição de layout geral para o aplicativo
def layout():
    # Define o nome das páginas
    nav = get_nav_from_toml("./pages/pages.toml")

    pg = st.navigation(nav)

    pg.run()

    # Instruções adicionais no sidebar
    with st.sidebar:
        st.subheader('Guia para instalação e execução do aplicativo localmente') 

        st.markdown('**1º** Crie e ative um ambiente virtual:')
        st.code('python -m venv venv')

        st.markdown('**2º** Ativação do ambiente virtual no Linux:')
        st.code('source venv/bin/activate')

        st.markdown('**2º** Ativação do ambiente virtual no Windows:')
        st.code('venv\\Scripts\\activate')

        st.markdown('**3º** Instalação das dependências:')
        st.code('pip install -r requirements.txt')

        st.markdown('**4º** Execução do aplicativo:')
        st.code('streamlit run main.py')
