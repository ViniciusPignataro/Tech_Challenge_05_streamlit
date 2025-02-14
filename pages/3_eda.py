import streamlit as st
from tabs.eda import analise_tab, insights_tab


def main():
    st.subheader(':red[Exploração e Insights]')

    tab1, tab2 = st.tabs(['Análise Exploratória dos Dados', 'Power BI'])

    with tab1:
       analise_tab.show()

    with tab2:
        insights_tab.show()

main()  