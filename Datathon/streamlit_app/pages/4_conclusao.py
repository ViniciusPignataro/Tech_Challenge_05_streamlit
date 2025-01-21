import streamlit as st


def main():
    st.subheader(':red[Conclusão]')

    tab1, tab2 = st.tabs(['Conclusão', 'Referências'])

    with tab1:
        st.subheader(':gray[Resultados e Eficiência do Prophet na Previsão]', divider='red')

        st.markdown('''
                    Dos resultados obtidos, observamos um WMAPE de aproximadamente 7% ao analisarmos os últimos 10 anos, havendo variação conforme aumento ou diminuição do tempo analisado no modelo, o que indica que o mesmo está apresentando uma precisão de aproximadamente 93% nas previsões realizadas. Esse valor é considerado satisfatório, pois está relativamente baixo, sugerindo que o modelo é eficaz em capturar a maior parte da variabilidade nos dados e em prever com precisão o preço do petróleo. \n 

                    Em suma, os resultados obtidos demonstram a robustez e a precisão do Prophet na tarefa de prever o preço do petróleo, considerando as características dos dados temporais e sazonais.
                    ''')
        
        st.subheader(':gray[Melhorias futuras]', divider='red')

        st.markdown('''
                    Apesar de o modelo Prophet ter apresentado resultados satisfatórios, ainda há espaço para melhorias e otimizações futuras. Algumas sugestões de aprimoramento incluem: \n

                    :one: **Ajuste de Hiperparâmetros**: O Prophet possui diversos hiperparâmetros que podem ser ajustados para melhorar a precisão das previsões. Realizar uma busca sistemática de hiperparâmetros pode ajudar a encontrar a combinação ideal para o conjunto de dados analisado. \n
                    ''')

    with tab2:
        st.subheader(':gray[Referências]', divider='red')

        st.markdown('''
                    :one: https://www.ipea.gov.br/ \n
                    :two: https://www.petroleoenergia.com.br/cotacao-de-petroleo-o-que-e-brent-e-wti/ \n
                    :three: https://www.petroleoenergia.com.br/exploracao-de-petroleo-em-aguas-profundas-desafios-e-oportunidades/ \n
                    :four: https://www.cnnbrasil.com.br/economia/mercado/guerra-petroleo-alimentos-e-juros-relembre-as-principais-crises-de-2022/ \n
                    ''')

main()  