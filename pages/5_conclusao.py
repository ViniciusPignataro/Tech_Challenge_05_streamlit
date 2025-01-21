import streamlit as st
from tabs.conclusao import conclusao_tab, referencias_tab


def main():
    st.subheader(':red[Conclusão]')

    tab1, tab2 = st.tabs(['Conclusão', 'Referências'])

    with tab1:
        conclusao_tab.show()

    with tab2:
        referencias_tab.show()
        
main()  