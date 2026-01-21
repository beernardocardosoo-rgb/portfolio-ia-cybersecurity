import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ============================================
# 1. GERAR DADOS DE EXEMPLO (Logs simulados)
# ============================================

np.random.seed(42)

# Comportamento NORMAL
logs_normais = {
    'timestamp': pd.date_range('2024-01-01', periods=800, freq='1min'),
    'tentativas_login': np.random.normal(5, 2, 800),
    'requisicoes_http': np.random.normal(100, 20, 800),
    'bytes_transferidos': np.random.normal(50000, 10000, 800),
    'tempo_resposta_ms': np.random.normal(200, 50, 800),
}

df_normal = pd.DataFrame(logs_normais)
df_normal['tipo'] = 'Normal'

# Comportamento ANÔMALO (ataques simulados)
logs_anomalos = {
    'timestamp': pd.date_range('2024-01-01 13:20', periods=50, freq='1min'),
    'tentativas_login': np.random.normal(50, 10, 50),
    'requisicoes_http': np.random.normal(500, 100, 50),
    'bytes_transferidos': np.random.normal(500000, 100000, 50),
    'tempo_resposta_ms': np.random.normal(5000, 1000, 50),
}

df_anomalo = pd.DataFrame(logs_anomalos)
df_anomalo['tipo'] = 'Anômalo'

# Combinar dados
df = pd.concat([df_normal, df_anomalo], ignore_index=True)
df = df.sort_values('timestamp').reset_index(drop=True)

# Salvar dados
df.to_csv('dados/logs_exemplo.csv', index=False)
print(f"✅ Dados gerados: {len(df)} registros")
print(f"   - Normais: {len(df_normal)}")
print(f"   - Anômalos: {len(df_anomalo)}\n")

# ============================================
# 2. PREPARAR DADOS PARA O MODELO
# ============================================

features = ['tentativas_login', 'requisicoes_http', 'bytes_transferidos', 'tempo_resposta_ms']
X = df[features].copy()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ============================================
# 3. TREINAR O MODELO (Isolation Forest)
# ============================================

modelo = IsolationForest(
    contamination=0.05,
    random_state=42,
    n_estimators=100
)

df['anomalia_pred'] = modelo.fit_predict(X_scaled)
df['anomalia_score'] = modelo.score_samples(X_scaled)

df['eh_anomalia'] = df['anomalia_pred'].apply(lambda x: 'Sim' if x == -1 else 'Não')

# ============================================
# 4. ANÁLISE DOS RESULTADOS
# ============================================

print("=" * 60)
print("📊 RESULTADOS DA DETECÇÃO DE ANOMALIAS")
print("=" * 60)

anomalias_detectadas = (df['anomalia_pred'] == -1).sum()
acuracia = (df['eh_anomalia'] == df['tipo'].apply(lambda x: 'Sim' if x == 'Anômalo' else 'Não')).sum() / len(df) * 100

print(f"\n🔍 Anomalias Detectadas: {anomalias_detectadas}")
print(f"✅ Acurácia do Modelo: {acuracia:.2f}%")
print(f"\n📈 Estatísticas das Features:")
print(df[features].describe())

print(f"\n🚨 Registros Anômalos Detectados:")
anomalias = df[df['anomalia_pred'] == -1][['timestamp', 'tentativas_login', 'requisicoes_http', 'bytes_transferidos', 'tempo_resposta_ms']]
print(anomalias.head(10))

# ============================================
# 5. SALVAR RESULTADOS
# ============================================

df.to_csv('dados/logs_com_anomalias.csv', index=False)
print(f"\n💾 Resultados salvos em 'logs_com_anomalias.csv'")

# ============================================
# 6. VISUALIZAÇÕES
# ============================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Detecção de Anomalias em Logs - Machine Learning', fontsize=16, fontweight='bold')

