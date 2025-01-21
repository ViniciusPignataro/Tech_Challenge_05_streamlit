import streamlit as st


def main():
    st.subheader(':red[Exploração e Insights]')

    tab1, tab2 = st.tabs(['Análise (mudar nome)', 'Power BI'])

    with tab1:
        st.subheader(':gray[Subtítulo sobre a parte da Análise]', divider='red')

        st.markdown('''
                    * SOBRE A ANÁLISE(COM GRAFICOS) * \n
                    ''')
    

    with tab2:
        st.subheader(':gray[Eventos e Insights Analisados com Power BI]', divider='red')

        st.markdown('''
                    * SOBRE INSIGHTS DENTRO DO CONTEXTO * \n
                    ''')
        

        st.subheader(':red[Insights]')

        st.markdown('''
                    :one: * SOBRE INSIGHTS EM SI (COM PRINTS) * \n
                    ''')
        
main()  