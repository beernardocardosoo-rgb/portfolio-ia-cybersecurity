import re
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

print("=" * 60)
print("ANÁLISE DE LOGS DE SERVIDOR LINUX")
print("=" * 60)

# 1. LER O ARQUIVO DE LOGS
print("\n[1] Lendo arquivo de logs...")
try:
    with open("logs_exemplo.txt", "r") as file:
        linhas = file.readlines()
    print(f"✓ {len(linhas)} linhas de log lidas com sucesso!")
except FileNotFoundError:
    print("✗ Erro: arquivo 'logs_exemplo.txt' não encontrado!")
    exit()

# 2. EXTRAIR DADOS DOS LOGS
print("\n[2] Extraindo dados dos logs...")

datas = []
horas = []
ips = []
usuarios = []
eventos = []
status = []

# Padrão regex para capturar informações
# Exemplo: Jan 15 08:23:45 servidor-web sshd[12453]: Failed password for invalid user admin from 203.0.113.45 port 54321 ssh2

for linha in linhas:
    # Extrair data e hora
    match_data = re.search(r"(\w{3}\s+\d+)\s+(\d+:\d+:\d+)", linha)
    if match_data:
        datas.append(match_data.group(1))
        horas.append(match_data.group(2))

    # Extrair IP
    match_ip = re.search(r"from\s+(\d+\.\d+\.\d+\.\d+)", linha)
    if match_ip:
        ips.append(match_ip.group(1))
    else:
        ips.append("N/A")

    # Extrair usuário
    match_user = re.search(r"(?:for|user)\s+(\w+)\s+", linha)
    if match_user:
        usuarios.append(match_user.group(1))
    else:
        usuarios.append("N/A")

    # Classificar evento (sucesso ou falha)
    if "Accepted password" in linha:
        eventos.append("Login Bem-sucedido")
        status.append("SUCESSO")
    elif "Failed password" in linha:
        eventos.append("Falha de Login")
        status.append("FALHA")
    else:
        eventos.append("Outro")
        status.append("OUTRO")

print(f"✓ Dados extraídos com sucesso!")

# 3. CRIAR DATAFRAME
print("\n[3] Organizando dados em tabela...")
df = pd.DataFrame({
    "data": datas,
    "hora": horas,
    "ip": ips,
    "usuario": usuarios,
    "evento": eventos,
    "status": status
})

print(f"✓ Tabela criada com {len(df)} registros!")

# 4. ANÁLISES E ESTATÍSTICAS
print("\n[4] Realizando análises...")

# Contar sucessos e falhas
total_sucessos = len(df[df["status"] == "SUCESSO"])
total_falhas = len(df[df["status"] == "FALHA"])
total_eventos = len(df)

print(f"\n   Total de eventos: {total_eventos}")
print(f"   ✓ Logins bem-sucedidos: {total_sucessos}")
print(f"   ✗ Falhas de login: {total_falhas}")

# IPs com mais tentativas falhadas
print("\n   Top 5 IPs com falhas de login:")
ips_falhas = df[df["status"] == "FALHA"]["ip"].value_counts().head(5)
for i, (ip, count) in enumerate(ips_falhas.items(), 1):
    print(f"   {i}. {ip}: {count} tentativas")

# Usuários mais atacados
print("\n   Top 5 usuários mais atacados:")
usuarios_atacados = df[df["status"] == "FALHA"]["usuario"].value_counts().head(5)
for i, (user, count) in enumerate(usuarios_atacados.items(), 1):
    print(f"   {i}. {user}: {count} tentativas")

# 5. SALVAR RELATÓRIO EM CSV
print("\n[5] Salvando relatório em CSV...")
df.to_csv("resultados/relatorio_completo.csv", index=False)
print("✓ Arquivo salvo: resultados/relatorio_completo.csv")

# 6. CRIAR GRÁFICOS
print("\n[6] Gerando gráficos...")

# Gráfico 1: Sucessos vs Falhas
plt.figure(figsize=(10, 6))
status_counts = df["status"].value_counts()
cores = ["#2ecc71", "#e74c3c", "#95a5a6"]
plt.bar(status_counts.index, status_counts.values, color=cores[:len(status_counts)])
plt.title("Distribuição de Eventos: Sucessos vs Falhas", fontsize=14, fontweight="bold")
plt.xlabel("Status", fontsize=12)
plt.ylabel("Quantidade", fontsize=12)
plt.grid(axis="y", alpha=0.3)
for i, v in enumerate(status_counts.values):
    plt.text(i, v + 0.5, str(v), ha="center", fontweight="bold")
plt.tight_layout()
plt.savefig("resultados/01_sucessos_vs_falhas.png", dpi=300, bbox_inches="tight")
plt.close()
print("✓ Gráfico salvo: resultados/01_sucessos_vs_falhas.png")

# Gráfico 2: Top 10 IPs com falhas
plt.figure(figsize=(12, 6))
ips_falhas_top10 = df[df["status"] == "FALHA"]["ip"].value_counts().head(10)
plt.barh(range(len(ips_falhas_top10)), ips_falhas_top10.values, color="#e74c3c")
plt.yticks(range(len(ips_falhas_top10)), ips_falhas_top10.index)
plt.title("Top 10 IPs com Tentativas de Login Falhadas", fontsize=14, fontweight="bold")
plt.xlabel("Quantidade de Tentativas", fontsize=12)
plt.ylabel("Endereço IP", fontsize=12)
plt.grid(axis="x", alpha=0.3)
for i, v in enumerate(ips_falhas_top10.values):
    plt.text(v + 0.1, i, str(v), va="center", fontweight="bold")
