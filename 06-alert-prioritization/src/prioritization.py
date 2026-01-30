# src/prioritization.py

import pandas as pd

def definir_prioridade(prob, alta=0.95, media=0.70):
    """
    Converte probabilidade de DDoS em nível de prioridade.
    - ALTA : prob >= alta
    - MÉDIA: media <= prob < alta
    - BAIXA: prob < media
    """
    if prob >= alta:
        return "ALTA"
    elif prob >= media:
        return "MEDIA"
    else:
        return "BAIXA"


def carregar_alertas_priorizados(csv_path: str) -> pd.DataFrame:
    """
    Carrega o CSV de alertas priorizados gerado pelo notebook
    e retorna um DataFrame.
    """
    df = pd.read_csv(csv_path)
    # Garante que a coluna 'prioridade' exista; se não existir, tenta criar a partir de ddos_proba
    if 'prioridade' not in df.columns and 'ddos_proba' in df.columns:
        df['prioridade'] = df['ddos_proba'].apply(definir_prioridade)
    return df
