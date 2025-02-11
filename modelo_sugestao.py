import pandas as pd
import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# =============================================================================
# Função: formatar_tipo_campos
# =============================================================================
def formatar_tipo_campos(df):
    """
    Ajusta os tipos de dados do DataFrame para garantir que as operações 
    matemáticas e análises sejam realizadas corretamente.

    - Para cada coluna da lista ["INDE", "IAA", "IEG", "IPS", "IDA", "IPP", "IPV", "IAN"]:
        * Converte os dados para string (caso não estejam) e substitui vírgulas por pontos,
          permitindo a conversão correta para o tipo float.
    
    Parâmetros:
        df (DataFrame): DataFrame original com os dados dos alunos.
    
    Retorna:
        DataFrame com os tipos de dados formatados.
    """
    
    # Para cada coluna numérica, substitui vírgulas por pontos e converte para float
    for col in ["INDE", "IAA", "IEG", "IPS", "IDA", "IPP", "IPV", "IAN"]:
        df[col] = df[col].astype(str).str.replace(",", ".").astype(float)
    
    return df

# =============================================================================
# Função: sugerir_melhorias
# =============================================================================
def sugerir_melhorias(nome_aluno, df, modelo, scaler, variaveis, pedras, top_n=1):
    """
    Gera sugestões de melhoria para um aluno específico com base no seu desempenho 
    e na comparação com a média dos alunos na próxima faixa de classificação (pedra).

    Passos realizados:
      1. Filtra os registros do aluno pelo nome e seleciona o registro do ano mais recente.
      2. Obtém o INDE atual e a classificação ("pedra") do aluno.
      3. Se o aluno já estiver no nível máximo (Topázio) ou não tiver classificação definida,
         retorna o resultado sem sugestões.
      4. Identifica a próxima pedra (classificação) na sequência definida.
      5. Calcula o INDE alvo como a média dos limites da próxima pedra.
      6. Determina a diferença entre o INDE alvo e o INDE atual.
      7. Seleciona os alunos que estão na faixa da próxima pedra para calcular a média dos indicadores.
      8. Para cada indicador, compara o valor do aluno com a média da próxima faixa e, 
         utilizando o coeficiente do modelo, calcula o potencial de ganho.
      9. Ordena as sugestões de melhoria com base no potencial de ganho e monta um relatório.

    Parâmetros:
        nome_aluno (str): Nome do aluno a ser analisado.
        df (DataFrame): DataFrame com os dados dos alunos.
        modelo (LinearRegression): Modelo de regressão linear treinado.
        scaler (StandardScaler): Objeto de normalização (não utilizado diretamente nesta função,
                                 mas incluído para padronização dos processos, se necessário).
        variaveis (list): Lista de colunas que representam os indicadores (features).
        pedras (dict): Dicionário com os limites de cada faixa de classificação.
        top_n (int): Número de indicadores mais relevantes a serem destacados nas sugestões.
    
    Retorna:
        dict: Dicionário com as informações do aluno, indicadores, sugestões de melhoria e um texto descritivo.
    """
    target_variable = 'INDE'
    # Filtra o DataFrame para encontrar os registros do aluno
    aluno = df[df['NOME'] == nome_aluno]
    if aluno.empty:
        return {"erro": "Aluno não encontrado no DataFrame."}
    
    # Seleciona o registro do aluno referente ao ano mais recente (última linha após ordenação por ano)
    aluno_recente = aluno.sort_values(by="ANO").iloc[-1]
    inde_aluno = aluno_recente[target_variable]  # INDE atual do aluno
    
    # Obtém a classificação (pedra) e o ano do registro
    pedra_atual = aluno_recente["PEDRA"]
    ano_atual = aluno_recente["ANO"].astype(str)
    
    texto = f"Aluno {nome_aluno} possui INDE de {inde_aluno:.2f}, classificado como {pedra_atual}.\n"
    
    # Se o aluno já estiver no nível máximo ou não tiver uma classificação definida,
    # retorna as informações sem sugestões de melhoria.
    if pedra_atual == "Topázio" or pd.isna(pedra_atual):
        texto += "O aluno já atingiu a melhor pedra ou não se encaixa em nenhuma faixa."
        result_json = {
            "nome": nome_aluno,
            "inde": inde_aluno,
            "pedra": pedra_atual,
            "ano": ano_atual,
            "proxima_pedra": None,
            "proximo_inde_medio_alcancavel": None,
            "indicadores": {var: aluno_recente[var] for var in variaveis},
            "sugestoes": [],
            "texto": texto
        }
        return result_json
    
    # Define a ordem das classificações ("pedras")
    ordem_pedras = ["Quartzo", "Ágata", "Ametista", "Topázio"]
    try:
        indice_atual = ordem_pedras.index(pedra_atual)
    except ValueError:
        return {"erro": "A pedra atual do aluno não está definida na ordem de pedras."}
    
    # Identifica a próxima pedra, se existir
    proxima_pedra = ordem_pedras[indice_atual + 1] if indice_atual + 1 < len(ordem_pedras) else None
    if proxima_pedra is None:
        texto += "Não há próxima pedra definida."
        result_json = {
            "nome": nome_aluno,
            "inde": inde_aluno,
            "pedra": pedra_atual,
            "ano": ano_atual,
            "proxima_pedra": None,
            "proximo_inde_medio_alcancavel": None,
            "indicadores": {var: aluno_recente[var] for var in variaveis},
            "sugestoes": [],
            "texto": texto
        }
        return result_json
    
    # Calcula o INDE alvo para a próxima pedra (média dos limites mínimo e máximo)
    limites_prox = pedras[proxima_pedra]
    inde_alvo = (limites_prox["min"] + limites_prox["max"]) / 2
    
    texto += f"Para atingir a pedra {proxima_pedra}, o aluno precisa alcançar um INDE próximo de {inde_alvo:.2f}.\n"
    
    # Calcula a diferença entre o INDE alvo e o INDE atual do aluno
    delta_ind = inde_alvo - inde_aluno
    if delta_ind <= 0:
        texto += "O aluno já atingiu ou ultrapassou o INDE médio da próxima pedra. Parabéns!"
        result_json = {
            "nome": nome_aluno,
            "inde": inde_aluno,
            "pedra": pedra_atual,
            "ano": ano_atual,
            "proxima_pedra": proxima_pedra,
            "proximo_inde_medio_alcancavel": inde_alvo,
            "indicadores": {var: aluno_recente[var] for var in variaveis},
            "sugestoes": [],
            "texto": texto
        }
        return result_json
    
    texto += f"Falta aproximadamente {delta_ind:.2f} no INDE para alcançar a próxima pedra.\n"
    
    # Seleciona os alunos que estão na faixa da próxima pedra (para comparar os indicadores)
    prox_min = limites_prox["min"]
    prox_max = limites_prox["max"]
    alunos_prox = df[(df[target_variable] >= prox_min) & (df[target_variable] < prox_max)]
    if alunos_prox.empty:
        texto += "Não há dados suficientes de alunos na faixa da próxima pedra para comparação."
        result_json = {
            "nome": nome_aluno,
            "inde": inde_aluno,
            "pedra": pedra_atual,
            "ano": ano_atual,
            "proxima_pedra": proxima_pedra,
            "proximo_inde_medio_alcancavel": inde_alvo,
            "indicadores": {var: aluno_recente[var] for var in variaveis},
            "sugestoes": [],
            "texto": texto
        }
        return result_json
    
    # Calcula a média dos indicadores dos alunos que já estão na faixa da próxima pedra
    media_prox = alunos_prox[variaveis].mean()
    
    # Para cada indicador, calcula o potencial de melhoria com base no coeficiente do modelo
    sugestoes = []
    for i, var in enumerate(variaveis):
        valor_aluno = aluno_recente[var]
        media_var = media_prox[var]
        coef = modelo.coef_[i]
        
        # Se o coeficiente for positivo e o valor do aluno estiver abaixo da média, 
        # calcula a diferença e o potencial de ganho
        if coef > 0 and valor_aluno < media_var:
            diferenca = media_var - valor_aluno
            potencial = diferenca * coef  
        else:
            diferenca = 0
            potencial = 0
        
        sugestoes.append({
            'indicador': var,
            'valor_aluno': valor_aluno,
            'media_proxima': media_var,
            'coeficiente': coef,
            'diferenca': diferenca,
            'potencial': potencial
        })
    
    # Ordena as sugestões de melhoria com base no potencial de ganho (ordem decrescente)
    sugestoes_ordenadas = sorted(sugestoes, key=lambda x: x['potencial'], reverse=True)
    
    texto += f"Sugestões para melhoria nos {min(top_n, len(sugestoes_ordenadas))} indicadores mais importantes:\n"
    for s in sugestoes_ordenadas[:top_n]:
        texto += (f" - {s['indicador']}: seu valor = {s['valor_aluno']:.2f}, "
                  f"média na próxima pedra = {s['media_proxima']:.2f} "
                  f"-> potencial de ganho no INDE: {s['potencial']:.2f}\n")
    
    # Monta o dicionário com todas as informações e sugestões calculadas
    result_json = {
        "nome": nome_aluno,
        "inde": inde_aluno,
        "pedra": pedra_atual,
        "ano": ano_atual,
        "proxima_pedra": proxima_pedra,
        "proximo_inde_medio_alcancavel": inde_alvo,
        "indicadores": {var: aluno_recente[var] for var in variaveis},
        "sugestoes": sugestoes,  # Todas as sugestões calculadas, não somente as top_n
        "texto": texto
    }
    
    return result_json