plt.tight_layout()
plt.savefig("resultados/02_top_ips_falhas.png", dpi=300, bbox_inches="tight")
plt.close()
print("✓ Gráfico salvo: resultados/02_top_ips_falhas.png")

# Gráfico 3: Usuários mais atacados
plt.figure(figsize=(12, 6))
usuarios_top10 = df[df["status"] == "FALHA"]["usuario"].value_counts().head(10)
plt.barh(range(len(usuarios_top10)), usuarios_top10.values, color="#f39c12")
plt.yticks(range(len(usuarios_top10)), usuarios_top10.index)
plt.title("Top 10 Usuários Mais Atacados", fontsize=14, fontweight="bold")
plt.xlabel("Quantidade de Tentativas", fontsize=12)
plt.ylabel("Nome do Usuário", fontsize=12)
plt.grid(axis="x", alpha=0.3)
for i, v in enumerate(usuarios_top10.values):
    plt.text(v + 0.1, i, str(v), va="center", fontweight="bold")
plt.tight_layout()
plt.savefig("resultados/03_top_usuarios_atacados.png", dpi=300, bbox_inches="tight")
plt.close()
print("✓ Gráfico salvo: resultados/03_top_usuarios_atacados.png")

# Gráfico 4: Distribuição por hora do dia
plt.figure(figsize=(14, 6))
horas_count = df["hora"].value_counts().sort_index()
plt.plot(horas_count.index, horas_count.values, marker="o", linewidth=2, markersize=8, color="#3498db")
plt.fill_between(range(len(horas_count)), horas_count.values, alpha=0.3, color="#3498db")
plt.title("Atividade de Login por Hora do Dia", fontsize=14, fontweight="bold")
plt.xlabel("Hora", fontsize=12)
plt.ylabel("Quantidade de Eventos", fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("resultados/04_atividade_por_hora.png", dpi=300, bbox_inches="tight")
plt.close()
print("✓ Gráfico salvo: resultados/04_atividade_por_hora.png")

# 7. CRIAR RELATÓRIO EM TEXTO
print("\n[7] Gerando relatório em texto...")

relatorio = f"""
{'='*70}
RELATÓRIO DE ANÁLISE DE LOGS DE SEGURANÇA
{'='*70}

DATA DA ANÁLISE: {pd.Timestamp.now().strftime('%d/%m/%Y %H:%M:%S')}

{'='*70}
RESUMO EXECUTIVO
{'='*70}

Total de eventos analisados: {total_eventos}
Logins bem-sucedidos: {total_sucessos} ({total_sucessos/total_eventos*100:.1f}%)
Falhas de login: {total_falhas} ({total_falhas/total_eventos*100:.1f}%)

{'='*70}
TOP 10 IPs COM FALHAS DE LOGIN (SUSPEITOS)
{'='*70}

"""

for i, (ip, count) in enumerate(df[df["status"] == "FALHA"]["ip"].value_counts().head(10).items(), 1):
    relatorio += f"{i:2d}. {ip:20s} - {count:3d} tentativas\n"

relatorio += f"""
{'='*70}
TOP 10 USUÁRIOS MAIS ATACADOS
{'='*70}

"""

for i, (user, count) in enumerate(df[df["status"] == "FALHA"]["usuario"].value_counts().head(10).items(), 1):
    relatorio += f"{i:2d}. {user:20s} - {count:3d} tentativas\n"

relatorio += f"""
{'='*70}
RECOMENDAÇÕES DE SEGURANÇA
{'='*70}

1. BLOQUEIO DE IPs SUSPEITOS:
   Os IPs abaixo tiveram múltiplas tentativas falhadas e devem ser
   investigados e potencialmente bloqueados:
"""

for ip, count in df[df["status"] == "FALHA"]["ip"].value_counts().head(5).items():
    relatorio += f"   - {ip} ({count} tentativas)\n"

relatorio += f"""
2. PROTEÇÃO DE CONTAS:
   Os seguintes usuários foram alvo de ataques de força bruta:
"""

for user, count in df[df["status"] == "FALHA"]["usuario"].value_counts().head(5).items():
    relatorio += f"   - {user} ({count} tentativas)\n"

relatorio += f"""
3. AÇÕES RECOMENDADAS:
   ✓ Implementar rate limiting (limite de tentativas)
   ✓ Usar autenticação de dois fatores (2FA)
   ✓ Mudar portas padrão do SSH (porta 22)
   ✓ Desabilitar login de root via SSH
   ✓ Monitorar continuamente os logs
   ✓ Bloquear IPs com múltiplas falhas

{'='*70}
FIM DO RELATÓRIO
{'='*70}
"""

with open("resultados/relatorio_seguranca.txt", "w", encoding="utf-8") as f:
    f.write(relatorio)


print("✓ Arquivo salvo: resultados/relatorio_seguranca.txt")

# 8. MENSAGEM FINAL
print("\n" + "="*60)
print("✓ ANÁLISE CONCLUÍDA COM SUCESSO!")
print("="*60)
print("\nArquivos gerados na pasta 'resultados/':")
print("  1. relatorio_completo.csv - Dados em formato tabular")
print("  2. relatorio_seguranca.txt - Relatório executivo")
print("  3. 01_sucessos_vs_falhas.png - Gráfico de distribuição")
print("  4. 02_top_ips_falhas.png - IPs suspeitos")
print("  5. 03_top_usuarios_atacados.png - Usuários atacados")
print("  6. 04_atividade_por_hora.png - Atividade temporal")
print("\n" + "="*60)
