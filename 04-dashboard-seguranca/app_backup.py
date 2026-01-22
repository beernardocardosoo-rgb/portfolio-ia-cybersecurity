import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import joblib
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# ========== CONFIGURAÇÃO DA PÁGINA ==========
st.set_page_config(
    page_title="Dashboard de Segurança",
    layout="wide",
    page_icon="🛡️",
    initial_sidebar_state="expanded"
)

# ========== CARREGAMENTO DE DADOS ==========
@st.cache_data
def carregar_dados():
    """Carrega o dataset de logins"""
    df = pd.read_csv('dados/logins_gerados.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

@st.cache_data
def carregar_modelo():
    """Carrega o modelo treinado"""
    modelo = joblib.load('dados/modelo_deteccao.pkl')
    scaler = joblib.load('dados/scaler.pkl')
    return modelo, scaler

# Carregar dados
df = carregar_dados()
modelo, scaler = carregar_modelo()

# ========== PROCESSAMENTO DE DADOS ==========
df['hora'] = df['timestamp'].dt.hour
df['dia_semana'] = df['timestamp'].dt.dayofweek
df['ip_encoded'] = pd.factorize(df['ip'])[0]
df['usuario_encoded'] = pd.factorize(df['usuario'])[0]
df['localizacao_encoded'] = pd.factorize(df['localizacao'])[0]

features = ['tentativas_intervalo', 'origem_confiavel', 'sucesso', 
            'hora', 'dia_semana', 'ip_encoded', 'usuario_encoded', 
            'localizacao_encoded']

X = df[features].copy()
X_scaled = scaler.transform(X)

# Fazer predições
predicoes = modelo.predict(X_scaled)
scores = modelo.score_samples(X_scaled)

df['anomalia'] = predicoes
df['anomalia_score'] = scores
df['eh_ataque'] = df['anomalia'] == -1

# ========== ESTILO CSS CUSTOMIZADO ==========
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
    }
    .metric-value {
        font-size: 32px;
        margin: 10px 0;
    }
    .alerta-critico {
        background-color: #ffebee;
        border-left: 4px solid #f44336;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    .alerta-aviso {
        background-color: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
</style>
""", unsafe_allow_html=True)

# ========== HEADER ==========
st.title("🛡️ Dashboard de Segurança")
st.markdown("**Monitoramento de Ameaças em Tempo Real** — Detecção de Força Bruta com IA")

# ========== SIDEBAR - FILTROS ==========
st.sidebar.title("🔧 Filtros")

data_inicio = st.sidebar.date_input(
    "Data inicial",
    value=df['timestamp'].min().date(),
    min_value=df['timestamp'].min().date(),
    max_value=df['timestamp'].max().date()
)

data_fim = st.sidebar.date_input(
    "Data final",
    value=df['timestamp'].max().date(),
    min_value=df['timestamp'].min().date(),
    max_value=df['timestamp'].max().date()
)

# Filtrar por data
df_filtrado = df[(df['timestamp'].dt.date >= data_inicio) & 
                 (df['timestamp'].dt.date <= data_fim)]

# ========== MÉTRICAS PRINCIPAIS ==========
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

total_eventos = len(df_filtrado)
total_ataques = (df_filtrado['eh_ataque']).sum()
taxa_ataque = (total_ataques / total_eventos * 100) if total_eventos > 0 else 0
ips_unicos = df_filtrado['ip'].nunique()

with col1:
    st.metric(
        label="📊 Total de Eventos",
        value=f"{total_eventos:,}",
        delta=f"{total_eventos} no período"
    )

with col2:
    st.metric(
        label="🚨 Ataques Detectados",
        value=f"{total_ataques:,}",
        delta=f"{taxa_ataque:.1f}%",
        delta_color="inverse"
    )

with col3:
    st.metric(
        label="🌐 IPs Únicos",
        value=f"{ips_unicos}",
        delta="monitorados"
    )

with col4:
    ips_suspeitos = df_filtrado[df_filtrado['eh_ataque']]['ip'].nunique()
    st.metric(
        label="⚠️ IPs Suspeitos",
        value=f"{ips_suspeitos}",
        delta="bloqueados"
    )

# ========== GRÁFICOS PRINCIPAIS ==========
st.markdown("---")
st.subheader("📈 Análise de Ataques")

col1, col2 = st.columns(2)

# Gráfico 1: Eventos por hora
with col1:
    eventos_hora = df_filtrado.groupby(df_filtrado['timestamp'].dt.hour).size()
    ataques_hora = df_filtrado[df_filtrado['eh_ataque']].groupby(
        df_filtrado[df_filtrado['eh_ataque']]['timestamp'].dt.hour
    ).size()

    fig_hora = go.Figure()
    fig_hora.add_trace(go.Bar(x=eventos_hora.index, y=eventos_hora.values, 
                              name='Normal', marker_color='#2ecc71'))
    fig_hora.add_trace(go.Bar(x=ataques_hora.index, y=ataques_hora.values, 
                              name='Ataque', marker_color='#e74c3c'))
    fig_hora.update_layout(
        title="Eventos por Hora do Dia",
        xaxis_title="Hora",
        yaxis_title="Quantidade",
        barmode='stack',
        height=400
    )
    st.plotly_chart(fig_hora, use_container_width=True)

# Gráfico 2: Top IPs suspeitos
with col2:
    ips_suspeitos_top = df_filtrado[df_filtrado['eh_ataque']]['ip'].value_counts().head(10)

    fig_ips = px.bar(
        x=ips_suspeitos_top.values,
        y=ips_suspeitos_top.index,
        orientation='h',
        title="Top 10 IPs Mais Suspeitos",
        labels={'x': 'Tentativas', 'y': 'IP'},
        color=ips_suspeitos_top.values,
        color_continuous_scale='Reds'
    )
    fig_ips.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig_ips, use_container_width=True)

# ========== GRÁFICOS SECUNDÁRIOS ==========
col1, col2 = st.columns(2)

# Gráfico 3: Distribuição por localização
with col1:
    localizacao_ataques = df_filtrado[df_filtrado['eh_ataque']]['localizacao'].value_counts()

    fig_loc = px.pie(
        values=localizacao_ataques.values,
        names=localizacao_ataques.index,
        title="Ataques por Localização",
        hole=0.3
    )
    fig_loc.update_layout(height=400)
    st.plotly_chart(fig_loc, use_container_width=True)

# Gráfico 4: Taxa de sucesso vs Falha
with col2:
    sucesso_count = df_filtrado['sucesso'].sum()
    falha_count = len(df_filtrado) - sucesso_count

    fig_sucesso = go.Figure(data=[
        go.Bar(name='Sucesso', x=['Resultado'], y=[sucesso_count], marker_color='#2ecc71'),
        go.Bar(name='Falha', x=['Resultado'], y=[falha_count], marker_color='#e74c3c')
    ])
    fig_sucesso.update_layout(
        title="Taxa de Sucesso vs Falha",
        barmode='stack',
        height=400,
        showlegend=True
    )
    st.plotly_chart(fig_sucesso, use_container_width=True)

# ========== ALERTAS CRÍTICOS ==========
st.markdown("---")
st.subheader("⚠️ Alertas de Segurança")

ataques_df = df_filtrado[df_filtrado['eh_ataque']].sort_values('timestamp', ascending=False)

if len(ataques_df) > 0:
    for idx, (_, row) in enumerate(ataques_df.head(5).iterrows()):
        with st.container():
            st.markdown(f"""
            <div class="alerta-critico">
                <strong>🚨 ALERTA #{idx+1}</strong><br>
                <strong>IP:</strong> {row['ip']} | <strong>Localização:</strong> {row['localizacao']}<br>
                <strong>Usuário Alvo:</strong> {row['usuario']} | <strong>Tentativas:</strong> {row['tentativas_intervalo']:.0f}<br>
                <strong>Timestamp:</strong> {row['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}<br>
                <strong>Confiança:</strong> {abs(row['anomalia_score'])*100:.1f}%
            </div>
            """, unsafe_allow_html=True)
else:
    st.success("✅ Nenhum ataque detectado no período selecionado!")

# ========== TABELA DETALHADA ==========
st.markdown("---")
st.subheader("📋 Dados Detalhados")

col1, col2 = st.columns(2)

with col1:
    st.write("**Últimos 10 Eventos Anômalos:**")
    ataques_tabela = ataques_df[['timestamp', 'ip', 'usuario', 'localizacao', 
                                   'tentativas_intervalo', 'anomalia_score']].head(10)
    ataques_tabela['anomalia_score'] = ataques_tabela['anomalia_score'].apply(lambda x: f"{abs(x)*100:.1f}%")
    st.dataframe(ataques_tabela, use_container_width=True)

with col2:
    st.write("**Resumo de IPs Suspeitos:**")
    ips_resumo = df_filtrado[df_filtrado['eh_ataque']].groupby('ip').agg({
        'usuario': 'count',
        'localizacao': 'first',
        'tentativas_intervalo': 'mean'
    }).rename(columns={
        'usuario': 'Tentativas',
        'localizacao': 'Localização',
        'tentativas_intervalo': 'Média Tentativas'
    }).sort_values('Tentativas', ascending=False).head(10)
    st.dataframe(ips_resumo, use_container_width=True)

# ========== FOOTER ==========
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray; font-size: 12px;">
    <p>🔐 Dashboard de Segurança | Detecção de Força Bruta com Machine Learning</p>
    <p>Última atualização: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """</p>
</div>
""", unsafe_allow_html=True)
