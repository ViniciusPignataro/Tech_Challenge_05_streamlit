import streamlit as st
from tabs.passos_magicos import sobre_tab, relatorios_tab, base_dados_tab

def main():
    # Definindo um título para a página    
    st.title('FIAP PÓS TECH - DATA ANALYTICS')
    
    # Criação de abas
    tab1, tab2, tab3 = st.tabs(['Sobre', 'Relatórios', 'Base de dados'])


    with tab1:
        sobre_tab.show()

    with tab2:
        relatorios_tab.show()

    with tab3:
        base_dados_tab.show()

main()  