def modelo_sugestao(nome_aluno: str, qtd_indicadores: int) -> json :
    # =============================================================================
    # Definição das faixas de classificação ("pedras")
    # =============================================================================
    pedras = {
        "Quartzo": {"min": 2.405, "max": 6.110},
        "Ágata": {"min": 6.111, "max": 7.154},
        "Ametista": {"min": 7.154, "max": 8.198},
        "Topázio": {"min": 8.198, "max": 9.294}
    }

    # =============================================================================
    # Carregamento e pré-processamento dos dados
    # =============================================================================

    # Carrega os dados a partir do arquivo CSV, utilizando ";" como separador
    df = pd.read_csv('base_dados\\base_full.csv', sep=';')

    # Lista dos indicadores que serão utilizados no modelo
    indicadores = ["IAA", "IEG", "IPS", "IDA", "IPP", "IPV", "IAN"]

    # Remove linhas que possuem valores nulos nas colunas essenciais (indicadores e INDE)
    df_limpo = df.dropna(subset=indicadores + ['INDE'])

    # Formata os tipos dos campos (converte colunas numéricas para o tipo correto)
    df_novo = formatar_tipo_campos(df_limpo)
    print(f"Total de registros após limpeza: {df_novo.shape[0]}")

    # Atualiza o DataFrame principal com os dados limpos e formatados
    df = df_novo.copy()

    # Define as variáveis (features) e a variável-alvo
    variaveis = ["IAA", "IEG", "IPS", "IDA", "IPP", "IPV", "IAN"]
    target_variable = 'INDE'

    # Separa os dados em features (X) e target (y)
    X = df[variaveis]
    y = df[target_variable]

    # Divide os dados em conjuntos de treinamento (70%) e teste (30%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # =============================================================================
    # Normalização e Treinamento do Modelo
    # =============================================================================

    # Normaliza as features para ter média 0 e desvio padrão 1,
    # o que facilita a interpretação dos coeficientes do modelo
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Treina um modelo de regressão linear com os dados normalizados
    modelo = LinearRegression()
    modelo.fit(X_train_scaled, y_train)

    # =============================================================================
    # Avaliação do Modelo
    # =============================================================================

    # Realiza previsões com o conjunto de teste
    y_pred = modelo.predict(X_test_scaled)
    print("Avaliação do Modelo:")
    print("R²:", r2_score(y_test, y_pred))
    print("MSE:", mean_squared_error(y_test, y_pred))

    # Exibe os coeficientes do modelo para cada indicador
    coeficientes = modelo.coef_
    df_coef = pd.DataFrame({
        'Variável': variaveis,
        'Coeficiente': coeficientes
    }).sort_values(by='Coeficiente', ascending=False)
    print("\nCoeficientes do modelo:")
    print(df_coef)

    # =============================================================================
    # Geração de Sugestões de Melhoria para um Aluno Específico
    # =============================================================================

    # Exemplo de uso da função de sugestões para o aluno 'ALUNO-14'
    resultado = sugerir_melhorias(nome_aluno, df, modelo, scaler, variaveis, pedras, top_n=qtd_indicadores)
    print("\nSugestões de melhoria:")
    print(resultado["texto"])

    # Salva o resultado obtido em um arquivo JSON para uso posterior (ex: integração com Streamlit)
    with open("resultado_aluno.json", "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=4)

    return resultado