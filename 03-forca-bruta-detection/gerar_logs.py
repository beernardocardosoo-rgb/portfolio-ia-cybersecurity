import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configurações
np.random.seed(42)
random.seed(42)

# Parâmetros
TOTAL_EVENTOS = 10000
TAXA_ATAQUE_RAPIDO = 0.02  # 2% ataques rápidos
TAXA_ATAQUE_LENTO = 0.03   # 3% ataques lentos
TAXA_NORMAL = 0.95         # 95% tráfego normal

# IPs atacantes
IPS_ATAQUE_RAPIDO = [f"203.0.113.{i}" for i in range(10, 13)]  # 3 IPs
IPS_ATAQUE_LENTO = [f"198.51.100.{i}" for i in range(20, 25)]  # 5 IPs

# IPs legítimos
IPS_LEGITIMOS = [f"192.168.1.{i}" for i in range(1, 100)]

# Usuários
USUARIOS_COMUNS = ['alice', 'bob', 'carlos', 'diana', 'eduardo', 'fernanda']
USUARIOS_ALVO = ['admin', 'root', 'administrator', 'user', 'guest']

# Localizações
LOCALIZACOES_CONFIAVEIS = ['Brasil', 'Portugal', 'EUA', 'Canadá']
LOCALIZACOES_SUSPEITAS = ['Desconhecido', 'Tor Exit Node', 'VPN', 'Proxy']

print("🔄 Gerando dataset de tentativas de login...")

# Lista para armazenar eventos
eventos = []

# Data inicial
data_inicio = datetime.now() - timedelta(days=7)

# Contador de eventos por tipo
eventos_normais = int(TOTAL_EVENTOS * TAXA_NORMAL)
eventos_ataque_rapido = int(TOTAL_EVENTOS * TAXA_ATAQUE_RAPIDO)
eventos_ataque_lento = int(TOTAL_EVENTOS * TAXA_ATAQUE_LENTO)

print(f"📊 Distribuição:")
print(f"   Normal: {eventos_normais}")
print(f"   Ataque rápido: {eventos_ataque_rapido}")
print(f"   Ataque lento: {eventos_ataque_lento}")

# ========== GERAR TRÁFEGO NORMAL ==========
print("\n✅ Gerando tráfego normal...")
for i in range(eventos_normais):
    timestamp = data_inicio + timedelta(
        minutes=random.randint(0, 10080)  # 7 dias
    )

    ip = random.choice(IPS_LEGITIMOS)
    usuario = random.choice(USUARIOS_COMUNS)

    # 90% de sucesso no tráfego normal
    sucesso = 1 if random.random() < 0.9 else 0

    localizacao = random.choice(LOCALIZACOES_CONFIAVEIS)
    tentativas_intervalo = random.randint(1, 3)
    origem_confiavel = 1

    eventos.append({
        'timestamp': timestamp,
        'ip': ip,
        'usuario': usuario,
        'sucesso': sucesso,
        'localizacao': localizacao,
        'tentativas_intervalo': tentativas_intervalo,
        'origem_confiavel': origem_confiavel,
        'tipo': 'normal'
    })

# ========== GERAR ATAQUES RÁPIDOS ==========
print("🚨 Gerando ataques rápidos (força bruta alta velocidade)...")
for ip_atacante in IPS_ATAQUE_RAPIDO:
    # Cada IP faz múltiplas rajadas de ataque
    num_rajadas = eventos_ataque_rapido // len(IPS_ATAQUE_RAPIDO)

    for _ in range(num_rajadas):
        timestamp_base = data_inicio + timedelta(
            minutes=random.randint(0, 10080)
        )

        # Rajada de 50-200 tentativas em poucos segundos
        num_tentativas = random.randint(50, 200)

        for j in range(num_tentativas):
            timestamp = timestamp_base + timedelta(seconds=j * 0.5)
            usuario = random.choice(USUARIOS_ALVO)
            sucesso = 0  # Ataques falham
            localizacao = random.choice(LOCALIZACOES_SUSPEITAS)
            tentativas_intervalo = num_tentativas
            origem_confiavel = 0

            eventos.append({
                'timestamp': timestamp,
                'ip': ip_atacante,
                'usuario': usuario,
                'sucesso': sucesso,
                'localizacao': localizacao,
                'tentativas_intervalo': tentativas_intervalo,
                'origem_confiavel': origem_confiavel,
                'tipo': 'ataque_rapido'
            })

# ========== GERAR ATAQUES LENTOS (STEALTH) ==========
print("🕵️ Gerando ataques lentos (stealth)...")
for ip_atacante in IPS_ATAQUE_LENTO:
    num_tentativas = eventos_ataque_lento // len(IPS_ATAQUE_LENTO)

    timestamp_base = data_inicio + timedelta(
        minutes=random.randint(0, 10080)
    )

    for j in range(num_tentativas):
        # Espaçamento de 5-20 segundos entre tentativas
        timestamp = timestamp_base + timedelta(seconds=j * random.randint(5, 20))
        usuario = random.choice(USUARIOS_ALVO)
        sucesso = 0
        localizacao = random.choice(LOCALIZACOES_SUSPEITAS)
        tentativas_intervalo = random.randint(10, 30)
        origem_confiavel = 0

        eventos.append({
            'timestamp': timestamp,
            'ip': ip_atacante,
            'usuario': usuario,
            'sucesso': sucesso,
            'localizacao': localizacao,
            'tentativas_intervalo': tentativas_intervalo,
            'origem_confiavel': origem_confiavel,
            'tipo': 'ataque_lento'
        })

# ========== CRIAR DATAFRAME ==========
print("\n📦 Criando DataFrame...")
df = pd.DataFrame(eventos)

# Ordenar por timestamp
df = df.sort_values('timestamp').reset_index(drop=True)

# Salvar
caminho_saida = 'dados/logins_gerados.csv'
df.to_csv(caminho_saida, index=False)

print(f"\n✅ Dataset gerado com sucesso!")
print(f"📁 Arquivo salvo em: {caminho_saida}")
print(f"\n📊 Estatísticas:")
print(f"   Total de eventos: {len(df)}")
print(f"   Período: {df['timestamp'].min()} até {df['timestamp'].max()}")
print(f"\n🔍 Distribuição por tipo:")
print(df['tipo'].value_counts())
print(f"\n🌍 IPs únicos: {df['ip'].nunique()}")
print(f"👤 Usuários únicos: {df['usuario'].nunique()}")
print(f"\n✅ Pronto para treinar o modelo!")
