import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import warnings
import os
warnings.filterwarnings('ignore')

# ========== CONFIGURAÇÃO DA PÁGINA ==========
st.set_page_config(
    page_title="Análise de Logs Linux",
    layout="wide",
    page_icon="📝",
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
</style>
""", unsafe_allow_html=True)

# ========== HEADER ==========
st.title("📝 Análise de Logs Linux")
st.markdown("**Projeto 01** — Análise Exploratória de Logs do Sistema com IA")

# ========== CARREGAMENTO DE DADOS ==========
def carregar_dados():
    """Carrega o dataset de logs com caminho dinâmico."""
    try:
        raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        caminho_csv = os.path.join(raiz, "dados", "relatorio_completo.csv")

        df = pd.read_csv(caminho_csv)

        if 'data' in df.columns and 'hora' in df.columns:
            # Converter data no formato "Jan 15" e hora "08:23:45"
            try:
                df['timestamp'] = pd.to_datetime(
                    df['data'] + ' ' + df['hora'],
                    format='%b %d %H:%M:%S',
                    errors='coerce'
                )
            except:
                st.error("Erro ao converter as datas com o formato esperado.")
        else:
            st.error("❌ Colunas 'data' e 'hora' não encontradas no CSV")
            return None

        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {str(e)}")
        return None

# Carregar dados
df = carregar_dados()

if df is not None:

    # Remover valores NaT (datas inválidas)
    df_valido = df.dropna(subset=['timestamp'])

    if len(df_valido) == 0:
        st.error("❌ Nenhuma data válida encontrada no dataset.")
        st.stop()

    # ========== SIDEBAR - FILTROS ==========
    st.sidebar.title("🔧 Filtros")

    # Filtro por data
    data_inicio = st.sidebar.date_input(
        "Data inicial",
        value=df_valido['timestamp'].min().date(),
        min_value=df_valido['timestamp'].min().date(),
        max_value=df_valido['timestamp'].max().date()
    )

    data_fim = st.sidebar.date_input(
        "Data final",
        value=df_valido['timestamp'].max().date(),
        min_value=df_valido['timestamp'].min().date(),
        max_value=df_valido['timestamp'].max().date()
    )

    # Filtro por IP
    ips_unicos = sorted(df_valido['ip'].unique())
    ip_selecionado = st.sidebar.multiselect(
        "IPs para analisar",
        options=ips_unicos,
        default=ips_unicos[:5] if len(ips_unicos) > 5 else ips_unicos
    )

    # Filtro por usuário
    usuarios_unicos = sorted(df_valido['usuario'].unique())
    usuario_selecionado = st.sidebar.multiselect(
        "Usuários para analisar",
        options=usuarios_unicos,
        default=usuarios_unicos[:5] if len(usuarios_unicos) > 5 else usuarios_unicos
    )

    # Filtro por evento
    eventos_unicos = sorted(df_valido['evento'].unique())
    evento_selecionado = st.sidebar.multiselect(
        "Eventos para analisar",
        options=eventos_unicos,
        default=eventos_unicos
    )

    # Aplicar filtros
    df_filtrado = df_valido[
        (df_valido['timestamp'].dt.date >= data_inicio) &
        (df_valido['timestamp'].dt.date <= data_fim) &
        (df_valido['ip'].isin(ip_selecionado)) &
        (df_valido['usuario'].isin(usuario_selecionado)) &
        (df_valido['evento'].isin(evento_selecionado))
    ]

    # ========== MÉTRICAS PRINCIPAIS ==========
    st.markdown("---")
    st.subheader("📊 Resumo dos Logs")

    col1, col2, col3, col4 = st.columns(4)

    total_eventos = len(df_filtrado)
    ips_unicos_filtrado = df_filtrado['ip'].nunique()
    usuarios_unicos_filtrado = df_filtrado['usuario'].nunique()
    status_sucesso = (df_filtrado['status'] == 'SUCESSO').sum() if 'status' in df_filtrado.columns else 0

    with col1:
        st.metric(
            label="📈 Total de Eventos",
            value=f"{total_eventos:,}",
            delta="logs analisados"
        )

    with col2:
        st.metric(
            label="🌐 IPs Únicos",
            value=f"{ips_unicos_filtrado}",
            delta="origem dos logs"
        )

    with col3:
        st.metric(
            label="👤 Usuários Únicos",
            value=f"{usuarios_unicos_filtrado}",
            delta="contas ativas"
        )

    with col4:
        taxa_sucesso = (status_sucesso / total_eventos * 100) if total_eventos > 0 else 0
        st.metric(
            label="✅ Taxa de Sucesso",
            value=f"{taxa_sucesso:.1f}%",
            delta=f"{status_sucesso} eventos"
        )

    st.markdown("---")

    # ========== GRÁFICOS PRINCIPAIS ==========
    st.subheader("📈 Análise Visual dos Logs")

    col1, col2 = st.columns(2)

    # Gráfico 1: Top IPs
    with col1:
        top_ips = df_filtrado['ip'].value_counts().head(10)
        fig_ips = px.bar(
            x=top_ips.values,
            y=top_ips.index,
            orientation='h',
            title="Top 10 IPs com Mais Eventos",
            labels={'x': 'Quantidade', 'y': 'IP'},
            color=top_ips.values,
            color_continuous_scale='Blues'
        )
        fig_ips.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_ips, use_container_width=True)

    # Gráfico 2: Top Usuários
    with col2:
        top_usuarios = df_filtrado['usuario'].value_counts().head(10)
        fig_usuarios = px.bar(
            x=top_usuarios.values,
            y=top_usuarios.index,
            orientation='h',
            title="Top 10 Usuários com Mais Eventos",
            labels={'x': 'Quantidade', 'y': 'Usuário'},
            color=top_usuarios.values,
            color_continuous_scale='Greens'
        )
        fig_usuarios.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_usuarios, use_container_width=True)

    # Gráfico 3: Distribuição de Eventos
    col1, col2 = st.columns(2)

    with col1:
        eventos_dist = df_filtrado['evento'].value_counts()
        fig_eventos = px.pie(
            values=eventos_dist.values,
            names=eventos_dist.index,
            title="Distribuição de Eventos",
            hole=0.3
        )
        fig_eventos.update_layout(height=400)
        st.plotly_chart(fig_eventos, use_container_width=True)

    # Gráfico 4: Status dos Eventos
    with col2:
        if 'status' in df_filtrado.columns:
            status_dist = df_filtrado['status'].value_counts()
            fig_status = px.pie(
                values=status_dist.values,
                names=status_dist.index,
                title="Distribuição de Status",
                hole=0.3,
                color_discrete_map={'SUCESSO': '#2ecc71', 'FALHA': '#e74c3c'}
            )
            fig_status.update_layout(height=400)
            st.plotly_chart(fig_status, use_container_width=True)

    # Gráfico 5: Timeline de Eventos
    st.subheader("📅 Timeline de Eventos")

    eventos_timeline = df_filtrado.groupby(df_filtrado['timestamp'].dt.date).size()
    fig_timeline = go.Figure()
    fig_timeline.add_trace(go.Scatter(
        x=eventos_timeline.index,
        y=eventos_timeline.values,
        mode='lines+markers',
        name='Eventos',
        line=dict(color='#667eea', width=2),
        marker=dict(size=8)
    ))
    fig_timeline.update_layout(
        title="Eventos ao Longo do Tempo",
        xaxis_title="Data",
        yaxis_title="Quantidade de Eventos",
        height=400,
        hovermode='x unified'
    )
    st.plotly_chart(fig_timeline, use_container_width=True)

    st.markdown("---")

    # ========== TABELA DETALHADA ==========
    st.subheader("📋 Dados Detalhados")

    st.write(f"**Mostrando {len(df_filtrado)} eventos**")

    colunas_exibicao = ['timestamp', 'ip', 'usuario', 'evento', 'status']
    colunas_disponiveis = [col for col in colunas_exibicao if col in df_filtrado.columns]

    df_exibicao = df_filtrado[colunas_disponiveis].sort_values('timestamp', ascending=False)

    st.dataframe(df_exibicao, use_container_width=True, height=400)

    # ========== DOWNLOAD DE DADOS ==========
    st.markdown("---")
    st.subheader("📥 Exportar Dados")

    col1, col2 = st.columns(2)

    with col1:
        csv = df_filtrado.to_csv(index=False)
        st.download_button(
            label="📥 Baixar como CSV",
            data=csv,
            file_name=f"logs_analise_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )

    with col2:
        st.info("💡 Use o botão acima para exportar os dados filtrados.")

    st.markdown("---")

    # ========== FOOTER ==========
    st.markdown("""
    <div style="text-align: center; color: gray; font-size: 12px;">
        <p>📝 Análise de Logs Linux | Projeto 01</p>
        <p>Última atualização: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.error("❌ Não foi possível carregar os dados.")
