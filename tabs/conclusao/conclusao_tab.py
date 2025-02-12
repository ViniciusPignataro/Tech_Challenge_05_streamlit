import streamlit as st

def show():
    st.subheader(':gray[Conclusão]', divider='red')

    st.markdown('''
                Este projeto propôs a criação de um modelo de machine learning para identificar alunos em risco, utilizando um conjunto de dados composto por notas acadêmicas e indicadores de desempenho, como o Índice de Desenvolvimento Acadêmico (IDA) e o Indicador de Autoavaliação (IAA). O principal objetivo foi desenvolver uma ferramenta que permita identificar de forma proativa os alunos mais propensos a enfrentar dificuldades acadêmicas, especialmente aqueles classificados na Pedra Quartzo, que representa o nível mais crítico de desempenho.
                ''')

    st.subheader(':gray[Benefícios do Modelo Preditivo]', divider='red')

    st.markdown('''
                :one: :red[**Ação Antecipada:**] Prever o risco de baixo desempenho permite que a escola intervenha antes que o aluno enfrente dificuldades graves. Isso possibilita ações mais eficazes e precisas. \n
                :two: :red[**Apoio Personalizado:**] Com as previsões do modelo, é possível oferecer um suporte ajustado às necessidades de cada aluno, garantindo uma abordagem mais direcionada e eficiente. \n
                :three: :red[**Uso Eficiente de Recursos:**] Identificando os alunos que realmente precisam de ajuda, o modelo permite que a Passos Mágicos utilize seus recursos de forma mais estratégica, focando nos estudantes em risco e evitando a distribuição indiscriminada de recursos. \n
                :four: :red[**Acompanhamento Contínuo:**] O modelo pode ser usado para monitorar o desempenho dos alunos ao longo do tempo. Com novos dados, as previsões são atualizadas, ajustando o suporte conforme necessário. Esse acompanhamento contínuo permite que a instituição avalie a eficácia das intervenções e ajuste suas estratégias em tempo real. \n
                ''')