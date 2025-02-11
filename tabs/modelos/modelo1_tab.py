import streamlit as st
import modelo_sugestao

explicacao_indicadores = {
    "IAN": "O (IAN) avalia se você está na fase de ensino correspondente à sua idade, de acordo com as diretrizes do Ministério da Educação. Para melhorar, acompanhe seu progresso e, se perceber que está fora do nível adequado, converse com seus professores para ajustar sua trajetória escolar.",
    "IDA": "O (IDA) mede sua proficiência por meio de avaliações padronizadas, com notas de 0 a 10, tanto nas provas do Programa de Aceleração do Conhecimento quanto na média das disciplinas no ensino superior. Para melhorar, revise os conteúdos com frequência, pratique exercícios e procure ajuda para superar dificuldades específicas.",
    "IEG": "O (IEG) registra seu comprometimento, seja pela entrega das atividades solicitadas (para alunos das Fases 0 a 7) ou pela participação em ações de voluntariado (para estudantes universitários). Para melhorar, tente manter uma rotina organizada, cumpra prazos e se envolva mais em projetos e atividades extracurriculares.",
    "IAA": "O (IAA) reflete sua percepção sobre seu próprio desempenho, suas relações interpessoais e sua visão sobre a instituição. Para melhorar, reflita sobre seus pontos fortes e áreas que precisam de desenvolvimento, busque feedback e esteja aberto a mudanças positivas.",
    "IPS": "O (IPS) é o resultado da avaliação da equipe de psicologia, considerando aspectos familiares, emocionais, comportamentais e de socialização. Para melhorar, trabalhe no desenvolvimento socioemocional, esteja aberto a apoio psicológico quando necessário e busque fortalecer suas habilidades de convivência.",
    "IPP": "O (IPP) avalia seu desenvolvimento cognitivo, raciocínio lógico e aspectos comportamentais e emocionais com base na observação de professores, pedagogos e psicopedagogos. Para melhorar, exercite o pensamento crítico, pratique a resolução de problemas e busque atividades que ajudem no equilíbrio emocional.",
    "IPV": "O (IPV) mede seu desenvolvimento nas aptidões necessárias para usar a educação como ferramenta de transformação pessoal. Para melhorar, confie mais em si mesmo, tenha iniciativa e identifique as habilidades que podem te ajudar a alcançar mudanças significativas na sua vida acadêmica e pessoal."
}


def obter_sugestoes(data, quantidade):
    """
    Retorna as 'quantidade' melhores sugestões (com potencial > 0)
    ordenadas de forma decrescente pelo valor de 'potencial'.
    """
    # Acessa a lista de sugestões
    sugestoes = data.get("sugestoes", [])
    
    # Filtra as sugestões com potencial maior que 0
    sugestoes_validas = [s for s in sugestoes if s.get("potencial", 0) > 0]
    
    # Ordena as sugestões do maior para o menor potencial
    sugestoes_ordenadas = sorted(sugestoes_validas, key=lambda s: s.get("potencial", 0), reverse=True)
    
    # Retorna a quantidade de dicionários solicitada
    return sugestoes_ordenadas[:quantidade]

