import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# ========== CONFIGURAÇÃO DA PÁGINA ==========
st.set_page_config(
    page_title="Dashboard de Segurança",
    layout="wide",
    page_icon="🛡️",
    initial_sidebar_state="expanded"
)

# ========== ESTILO CSS CUSTOMIZADO ==========
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 16px;
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
    .projeto-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# ========== HEADER ==========
st.title("🛡️ Dashboard de Segurança")
st.markdown("**Central de Monitoramento — Análise de Logs, Anomalias e Ataques de Força Bruta**")

st.markdown("---")

# ========== CARREGAMENTO DE DADOS ==========
@st.cache_data
def carregar_dados_projeto01():
    """Carrega dados do Projeto 01"""
    try:
        df = pd.read_csv('dados/relatorio_completo.csv')
        return df
    except:
        return None

@st.cache_data
def carregar_dados_projeto02():
    """Carrega dados do Projeto 02"""
    try:
        df = pd.read_csv('dados/logs_com_anomalias.csv')
        return df
    except:
        return None

@st.cache_data
def carregar_dados_projeto03():
    """Carrega dados do Projeto 03"""
    try:
        df = pd.read_csv('dados/logins_gerados.csv')
        return df
    except:
        return None

# Carregar dados
df_p01 = carregar_dados_projeto01()
df_p02 = carregar_dados_projeto02()
df_p03 = carregar_dados_projeto03()

# ========== MÉTRICAS CONSOLIDADAS ==========
st.subheader("📊 Resumo Consolidado")

col1, col2, col3, col4 = st.columns(4)

# Projeto 01
if df_p01 is not None:
    total_eventos_p01 = len(df_p01)
    with col1:
        st.metric(
            label="📝 Eventos (P01)",
            value=f"{total_eventos_p01:,}",
            delta="Logs analisados"
        )
else:
    with col1:
        st.metric(label="📝 Eventos (P01)", value="—", delta="Dados indisponíveis")

# Projeto 02
if df_p02 is not None:
    total_anomalias = (df_p02['eh_anomalia'] == True).sum() if 'eh_anomalia' in df_p02.columns else 0
    with col2:
        st.metric(
            label="🤖 Anomalias (P02)",
            value=f"{total_anomalias:,}",
            delta=f"{(total_anomalias/len(df_p02)*100):.1f}%" if len(df_p02) > 0 else "0%",
            delta_color="inverse"
        )
else:
    with col2:
        st.metric(label="🤖 Anomalias (P02)", value="—", delta="Dados indisponíveis")

# Projeto 03
if df_p03 is not None:
    total_ataques = len(df_p03)
    with col3:
        st.metric(
            label="🔐 Ataques (P03)",
            value=f"{total_ataques:,}",
            delta="Força bruta"
        )
else:
    with col3:
        st.metric(label="🔐 Ataques (P03)", value="—", delta="Dados indisponíveis")

# Total consolidado
total_consolidado = 0
if df_p01 is not None:
    total_consolidado += len(df_p01)
if df_p02 is not None:
    total_consolidado += len(df_p02)
if df_p03 is not None:
    total_consolidado += len(df_p03)

with col4:
    st.metric(
        label="📈 Total Consolidado",
        value=f"{total_consolidado:,}",
        delta="eventos monitorados"
    )

st.markdown("---")

# ========== CARDS DOS PROJETOS ==========
st.subheader("🔍 Navegue pelos Projetos")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="projeto-card">
        <h3>📝 Projeto 01</h3>
        <p><strong>Análise de Logs Linux</strong></p>
        <p>Análise exploratória de logs do sistema com IA avançada.</p>
        <p>👉 Clique em <strong>Análise Logs Linux</strong> na sidebar</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="projeto-card">
        <h3>🤖 Projeto 02</h3>
        <p><strong>Detecção de Anomalias</strong></p>
        <p>Machine Learning para identificar comportamentos anômalos.</p>
        <p>👉 Clique em <strong>Detecção Anomalias</strong> na sidebar</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="projeto-card">
        <h3>🔐 Projeto 03</h3>
        <p><strong>Força Bruta Detection</strong></p>
        <p>Detecção de ataques de força bruta em tempo real.</p>
        <p>👉 Clique em <strong>Força Bruta</strong> na sidebar</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ========== ALERTAS CONSOLIDADOS ==========
st.subheader("⚠️ Alertas Críticos Consolidados")

alertas_count = 0

if df_p02 is not None and 'eh_anomalia' in df_p02.columns:
    anomalias = df_p02[df_p02['eh_anomalia'] == True]
    if len(anomalias) > 0:
        st.markdown(f"""
        <div class="alerta-critico">
            <strong>🤖 ANOMALIAS DETECTADAS (P02)</strong><br>
            Total: {len(anomalias)} eventos anômalos identificados
        </div>
        """, unsafe_allow_html=True)
        alertas_count += 1

if df_p03 is not None:
    st.markdown(f"""
    <div class="alerta-critico">
        <strong>🔐 ATAQUES DE FORÇA BRUTA (P03)</strong><br>
        Total: {len(df_p03)} tentativas monitoradas
    </div>
    """, unsafe_allow_html=True)
    alertas_count += 1

if alertas_count == 0:
    st.success("✅ Nenhum alerta crítico no momento!")

st.markdown("---")

# ========== INFORMAÇÕES ==========
st.subheader("ℹ️ Sobre este Dashboard")

st.markdown("""
Este **Dashboard de Segurança** integra 3 projetos de IA + CyberSecurity:

• **Projeto 01 — Análise de Logs Linux**  
  Análise exploratória de logs do sistema com visualizações e IA.

• **Projeto 02 — Detecção de Anomalias**  
  Machine Learning (Isolation Forest) para detectar comportamentos anômalos.

• **Projeto 03 — Força Bruta Detection**  
  Detecção de ataques de força bruta com modelo treinado.

---

**Como usar:**
1. Selecione um projeto na barra lateral (sidebar)
2. Explore os gráficos e métricas
3. Analise os alertas de segurança
4. Use os filtros para investigar períodos específicos

**Tecnologias:**
Python • Streamlit • Plotly • Pandas • Scikit-learn • IA (Mistral/Ollama)
""")

st.markdown("---")

# ========== FOOTER ==========
st.markdown("""
<div style="text-align: center; color: gray; font-size: 12px;">
    <p>🔐 Dashboard de Segurança | IA + CyberSecurity</p>
    <p>Última atualização: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """</p>
</div>
""", unsafe_allow_html=True)
