import streamlit as st
from tabs.passos_magicos import sobre_tab

def main():
    # Definindo um título para a página    
    st.title('FIAP PÓS TECH - DATA ANALYTICS')
    
    # Criação de abas
    tab1, tab2, tab3 = st.tabs(['Sobre', 'Relatórios', 'Base de dados'])


    with tab1:
        sobre_tab.show()
    # with tab1:
    #     st.markdown('''
    #                 * INTRODUZIR TEXTO SOBRE A PASSOS MÁGICOS, SEPARANDO MAIS SUBHEADERS PARA MISSAO, VISÃO E VALORES * \n
    # 	            ''')

    with tab2:
        st.markdown('''
                    * INSERIR SOBRE PEDE E RELATÓRIOS *
                    ''')

    with tab3:
        st.markdown('''
                    * INSERIR SOBRE BASE DE DADOS *
                    ''')

main()  