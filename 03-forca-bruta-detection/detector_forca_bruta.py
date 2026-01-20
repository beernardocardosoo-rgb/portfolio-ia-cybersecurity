import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("🔐 DETECTOR DE FORÇA BRUTA COM MACHINE LEARNING")
print("=" * 70)

# ========== CARREGAR DADOS ==========
print("\n📂 Carregando dataset...")
df = pd.read_csv('dados/logins_gerados.csv')
print(f"✅ Dataset carregado: {len(df)} eventos")

# ========== PRÉ-PROCESSAMENTO ==========
print("\n🔧 Pré-processando dados...")

# Converter timestamp para datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extrair features temporais
df['hora'] = df['timestamp'].dt.hour
df['dia_semana'] = df['timestamp'].dt.dayofweek

# Codificar variáveis categóricas
df['ip_encoded'] = pd.factorize(df['ip'])[0]
df['usuario_encoded'] = pd.factorize(df['usuario'])[0]
df['localizacao_encoded'] = pd.factorize(df['localizacao'])[0]

# Features para o modelo
features = ['tentativas_intervalo', 'origem_confiavel', 'sucesso', 
            'hora', 'dia_semana', 'ip_encoded', 'usuario_encoded', 
            'localizacao_encoded']

X = df[features].copy()

# Normalizar features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(f"✅ Features preparadas: {len(features)} variáveis")

# ========== TREINAR MODELO ==========
print("\n🤖 Treinando modelo Isolation Forest...")

# Isolation Forest para detecção de anomalias
modelo = IsolationForest(
    contamination=0.05,  # 5% são anomalias (ataques)
    random_state=42,
    n_estimators=100
)

# Treinar
predicoes = modelo.fit_predict(X_scaled)
scores = modelo.score_samples(X_scaled)

# Adicionar ao dataframe
df['anomalia'] = predicoes  # -1 = anomalia, 1 = normal
df['anomalia_score'] = scores

print(f"✅ Modelo treinado com sucesso!")

# ========== ANÁLISE DE RESULTADOS ==========
print("\n📊 RESULTADOS DA DETECÇÃO:")
print("-" * 70)

total_anomalias = (df['anomalia'] == -1).sum()
total_normais = (df['anomalia'] == 1).sum()

print(f"🔍 Eventos normais: {total_normais} ({100*total_normais/len(df):.1f}%)")
print(f"🚨 Eventos anômalos (ataques): {total_anomalias} ({100*total_anomalias/len(df):.1f}%)")

# ========== IDENTIFICAR IPS ATACANTES ==========
print("\n🕵️ IPS SUSPEITOS DETECTADOS:")
print("-" * 70)

ips_suspeitos = df[df['anomalia'] == -1]['ip'].value_counts().head(10)

for ip, count in ips_suspeitos.items():
    localizacao = df[df['ip'] == ip]['localizacao'].iloc[0]
    confianca = (count / total_anomalias) * 100
    print(f"   IP: {ip}")
    print(f"   Tentativas anômalas: {count}")
    print(f"   Localização: {localizacao}")
    print(f"   Confiança: {confianca:.1f}%")
    print()

# ========== GERAR ALERTAS ==========
print("\n⚠️ GERANDO ALERTAS...")

alertas = []

for ip in ips_suspeitos.head(5).index:
    eventos_ip = df[df['ip'] == ip]
    eventos_ataque = eventos_ip[eventos_ip['anomalia'] == -1]

    usuarios_alvo = eventos_ataque['usuario'].unique()
    localizacao = eventos_ataque['localizacao'].iloc[0]
    tentativas = eventos_ataque['tentativas_intervalo'].mean()

    alerta = f"""
╔════════════════════════════════════════════════════════════════╗
║                    🚨 ALERTA DE SEGURANÇA 🚨                  ║
╚════════════════════════════════════════════════════════════════╝

IP ATACANTE: {ip}
LOCALIZAÇÃO: {localizacao}
TENTATIVAS DETECTADAS: {len(eventos_ataque)}
MÉDIA DE TENTATIVAS/INTERVALO: {tentativas:.1f}

USUÁRIOS ALVO:
{', '.join(usuarios_alvo)}

CONFIANÇA DA DETECÇÃO: {(len(eventos_ataque)/total_anomalias)*100:.1f}%

RECOMENDAÇÃO: ⛔ BLOQUEAR IP IMEDIATAMENTE

Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
════════════════════════════════════════════════════════════════
"""
    alertas.append(alerta)

