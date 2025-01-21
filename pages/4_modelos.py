import streamlit as st
from tabs.modelos import modelo1_tab, modelo2_tab, modelo3_tab, modelo4_tab


def main():
    st.subheader(':red[Modelos (INSERIR SOBRE OS MODELOS UTILIZADOS EM TABS SEPARADAS)]', divider='red')

    tab0, tab1, tab2, tab3 = st.tabs(['Modelo1', 'Modelo2', 'Modelo3', 'Modelo4'])

    with tab0: 
        modelo1_tab.show()

    with tab1:
        modelo2_tab.show()

    with tab2:
        modelo3_tab.show()

    with tab3:
        modelo4_tab.show()



main()  