import streamlit as st

def show():
    st.write("""
        A :red[Random Forest] é uma técnica de aprendizado de máquina poderosa e versátil, utilizada para tarefas de classificação e regressão. Ela é baseada na construção de múltiplas árvores de decisão durante o treinamento e na saída da classe que é o modo das classes (classificação) ou média das previsões (regressão) das árvores individuais. \n

        Imagine que você quer prever se um cliente vai comprar um produto com base em características como idade, renda e histórico de compras. A Random Forest cria várias árvores de decisão com diferentes subconjuntos dos dados e características, e cada árvore faz uma previsão. A previsão final é determinada pela maioria das previsões das árvores (no caso de classificação) ou pela média (no caso de regressão). \n

        A Random Forest é particularmente eficaz porque reduz o risco de overfitting, que é comum em árvores de decisão individuais. Ao combinar as previsões de várias árvores, ela melhora a precisão e a robustez do modelo. Além disso, a Random Forest pode lidar com grandes conjuntos de dados e um grande número de características, tornando-a uma escolha popular para muitas aplicações práticas. \n
    """)


    st.subheader(':gray[Resultados]', divider= 'red')

    st.write("""
             Ao utilizar a :red[Random Forest] para analisar a base de dados fornecida pela :red[Passos Mágicos], obtivemos um R² de aproximadamente 0.97, o que indica uma excelente precisão dos dados de teste em relação aos dados de treino, porém com risco de overfitting, conforme indica também o gráfico abaixo:
             """)

    t1, t2, t3 = st.columns([1, 9, 1])

    with t2:
        st.image('assets/img/scatter_random_forest.png', caption='Scatter plot da Random Forest')