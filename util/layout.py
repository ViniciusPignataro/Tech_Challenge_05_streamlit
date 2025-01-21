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

        st.image('assets/img/logo-fiap.png')
        st.image('assets/img/logo-postech.png')

        st.divider()

        st.text(
            'Vinicius Mathias Lacrimanti Pignataro',
            help='LinkedIn: https://www.linkedin.com/in/vinicius-pignataro/'
        )
        st.text('RM 354421')

        st.text(
            'Gabriel Krieguer Zarichen'
        )
        st.text('')

        st.text(
            'Georgia Oliveira Paixão Duarte'
        )
        st.text('')

        st.text(
            'Mauricio Alexandre de Souza Júnior'
        )
        st.text('')

        st.text(
            'Renan da Silva Leão'
        )
        st.text('')

        st.divider()

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
