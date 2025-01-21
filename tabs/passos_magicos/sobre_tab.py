import streamlit as st

def show():
    st.markdown(''' 
                A ONG **:red[Passos Mágicos]** é uma organização que busca ajudar crianças e adolescentes em situação de vulnerabilidade social, oferecendo oportunidades de crescimento e desenvolvimento. Ela trabalha com diversos projetos nas áreas de educação, cultura e esporte, com o objetivo de proporcionar um futuro mais digno para os jovens atendidos. \n
                Os programas incluem atividades como reforço escolar, apoio psicológico, oficinas culturais e esportivas, entre outras, para ajudar esses jovens a desenvolverem suas habilidades e talentos. A ideia é criar um ambiente de apoio e aprendizado, para que eles possam superar os desafios da vida e ter mais chances de alcançar seus objetivos.
                ''')
    
    col0, col1 = st.columns([1, 1])

    with col0: 
        st.subheader(':red[Missão]', divider='red')
        st.markdown('''
                    Sua missão, de acordo com o site da ONG, é: <br/>
                    <quote>:orange["[...] transformar a vida de jovens e crianças, oferecendo ferramentas para levá-los a melhores oportunidades de vida."] </quote>
                    ''', unsafe_allow_html=True)
        
        st.subheader(':red[Visão]', divider='red')
        st.markdown('''
                    Sua visão, de acordo com o site da ONG, é: <br/>
                    <quote>:orange["[...] viver em um Brasil no qual todas as crianças e jovens têm iguais oportunidades para realizarem seus sonhos e são agentes transformadores de suas próprias vidas. </quote>]
                    ''', unsafe_allow_html=True)
        
    with col1:
        st.subheader(':red[Valores]', divider='red')
        st.markdown('''
                    Seus valores, de acordo com o site da ONG, são:
                    - Empatia
                    - Amor ao aprendizado
                    - Poder em acreditar em si e no próximo
                    - Pertencimento
                    - Gratidão
                    - Busca pelo Saber
                    - Educação que transforma e ajuda a transformar
                    - Aprender a aprender
                    ''')