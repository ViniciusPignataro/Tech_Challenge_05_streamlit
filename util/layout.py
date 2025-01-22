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

        st.markdown('#')

        _, col, _ = st.columns([1, 8, 1])

        with col:
            st.image('assets/img/logo-fiap.png', width=150, use_container_width=True)
            st.image('assets/img/logo-postech.png', width=200, use_container_width=True)

        st.divider()

        st.text(
            'Vinicius Mathias Lacrimanti Pignataro \n RM 354421',
            help='LinkedIn: https://www.linkedin.com/in/vinicius-pignataro/'
        )

        st.text(
            'Gabriel Krieguer Zarichen \n RM 354774',
            help='LinkedIn: https://www.linkedin.com/in/gabriel-zarichen/'
        )

        st.text(
            'Georgia Oliveira Paixão Duarte \n RM 354529',
            help='LinkedIn: https://www.linkedin.com/in/georgia-oliveira-paix%C3%A3o-duarte-61133729/'
        )

        st.text(
            'Mauricio Alexandre de Souza Júnior \n RM 355078',
            help='LinkedIn: https://www.linkedin.com/in/mauricio-a-souza-junior-56a68728a/'
        )

        st.text(
            'Renan da Silva Leão \n RM 355101',
            help='LinkedIn: https://www.linkedin.com/in/renanleao7/'
        )

        st.text(
            'Turma: 4DTAT'
        )

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