# Salvar alertas em arquivo
with open('resultados/alertas.txt', 'w', encoding='utf-8') as f:
    f.write("🔐 RELATÓRIO DE ALERTAS DE FORÇA BRUTA\n")
    f.write(f"Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("=" * 70 + "\n\n")
    for alerta in alertas:
        f.write(alerta)

print(f"✅ {len(alertas)} alertas gerados e salvos em: resultados/alertas.txt")

# ========== GERAR RELATÓRIO DETALHADO ==========
print("\n📋 GERANDO RELATÓRIO DETALHADO...")

relatorio = f"""
╔════════════════════════════════════════════════════════════════╗
║         RELATÓRIO DE DETECÇÃO DE FORÇA BRUTA                  ║
║                   Machine Learning Analysis                   ║
╚════════════════════════════════════════════════════════════════╝

DATA DO RELATÓRIO: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

═══════════════════════════════════════════════════════════════════

📊 ESTATÍSTICAS GERAIS:

   • Total de eventos analisados: {len(df):,}
   • Período: {df['timestamp'].min()} até {df['timestamp'].max()}
   • IPs únicos: {df['ip'].nunique()}
   • Usuários únicos: {df['usuario'].nunique()}
   • Localizações: {df['localizacao'].nunique()}

═══════════════════════════════════════════════════════════════════

🚨 DETECÇÃO DE ATAQUES:

   • Eventos normais: {total_normais} ({100*total_normais/len(df):.2f}%)
   • Eventos anômalos: {total_anomalias} ({100*total_anomalias/len(df):.2f}%)
   • Taxa de detecção: {(total_anomalias/len(df))*100:.2f}%

═══════════════════════════════════════════════════════════════════

🔍 TOP 10 IPS MAIS SUSPEITOS:

"""

for idx, (ip, count) in enumerate(ips_suspeitos.head(10).items(), 1):
    localizacao = df[df['ip'] == ip]['localizacao'].iloc[0]
    risco = "🔴 CRÍTICO" if count > 50 else "🟠 ALTO" if count > 20 else "🟡 MÉDIO"
    relatorio += f"\n   {idx}. IP: {ip} | Tentativas: {count} | {risco} | Localização: {localizacao}"

relatorio += f"""

═══════════════════════════════════════════════════════════════════

✅ EVENTOS LEGÍTIMOS:

   • Taxa de sucesso: {(df[df['anomalia']==1]['sucesso'].sum() / total_normais * 100):.2f}%
   • Origem confiável: {(df[df['anomalia']==1]['origem_confiavel'].sum() / total_normais * 100):.2f}%

═══════════════════════════════════════════════════════════════════

🤖 MODELO UTILIZADO:

   • Algoritmo: Isolation Forest
   • Contaminação esperada: 5%
   • Estimadores: 100
   • Seed: 42 (reprodutível)

═══════════════════════════════════════════════════════════════════

💡 RECOMENDAÇÕES:

   1. ⛔ Bloquear imediatamente os IPs críticos
   2. 🔐 Implementar rate limiting (máx 5 tentativas/minuto)
   3. 📧 Notificar usuários sobre tentativas de acesso
   4. 🔍 Investigar padrões de ataque lento (mais sofisticados)
   5. 📊 Monitorar continuamente com este modelo

═══════════════════════════════════════════════════════════════════

Relatório gerado automaticamente pelo sistema de detecção de força bruta.
"""

with open('resultados/relatorio.txt', 'w', encoding='utf-8') as f:
    f.write(relatorio)

print("✅ Relatório detalhado salvo em: resultados/relatorio.txt")

# ========== SALVAR MODELO ==========
print("\n💾 Salvando modelo treinado...")
joblib.dump(modelo, 'modelos/modelo_deteccao.pkl')
joblib.dump(scaler, 'modelos/scaler.pkl')
print("✅ Modelo salvo em: modelos/modelo_deteccao.pkl")

# ========== GERAR GRÁFICOS ==========
print("\n📈 Gerando visualizações...")

# Configurar estilo
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (14, 10)

# Gráfico 1: Distribuição de anomalias
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Gráfico 1.1: Pie chart de anomalias
cores = ['#2ecc71', '#e74c3c']
axes[0, 0].pie([total_normais, total_anomalias], 
               labels=['Normal', 'Anômalo'], 
               autopct='%1.1f%%',
               colors=cores,
               startangle=90,
               textprops={'fontsize': 12, 'weight': 'bold'})
axes[0, 0].set_title('Distribuição de Eventos\n(Normal vs Anômalo)', fontsize=14, weight='bold')

# Gráfico 1.2: Top 10 IPs suspeitos
ips_suspeitos.head(10).plot(kind='barh', ax=axes[0, 1], color='#e74c3c')
axes[0, 1].set_title('Top 10 IPs Mais Suspeitos', fontsize=14, weight='bold')
axes[0, 1].set_xlabel('Número de Tentativas Anômalas', fontsize=11)
axes[0, 1].invert_yaxis()

# Gráfico 1.3: Anomalias por hora do dia
anomalias_hora = df[df['anomalia'] == -1]['hora'].value_counts().sort_index()
axes[1, 0].bar(anomalias_hora.index, anomalias_hora.values, color='#e74c3c', alpha=0.7)
axes[1, 0].set_title('Ataques por Hora do Dia', fontsize=14, weight='bold')
axes[1, 0].set_xlabel('Hora do Dia', fontsize=11)
axes[1, 0].set_ylabel('Quantidade de Ataques', fontsize=11)

# Gráfico 1.4: Score de anomalia
axes[1, 1].hist(df[df['anomalia'] == 1]['anomalia_score'], bins=50, alpha=0.7, label='Normal', color='#2ecc71')
axes[1, 1].hist(df[df['anomalia'] == -1]['anomalia_score'], bins=50, alpha=0.7, label='Anômalo', color='#e74c3c')
axes[1, 1].set_title('Distribuição de Scores de Anomalia', fontsize=14, weight='bold')
axes[1, 1].set_xlabel('Score de Anomalia', fontsize=11)
axes[1, 1].set_ylabel('Frequência', fontsize=11)
axes[1, 1].legend()

plt.tight_layout()
plt.savefig('resultados/analise_deteccao.png', dpi=300, bbox_inches='tight')
print("✅ Gráfico salvo em: resultados/analise_deteccao.png")

# Gráfico 2: Matriz de confusão visual
fig, ax = plt.subplots(figsize=(10, 6))

tentativas_por_ip = df.groupby('ip')['tentativas_intervalo'].mean()
anomalias_por_ip = df[df['anomalia'] == -1].groupby('ip').size()

dados_plot = pd.DataFrame({
    'Tentativas Médias': tentativas_por_ip,
    'Anomalias Detectadas': anomalias_por_ip
}).fillna(0).head(15)

dados_plot.plot(kind='barh', ax=ax, color=['#3498db', '#e74c3c'])
ax.set_title('Análise de Tentativas vs Anomalias por IP', fontsize=14, weight='bold')
ax.set_xlabel('Quantidade', fontsize=11)
plt.tight_layout()
plt.savefig('resultados/analise_ips.png', dpi=300, bbox_inches='tight')
print("✅ Gráfico salvo em: resultados/analise_ips.png")

# ========== RESUMO FINAL ==========
print("\n" + "=" * 70)
print("✅ ANÁLISE CONCLUÍDA COM SUCESSO!")
print("=" * 70)
print(f"\n📁 Arquivos gerados:")
print(f"   ✅ dados/logins_gerados.csv")
print(f"   ✅ modelos/modelo_deteccao.pkl")
print(f"   ✅ modelos/scaler.pkl")
print(f"   ✅ resultados/alertas.txt")
print(f"   ✅ resultados/relatorio.txt")
print(f"   ✅ resultados/analise_deteccao.png")
print(f"   ✅ resultados/analise_ips.png")
print(f"\n🎯 Próximos passos:")
print(f"   1. Revisar os alertas em: resultados/alertas.txt")
print(f"   2. Analisar o relatório em: resultados/relatorio.txt")
print(f"   3. Visualizar os gráficos em: resultados/")
print(f"   4. Usar o modelo salvo para novas predições")
print("\n" + "=" * 70)
