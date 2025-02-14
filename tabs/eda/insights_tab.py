import streamlit as st

def show():
    st.subheader(':gray[Eventos e Insights Analisados com Power BI]', divider='red')

    st.markdown('''
                Para complementar nossa análise exploratória, utilizamos o Power BI para visualizar os dados de forma mais interativa e dinâmica. A ferramenta permitiu uma abordagem mais detalhada na distribuição dos alunos ao longo dos anos, especialmente em relação às Pedras, que representam a classificação baseada no INDE. Com essa análise, buscamos entender como a evolução do INDE influencia a categorização dos alunos e se há variações na média necessária para cada Pedra ao longo dos anos.

                Um dos principais gráficos construídos foi um gráfico de barras que agrupa as quatro Pedras em três barras correspondentes a cada ano analisado. Esse gráfico nos permitiu observar que, apesar de pequenas variações anuais, a média do INDE para cada Pedra se mantém relativamente estável, sempre acompanhando sua respectiva categoria. No entanto, percebemos que em alguns anos a média necessária para um aluno atingir determinada Pedra foi levemente maior ou menor, indicando que o critério de progressão pode ter tido pequenas oscilações ao longo do tempo. Essa informação é relevante para entender como os alunos foram classificados em diferentes períodos e pode auxiliar na definição de limites mais consistentes para futuras análises.\n
                ''')
    st.image(f"assets/img/powerbi_media_pedra_ano.png", caption=f"Distribuição INDE.")
    st.markdown('''
                Outro gráfico importante criado no **Power BI** foi a **contagem de alunos por Pedra em cada ano**, permitindo uma visão mais clara da distribuição dos estudantes ao longo do tempo. Esse gráfico reforça a tendência já observada na análise exploratória, destacando que a **maior parte dos alunos pertence à Pedra Ametista**, correspondente a um **INDE médio de 7,5**, que se mostrou predominante nos anos analisados. Essa distribuição sugere que a maioria dos estudantes se encontra em um nível intermediário dentro do programa.  

                Por outro lado, a **Pedra Topázio**, que representa a classificação mais alta, possui a menor quantidade de alunos, o que pode indicar um espaço significativo para evolução. Essa menor presença de estudantes no nível mais alto sugere que há desafios no caminho para atingir esse patamar, seja por dificuldades individuais dos alunos ou pela necessidade de intervenções mais direcionadas para impulsionar esse avanço. Essa informação pode ser útil para futuras análises, auxiliando na criação de estratégias para melhorar a progressão dos alunos ao longo do tempo.\n
                ''')
    st.image(f"assets/img/powerbi_contagem_pedra_ano.png", caption=f"Distribuição INDE.")
    st.divider
    st.markdown('''
                Para compreender melhor as variações anuais no INDE e na distribuição das Pedras, analisamos os três gráficos comparativos a seguir, dos indicadores ao longo dos anos, agrupados conforme suas categorias. \n \n
                O primeiro conjunto de indicadores analisados foram os de desempenho acadêmico (IDA, IEG e IAN). Observamos que, em 2020, esses indicadores apresentavam valores médios de 6,2, 7,8 e 7,3, respectivamente. No entanto, todos sofreram uma queda em 2021, com apenas IDA e IEG se recuperando para os valores iniciais em 2022, enquanto o IAN continuou caindo. Essa tendência sugere que algo impactou negativamente esse indicador, tornando-o um ponto de atenção, pois sua recuperação não ocorreu como nos demais. Esse declínio contínuo pode indicar a necessidade de investigações mais aprofundadas para entender os fatores que influenciaram essa queda e possíveis ações para revertê-la.\n
                ''')
    st.image(f"assets/img/powerbi_desempenhos_academicos.png", caption=f"Distribuição INDE.")
    st.markdown('''
                O segundo gráfico analisou os indicadores psicopedagógicos (IPP e IPV). O IPV apresentou uma queda leve, indo de 7,5 em 2020 para 7,25 em 2022, o que, apesar de ser uma redução, não representa uma mudança brusca. Já o IPP teve um comportamento mais instável, inicialmente crescendo de 7,33 em 2020 para 7,6 em 2021, mas caindo abruptamente para 6,3 em 2022. Essa variação mais acentuada no IPP pode indicar um fator específico que impactou negativamente esse indicador no último ano analisado, tornando-se também um ponto crítico a ser investigado.\n
                ''')
    st.image(f"assets/img/powerbi_desempenhos_psicopedagogicos.png", caption=f"Distribuição INDE.")
    st.markdown('''
                Por fim, o terceiro gráfico apresentou os indicadores psicossociais (IAA e IPS). Diferente dos outros indicadores, esses não sofreram variações tão significativas. O IAA teve uma leve queda, enquanto o IPS apresentou um pequeno crescimento, mas ambos permaneceram relativamente estáveis ao longo dos três anos. Isso sugere que, embora ações mais impactantes possam ser necessárias para elevar esses indicadores, eles não são prioritários no momento, já que não demonstram uma tendência negativa como os demais.\n
                ''')
    st.image(f"assets/img/powerbi_desempenhos_psicossociais.png", caption=f"Distribuição INDE.")
    st.markdown('''
                Com base nessas análises, fica evidente a importância de focarmos nos indicadores que apresentaram quedas mais expressivas, como IAN e IPP, pois a deterioração desses aspectos pode estar influenciando diretamente o desempenho geral dos alunos. Como o INDE é composto a partir desses indicadores, ações voltadas para melhorar os pontos em queda não apenas beneficiariam os estudantes individualmente, mas também reforçariam a metodologia de avaliação, garantindo que as melhorias sejam refletidas tanto nos resultados dos alunos quanto no acompanhamento da evolução do programa.\n
                ''')

    st.subheader(':red[Insights]')

    st.markdown('''
                :one: **Análise mais detalhada dos indicadores que caíram (IAN e IPP)** – Os indicadores IAN (acadêmico) e IPP (psicopedagógico) apresentaram quedas mais significativas ao longo do tempo, o que levanta um alerta para entender o que pode ter impactado negativamente esses aspectos. Uma análise mais aprofundada pode revelar fatores como mudanças na metodologia, dificuldades dos alunos em relação a determinados conteúdos ou até mesmo questões externas, permitindo a implementação de estratégias para reverter essa queda. \n
                ''')
    st.markdown('''
                :two: **Oportunidade de aumentar o número de alunos na Pedra Topázio** – A distribuição das Pedras revelou que a maioria dos alunos está na Pedra Ametista, enquanto a Pedra Topázio, que representa o nível mais alto, possui a menor quantidade de estudantes. Isso indica que há potencial para evolução, e estratégias podem ser traçadas para ajudar alunos da Pedra Ametista a avançarem. O foco pode estar em intervenções direcionadas nos indicadores que apresentam mais correlação com o INDE, garantindo que os alunos tenham suporte para subir de nível. \n
                ''')
    st.markdown('''
                :three: **Oscilações na média do INDE para cada Pedra podem impactar a progressão dos alunos** – A análise mostrou que a média do INDE para cada Pedra se manteve relativamente estável, mas com pequenas variações ao longo dos anos. Essas oscilações podem indicar que, em alguns momentos, os critérios para alcançar determinada Pedra foram um pouco mais rígidos ou mais flexíveis. Isso pode ser um fator a ser analisado no futuro para garantir maior consistência nos limites de progressão, ajudando a definir com mais clareza os objetivos que os alunos precisam atingir. \n
                ''')
    