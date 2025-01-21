import streamlit as st


def main():
    st.subheader(':red[Conclusão]')

    tab1, tab2 = st.tabs(['Conclusão', 'Referências'])

    with tab1:
        st.subheader(':gray[INSERIR SUBTITULO DE CONCLUSAO]', divider='red')

        st.markdown('''
                    * INSERIR SOBRE CONCLUSÃO * \n
                    ''')
        
        st.subheader(':gray[Melhorias futuras]', divider='red')

        st.markdown('''
                    * INSERIR BALELA SOBRE MELHORIA QUE NUNCA VAI ACONTECER * \n
                    ''')

    with tab2:
        st.subheader(':gray[Referências]', divider='red')

        st.markdown('''
                    :one: * INSERIR REFERÊNCIAS * \n
                    ''')

main()  