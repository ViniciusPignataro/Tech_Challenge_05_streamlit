import streamlit as st

def show():
    st.write("""
        A :red[Regressão Linear] é uma técnica estatística essencial que ajuda a entender a relação entre uma variável dependente e uma ou mais variáveis independentes. É amplamente utilizada em áreas como economia, ciências sociais, biologia e engenharia para prever valores e compreender as relações entre variáveis. \n

        Imagine que você quer prever o preço de uma casa com base em características como tamanho, localização e número de quartos. A regressão linear analisa dados históricos dessas características e seus respectivos preços para encontrar uma linha reta (ou plano, no caso de múltiplas variáveis) que melhor se ajusta aos dados. Essa linha é então usada para fazer previsões sobre o preço de novas casas com base em suas características. \n

        Diferente de modelos mais complexos, a regressão linear é relativamente simples de entender e implementar. Ela assume que a relação entre as variáveis é linear, ou seja, uma mudança na variável independente resulta em uma mudança proporcional na variável dependente. Essa simplicidade torna a regressão linear uma ferramenta poderosa e fácil de usar para muitas aplicações práticas, sendo especialmente eficaz quando a relação entre as variáveis é aproximadamente linear e os dados não apresentam padrões complexos ou não-lineares.
    """)

    st.subheader(':gray[Resultados]', divider= 'red')

    st.write("""
             Ao utilizar a :red[Regressão Linear] para analisar a base de dados fornecida pela :red[Passos Mágicos], obtivemos um R² de aproximadamente 0.96, o que indica uma boa precisão dos dados de teste em relação aos dados de treino, conforme indica também o gráfico abaixo:
             """)

    t1, t2, t3 = st.columns([1, 9, 1])

    with t2:
        st.image('assets/img/scatter_linear_regression.png', caption='Scatter plot da Regressão Linear')