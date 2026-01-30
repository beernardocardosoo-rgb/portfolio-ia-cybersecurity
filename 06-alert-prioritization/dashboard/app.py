# dashboard/app.py

import os
import sys
import pathlib

import streamlit as st
import pandas as pd

# Ajustar o path para conseguir importar o pacote src
ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.prioritization import carregar_alertas_priorizados  # type: ignore


# Caminho para o CSV gerado pelo notebook
DEFAULT_CSV_PATH = ROOT_DIR / "data" / "ddos_alerts_prioritized.csv"


@st.cache_data
def load_data(csv_path: str) -> pd.DataFrame:
    return carregar_alertas_priorizados(csv_path)


def main():
    st.set_page_config(
        page_title="Prioritização de Alertas DDoS",
        layout="wide"
    )

    st.title("Dashboard de Prioritização de Alertas DDoS")

    st.markdown("""
Este dashboard exibe a **fila de alertas priorizados** gerada pelo modelo de detecção de DDoS baseado em Random Forest.

**Como funciona:**
- Cada fluxo de rede recebe uma **probabilidade de ser DDoS** (0 a 1).
- Com base nessa probabilidade, o sistema atribui uma **prioridade**:
  - 🔴 **ALTA**: probabilidade ≥ 0.95 (atenção imediata)
  - 🟡 **MÉDIA**: 0.70 ≤ probabilidade < 0.95 (investigar)
  - 🟢 **BAIXA**: probabilidade < 0.70 (monitorar)

Use os filtros na barra lateral para explorar os alertas por prioridade e tipo de tráfego.
""")

    # Sidebar – seleção de arquivo e filtros
    st.sidebar.header("Configurações")

    csv_path = st.sidebar.text_input(
        "Caminho do CSV de alertas priorizados",
        value=str(DEFAULT_CSV_PATH)
    )

    if not os.path.exists(csv_path):
        st.error(f"Arquivo CSV não encontrado: {csv_path}")
        st.stop()

    df = load_data(csv_path)

    # Filtros básicos
    prioridades = sorted(df['prioridade'].dropna().unique().tolist())
    prioridade_sel = st.sidebar.multiselect(
        "Filtrar por prioridade",
        options=prioridades,
        default=prioridades  # todas selecionadas inicialmente
    )

    # Se existir Label no CSV (para validação)
    labels = df['Label'].unique().tolist() if 'Label' in df.columns else []
    label_sel = st.sidebar.multiselect(
        "Filtrar por Label (se disponível)",
        options=labels,
        default=labels
    ) if labels else []

    # Aplicar filtros
    df_filtrado = df.copy()
    if prioridade_sel:
        df_filtrado = df_filtrado[df_filtrado['prioridade'].isin(prioridade_sel)]
    if label_sel:
        df_filtrado = df_filtrado[df_filtrado['Label'].isin(label_sel)]

    # Métricas de topo
    col1, col2, col3 = st.columns(3)

    total_alertas = len(df_filtrado)
    total_alta = (df_filtrado['prioridade'] == 'ALTA').sum()
    total_media = (df_filtrado['prioridade'] == 'MEDIA').sum()
    total_baixa = (df_filtrado['prioridade'] == 'BAIXA').sum()

    with col1:
        st.metric("Total de alertas filtrados", total_alertas)

    with col2:
        st.metric("Prioridade ALTA", total_alta)

    with col3:
        st.metric("Prioridade MÉDIA / BAIXA", total_media + total_baixa)

    st.markdown("---")

    # Gráfico simples de distribuição por prioridade
    st.subheader("Distribuição de alertas por prioridade")

    if not df_filtrado.empty:
        contagem_prioridade = df_filtrado['prioridade'].value_counts().sort_index()
        st.bar_chart(contagem_prioridade)
    else:
        st.info("Nenhum alerta com os filtros selecionados.")

    st.markdown("---")

    # Tabela de alertas
    st.subheader("Fila de alertas priorizada")

    # Criar coluna auxiliar para ordenar corretamente (ALTA > MEDIA > BAIXA)
    prioridade_ordem = {'ALTA': 0, 'MEDIA': 1, 'BAIXA': 2}
    df_filtrado_copia = df_filtrado.copy()
    df_filtrado_copia['_ordem'] = df_filtrado_copia['prioridade'].map(prioridade_ordem)

    # Ordenar: primeiro por prioridade (ALTA > MEDIA > BAIXA), depois por probabilidade decrescente
    df_exibir = df_filtrado_copia.sort_values(
        by=['_ordem', 'ddos_proba'],
        ascending=[True, False]
    ).drop(columns=['_ordem'])  # remove coluna auxiliar antes de exibir

    st.dataframe(
        df_exibir,
        use_container_width=True,
        height=400
    )


if __name__ == "__main__":
    main()
