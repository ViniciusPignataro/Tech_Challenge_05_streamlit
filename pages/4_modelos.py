import streamlit as st
from tabs.modelos import modelo_linear_regression, modelo_random_forest, modelo_decision_tree, modelo_svr, modelo_andamento

def main():
    st.subheader(':red[Modelos e Treinamento]', divider='red')

    tab0, tab1, tab2, tab3, tab4 = st.tabs(['Linear Regression', 'Random Forest', 'Decision Tree', 'SVR', 'Funcionamento'])

    with tab0: 
        modelo_linear_regression.show()

    with tab1:
        modelo_random_forest.show()

    with tab2:
        modelo_decision_tree.show()

    with tab3:
        modelo_svr.show()

    with tab4:
        modelo_andamento.show()

main()  