axes[0, 0].scatter(df.index, df['tentativas_login'], c=df['anomalia_pred'], cmap='RdYlGn_r', alpha=0.6)
axes[0, 0].set_title('Tentativas de Login ao Longo do Tempo')
axes[0, 0].set_xlabel('Índice de Registro')
axes[0, 0].set_ylabel('Tentativas')
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].scatter(df.index, df['requisicoes_http'], c=df['anomalia_pred'], cmap='RdYlGn_r', alpha=0.6)
axes[0, 1].set_title('Requisições HTTP ao Longo do Tempo')
axes[0, 1].set_xlabel('Índice de Registro')
axes[0, 1].set_ylabel('Requisições')
axes[0, 1].grid(True, alpha=0.3)

axes[1, 0].scatter(df.index, df['bytes_transferidos'], c=df['anomalia_pred'], cmap='RdYlGn_r', alpha=0.6)
axes[1, 0].set_title('Bytes Transferidos ao Longo do Tempo')
axes[1, 0].set_xlabel('Índice de Registro')
axes[1, 0].set_ylabel('Bytes')
axes[1, 0].grid(True, alpha=0.3)

axes[1, 1].scatter(df.index, df['tempo_resposta_ms'], c=df['anomalia_pred'], cmap='RdYlGn_r', alpha=0.6)
axes[1, 1].set_title('Tempo de Resposta ao Longo do Tempo')
axes[1, 1].set_xlabel('Índice de Registro')
axes[1, 1].set_ylabel('Tempo (ms)')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('visualizacoes_anomalias.png', dpi=300, bbox_inches='tight')
print(f"📊 Gráficos salvos em 'visualizacoes_anomalias.png'")
plt.show()

# ============================================
# 7. GRÁFICO DE DISTRIBUIÇÃO DE ANOMALIAS
# ============================================

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

contagem = df['eh_anomalia'].value_counts()
axes[0].bar(contagem.index, contagem.values, color=['#2ecc71', '#e74c3c'])
axes[0].set_title('Distribuição: Normal vs Anômalo', fontweight='bold')
axes[0].set_ylabel('Quantidade')
axes[0].grid(True, alpha=0.3, axis='y')

axes[1].hist(df['anomalia_score'], bins=50, color='#3498db', edgecolor='black', alpha=0.7)
axes[1].axvline(df[df['anomalia_pred'] == -1]['anomalia_score'].max(), color='red', linestyle='--', linewidth=2, label='Limiar de Anomalia')
axes[1].set_title('Distribuição de Anomaly Scores', fontweight='bold')
axes[1].set_xlabel('Anomaly Score')
axes[1].set_ylabel('Frequência')
axes[1].legend()
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('distribuicao_anomalias.png', dpi=300, bbox_inches='tight')
print(f"📊 Distribuição salva em 'distribuicao_anomalias.png'")
plt.show()

# ============================================
# 8. GERAR RELATÓRIO EXECUTIVO
# ============================================
with open('resultados/relatorio_anomalias.txt', 'w', encoding='utf-8') as f:
    f.write("=" * 60 + "\n")
    f.write("RELATÓRIO DE DETECÇÃO DE ANOMALIAS\n")
    f.write("=" * 60 + "\n\n")
    f.write(f"Total de registros analisados: {len(df)}\n")
    f.write(f"Anomalias detectadas: {anomalias_detectadas}\n")
    f.write(f"Taxa de anomalias: {(anomalias_detectadas/len(df))*100:.2f}%\n")
    f.write(f"Acurácia do modelo: {acuracia:.2f}%\n\n")
    f.write("Top 10 Anomalias Detectadas:\n")
    f.write(anomalias.head(10).to_string())

print("✓ Relatório salvo: resultados/relatorio_anomalias.txt")

# ============================================
# 9. ANÁLISE AVANÇADA COM IA
# ============================================
print("\n[9] Gerando análise avançada com IA (Mistral via Ollama)...")

from ia_anomalias import analisar_anomalias_com_llm

with open('resultados/relatorio_anomalias.txt', 'r', encoding='utf-8') as f:
    texto_base = f.read()

analise_ia = analisar_anomalias_com_llm(texto_base)

with open('resultados/relatorio_ia_avancado.txt', 'w', encoding='utf-8') as f:
    f.write(analise_ia)

print("✓ Análise IA salva: resultados/relatorio_ia_avancado.txt")


print("\n" + "=" * 60)
print("✅ PROJETO CONCLUÍDO COM SUCESSO!")
print("=" * 60)
