import streamlit as st
from tabs.passos_magicos import sobre_tab, relatorios_tab

def main():
    # Definindo um título para a página    
    col1, col2 = st.columns([2, 1])

    with col1: 
        st.title('FIAP PÓS TECH - DATA ANALYTICS')

    with col2:
        st.image('assets/img/logo-passos-magicos.png', use_container_width=True)

    # Criação de abas
    tab1, tab2 = st.tabs(['Sobre', 'Relatórios'])


    with tab1:
        sobre_tab.show()

    with tab2:
        relatorios_tab.show()

main()  