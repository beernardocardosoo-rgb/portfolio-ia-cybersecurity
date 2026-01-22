import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import warnings
import os
warnings.filterwarnings("ignore")

# -----------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------
st.set_page_config(
    page_title="Detector de Anomalias ML",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Detector de Anomalias com Machine Learning")
st.markdown("Projeto 02 — Detecção Inteligente de Padrões Anormais")

# -----------------------------
# FUNÇÃO DE CARREGAMENTO
# -----------------------------
def carregar_dados():

    caminho = r"C:\Users\Bernardo\Desktop\portfolio-ia-cybersecurity\02-detector-anomalias-ml\dados\logs_com_anomalias.csv"

    if not os.path.exists(caminho):
        st.error("❌ Arquivo não encontrado.")
        return None

    df = pd.read_csv(caminho)

    # Converter timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Garantir coluna booleana
    if "eh_anomalia" in df.columns:
        df["eh_anomalia"] = df["eh_anomalia"].astype(str).str.lower() == "true"
    else:
        df["eh_anomalia"] = False

    # Criar anomalias REALISTAS automáticas (top 5% maior score)
    if "anomalia_score" in df.columns:
        limite = df["anomalia_score"].quantile(0.95)
        df["eh_anomalia"] = df["anomalia_score"] >= limite

    return df

# Carrega dados
df = carregar_dados()

if df is None:
    st.stop()

# -----------------------------
# DEBUG (mostra as 5 primeiras linhas)
# -----------------------------
with st.expander("🔍 Debug – Visualizar Dados"):
    st.write(df.head())
    st.write("Valores únicos de eh_anomalia:", df["eh_anomalia"].value_counts())
    st.write("Intervalo de score:", df["anomalia_score"].describe())

# -----------------------------
# FILTROS
#-------------
st.sidebar.header("Filtros")

data_inicio = st.sidebar.date_input("Data inicial", df["timestamp"].min().date())
data_fim = st.sidebar.date_input("Data final", df["timestamp"].max().date())

tipos = sorted(df["tipo"].unique())
tipo_sel = st.sidebar.multiselect("Tipo", tipos, default=tipos)

apenas_anomalias = st.sidebar.checkbox("Mostrar apenas anomalias", False)

# Filtragem
df_f = df[
    (df["timestamp"].dt.date >= data_inicio) &
    (df["timestamp"].dt.date <= data_fim) &
    (df["tipo"].isin(tipo_sel))
]

if apenas_anomalias:
    df_f = df_f[df_f["eh_anomalia"] == True]

# -----------------------------
# KPIs
# -----------------------------
st.subheader("📊 Resumo")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de Logs", len(df_f))

with col2:
    total_anom = df_f["eh_anomalia"].sum()
    st.metric("Anomalias", int(total_anom))

with col3:
    st.metric("Score Médio", round(df_f["anomalia_score"].mean(), 4))

# -----------------------------
# GRÁFICOS
# -----------------------------
st.subheader("📈 Análise Visual")

# Timeline
fig = px.line(df_f, x="timestamp", y="anomalia_score", color="eh_anomalia", title="Score ao longo do tempo")
st.plotly_chart(fig, use_container_width=True)

# Histograma
fig2 = px.histogram(df_f, x="anomalia_score", nbins=50, title="Distribuição de Score")
st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# TABELA
# -----------------------------
st.subheader("📋 Logs Detalhados")
st.dataframe(df_f, use_container_width=True)

# -----------------------------
# DOWNLOAD
# -----------------------------
csv = df_f.to_csv(index=False)
st.download_button("📥 Exportar CSV", csv, "logs_filtrados.csv", "text/csv")