def show():
    col1, col2 = st.columns([2,4])
    with col1:
        col1_1, col1_2 = st.columns(2)
        with col1_1:
            help = 'Insira um nome para buscar um aluno e o modelo realizar as sugestões.'
            nome_aluno = st.text_input("Buscar aluno:", value="ALUNO-1", type="default", on_change=None, args=None,help=help, kwargs=None, placeholder="Ex: ALUNO-1", disabled=False, label_visibility="visible")
        with col1_2:
            help = 'Insira o número de indicadores que deseja que o sistema sugira. (Exemplo: 1 irá trazer o principal indicador em que o aluno pode melhorar seu INDE)'
            qtd_indicadores = st.number_input("Quantidade indicadores:", value=3, help=help, kwargs=None, disabled=False, label_visibility="visible")
        st.divider()
        st.subheader('Informações gerais')
        resultados = modelo_sugestao.modelo_sugestao(nome_aluno=nome_aluno, qtd_indicadores=int(qtd_indicadores))
        col1_3, col1_4 = st.columns(2)
        match resultados['pedra']:
            case 'Quartzo': cor_pedra = 'grey'
            case 'Ágata': cor_pedra = 'rainbow'
            case 'Ametista': cor_pedra = 'violet'
            case 'Topázio': cor_pedra = 'orange'
        match resultados['proxima_pedra']:
            case 'Quartzo': cor_prox_pedra = 'grey'
            case 'Ágata': cor_prox_pedra = 'rainbow'
            case 'Ametista': cor_prox_pedra = 'violet'
            case 'Topázio': cor_prox_pedra = 'orange'
            case _: cor_prox_pedra = cor_pedra
        with col1_3:
            st.write(f":mortar_board:  Nome:  :red[{resultados['nome']}]")
            st.write(f":memo:  INDE Atual: :red[{round(resultados['inde'],3)}]")
            st.write(f":spiral_calendar_pad:  Ano referência: :red[{resultados['ano']}]")
            st.write(f":gem:  Pedra atual: :{cor_pedra}[{resultados['pedra']}]")
            st.write(f"	:dart:  Próxima pedra: :{cor_prox_pedra}[{resultados['proxima_pedra']}]")
        with col1_4:
            st.markdown("**:blue[Indicadores:]**")
            st.markdown(f"""
                <div style="display: flex; justify-content: space-around;">
                    <span>IAA: {round(resultados['indicadores']['IAA'],2)}</span>
                    <span></span>
                    <span>IEG: {round(resultados['indicadores']['IEG'],2)}</span>
                </div>
            """, unsafe_allow_html=True)
            st.markdown(f"""
                <div style="display: flex; justify-content: space-around;">
                    <span>IPS: {round(resultados['indicadores']['IPS'],2)}</span>
                    <span></span>
                    <span>IDA: {round(resultados['indicadores']['IDA'],2)}</span>
                </div>
            """, unsafe_allow_html=True)
            st.markdown(f"""
                <div style="display: flex; justify-content: space-around;">
                    <span>IPP: {round(resultados['indicadores']['IPP'],2)}</span>
                    <span></span>
                    <span>IPV: {round(resultados['indicadores']['IPV'],2)}</span>
                </div>
            """, unsafe_allow_html=True)
            st.markdown(f"IAN: {round(resultados['indicadores']['IAN'],2)}")
    
    with col2:
        
        match resultados['proxima_pedra']:
            case 'Quartzo': img_proxima_pedra = 'quartz'
            case 'Ágata': img_proxima_pedra = 'agate'
            case 'Ametista': img_proxima_pedra = 'amethyst'
            case 'Topázio': img_proxima_pedra = 'topaz'
            case _: img_proxima_pedra = 'topaz'
        with st.container(border=True):
            col2_1, col2_2 = st.columns([6,2])
            with col2_1:
                sugestoes = obter_sugestoes(resultados, int(qtd_indicadores))
                st.subheader('Sugestão de objetivo:')
                for s in sugestoes:
                    with st.expander(f"{s['indicador']} -- Atual = {round(s['valor_aluno'],2)} -- Média próxima pedra = {round(s['media_proxima'],2)}"):
                        st.divider()
                        st.markdown(f"O seu **{s['indicador']}** atual está com um valor total de **{round(s['valor_aluno'],2)}**, segundo a análise do nosso modelo de Regressão Linear, a média desse mesmo indicador para os alunos que estão na próxima pedra alcançável é de **{round(s['media_proxima'],2)}**, com isso sugerimos um dos seus focos para aprimoramento seja relacionado a aumentar esse indicador, pois a diferença entre seu indicador e dos alunos da próxima pedra é de **{round(s['diferenca'],2)}** e multiplicando por seu respectivo coeficiente, você pode vir a ganhar até **{round(s['potencial'],2)}** de INDE!!")
                        st.markdown(f"***Mas o que é o {s['indicador']}?***")
                        st.markdown(f"{explicacao_indicadores[s['indicador']]}")
            with col2_2:
                st.image(f"img/{img_proxima_pedra}.png", caption=f"Próxima pedra para alcançar - {resultados['proxima_pedra']}.", width=200)
            