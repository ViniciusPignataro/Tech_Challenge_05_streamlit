import streamlit as st

def show():
    st.write("""
        A :red[Support Vector Regression (SVR)] é uma técnica de aprendizado de máquina baseada em Support Vector Machines (SVM), utilizada para tarefas de regressão. Ela busca encontrar uma função que tenha no máximo uma determinada margem de erro para todos os pontos de dados, ao mesmo tempo que é o mais plana possível. \n

        Imagine que você quer prever o preço de uma casa com base em características como tamanho, localização e número de quartos. O SVR analisa os dados históricos dessas características e seus respectivos preços para encontrar uma função que melhor se ajusta aos dados, mantendo uma margem de erro mínima. \n

        O SVR é particularmente eficaz em situações onde os dados apresentam padrões complexos e não-lineares. Ele utiliza um conceito chamado de kernel trick para transformar os dados em um espaço de alta dimensão, onde uma função linear pode ser ajustada para capturar as relações não-lineares nos dados originais. \n
    """)

    st.subheader(':gray[Resultados]', divider= 'red')

    st.write("""
             Ao utilizar o :red[SVR] para analisar a base de dados fornecida pela :red[Passos Mágicos], obtivemos um R² de aproximadamente 0.99, o que indica uma boa precisão dos dados de teste em relação aos dados de treino, porém com alta possibilidade de overfitting, conforme indica também o gráfico abaixo:
             """)

    t1, t2, t3 = st.columns([1, 9, 1])

    with t2:
        st.image('assets/img/scatter_svr.png', caption='Scatter plot do SVR')