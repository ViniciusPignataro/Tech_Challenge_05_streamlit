import streamlit as st

def show():
    st.write("""
        A :red[Árvore de Decisão] é uma técnica de aprendizado de máquina amplamente utilizada para tarefas de classificação e regressão. Ela funciona dividindo os dados em subconjuntos com base em uma série de testes de decisão, resultando em uma estrutura de árvore onde cada nó representa uma característica dos dados e cada ramo representa um resultado possível. \n

        Imagine que você quer prever se um cliente vai comprar um produto com base em características como idade, renda e histórico de compras. Uma árvore de decisão analisa os dados históricos e cria uma série de perguntas (nós) que dividem os dados em grupos menores (ramos), até chegar a uma decisão final (folhas). Cada caminho da raiz até uma folha representa uma regra de decisão que pode ser usada para fazer previsões sobre novos dados. \n

        As árvores de decisão são fáceis de entender e interpretar, pois a lógica de decisão pode ser visualizada como um diagrama de árvore. Elas são capazes de lidar com dados categóricos e numéricos e podem capturar interações complexas entre características. No entanto, as árvores de decisão individuais podem ser propensas ao overfitting, especialmente com conjuntos de dados pequenos ou ruidosos. \n
    """)

    st.subheader(':gray[Resultados]', divider= 'red')

    st.write("""
             Ao utilizar a :red[Árvore de Decisão] para analisar a base de dados fornecida pela :red[Passos Mágicos], obtivemos um R² de aproximadamente 0.90, o que indica uma boa precisão dos dados de teste em relação aos dados de treino, conforme indica também o gráfico abaixo:
             """)

    t1, t2, t3 = st.columns([1, 9, 1])

    with t2:
        st.image('assets/img/scatter_decision_tree.png', caption='Scatter plot da Árvore de Decisão')