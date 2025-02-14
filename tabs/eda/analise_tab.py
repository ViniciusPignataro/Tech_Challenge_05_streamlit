import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():
    st.subheader(':gray[Entendendo melhor os indicadores]', divider='red')

    st.markdown('''
                Para compreender melhor a relação entre os indicadores médios e os INDEs dos alunos, realizamos uma análise exploratória dos dados. Foram gerados gráficos de dispersão, histogramas de distribuição, boxplots e uma matriz de correlação para examinar padrões, outliers e possíveis associações entre as variáveis. Essa análise inicial nos permite levantar hipóteses sobre quais fatores podem influenciar a evolução dos alunos e, assim, direcionar a escolha do modelo de machine learning mais adequado para prever os INDEs.\n

                A escolha do INDE como variável-alvo se justifica pelo seu papel central na definição da classificação final dos alunos dentro do programa. O INDE sintetiza a performance do estudante ao longo do tempo, funcionando como um indicador-chave para determinar sua evolução e progressão dentro das categorias, incluindo a transição de nível de classificação(pedra). Dessa forma, ao modelar o impacto dos indicadores médios sobre o INDE, conseguimos entender quais fatores mais influenciam essa progressão e como otimizar o desempenho dos alunos por meio de intervenções direcionadas. \n
                ''')
    
    st.image("assets/img/distribuicao_inde.png", caption="Distribuição INDE.")

    st.markdown('''
                O histograma da variável INDE revela um padrão de distribuição característico, onde os valores começam em 0, crescem exponencialmente até atingir um pico entre 7 e 8, e depois começam a diminuir gradualmente até 10. Essa distribuição indica que a maioria dos alunos possui INDE entre 6 e 10, com uma concentração significativa em torno de 7,5, sugerindo que a maioria dos estudantes apresenta um desempenho intermediário a avançado. Esse comportamento pode indicar uma menor presença de alunos com notas muito baixas, além de reforçar a importância de analisar quais fatores influenciam a progressão dentro desse intervalo dominante. Compreender essa distribuição é essencial para identificar padrões de desempenho e direcionar estratégias que auxiliem na evolução dos alunos com base nos indicadores médios. \n

                Da mesma forma, podemos separar os três anos presentes no banco de dados para verificar a consistência do padrão observado. A distribuição do INDE se mantém semelhante em todos os anos analisados, com a maioria dos alunos concentrada entre 6 e 10 e um pico em torno de 7 a 8. No entanto, observamos uma leve queda nas notas mais altas ao longo dos anos: no primeiro ano, há mais registros de alunos com INDE acima de 9, no segundo essa quantidade diminui e, no último ano, praticamente não há alunos nessa faixa. Essa tendência também é refletida no boxplot, que mostra uma leve redução na dispersão dos valores no último ano. Nos dois primeiros anos, os valores variam aproximadamente de 6 a 8, enquanto no último ano o intervalo se estreita, começando em 6,4 e terminando em 7,8. Essa mudança pode indicar uma menor ocorrência de desempenhos excepcionais nos anos mais recentes, sugerindo a necessidade de investigar fatores que possam estar influenciando essa variação. \n
                ''')
    
    st.image("assets/img/distribuicao_boxplot_eda.png", caption="Distribuição e Boxplot INDE.")

    st.divider()

    st.markdown('''
                Outra ferramenta que nos auxilia no levantamento de hipóteses é o **gráfico de dispersão**, que permite visualizar a relação entre cada **indicador** e o **INDE**. Como esperado, **nenhum dos indicadores apresenta uma correspondência exata** com o INDE, uma vez que ele é composto a partir de todos eles. No entanto, ao analisar os padrões, percebemos que alguns indicadores exibem uma **tendência mais clara de crescimento junto com o INDE**, como o **IDA, o IEG e o IPV**, que começam com valores mais baixos e aumentam conforme o INDE se eleva.  

                Essa observação sugere que esses indicadores podem ter um impacto mais direto na definição do INDE, o que nos leva a considerar a hipótese de que sua influência pode ser maior em comparação com os demais. Esse tipo de análise é fundamental para entender como os diferentes fatores contribuem para a evolução dos alunos, fornecendo insights iniciais sobre quais variáveis podem ser mais relevantes na modelagem preditiva.
                ''')

    st.image("assets/img/dispersao_indicadores_inde.png", caption="Dispersão dos indicadores(IAA, IEG, IPS, IDA, IPP, IPV, IAN).")

    st.markdown('''
                Outra ferramenta essencial na análise exploratória é a **matriz de correlação**, que nos permite visualizar a relação entre todas as variáveis do conjunto de dados. Diferente do gráfico de dispersão, que mostra individualmente a relação entre duas variáveis, a matriz de correlação nos oferece uma visão global das associações, facilitando a identificação de padrões e possíveis dependências entre os indicadores.  

                Ao analisar a matriz, observamos novamente que o **INDE apresenta uma correlação mais forte com os indicadores IDA e IEG**, reforçando a tendência já percebida nos gráficos anteriores. Esse resultado sugere que esses fatores podem desempenhar um papel mais relevante na definição do INDE, o que nos leva a considerar a hipótese de que possuem maior peso na composição final desse indicador. Essa análise é fundamental para a construção de modelos preditivos, pois nos ajuda a direcionar quais variáveis podem ter maior influência na evolução dos alunos e, consequentemente, quais aspectos podem ser priorizados para otimizar seu desempenho.
                ''')
    
    st.image("assets/img/matriz_correlacao.png", caption="Matriz de correçação INDE vs Indicadores.")

    st.markdown('''
                Com base na análise exploratória, identificamos que algumas variáveis se destacam na relação com o INDE, o que pode servir como um ponto de partida para compreender sua composição a partir de um modelo preditivo. O treinamento do modelo permitirá não apenas confirmar a influência desses indicadores na definição do INDE, mas também determinar seus coeficientes de impacto com maior precisão. Além disso, essa abordagem pode auxiliar na identificação de valores médios compatíveis para cada indicador, permitindo, no futuro, a formulação de sugestões personalizadas para que os alunos tenham um direcionamento mais claro sobre quais aspectos precisam melhorar para otimizar seu desempenho no programa.
                ''')