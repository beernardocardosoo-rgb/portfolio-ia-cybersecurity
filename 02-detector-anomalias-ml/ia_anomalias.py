import subprocess

def analisar_anomalias_com_llm(texto_relatorio):
    prompt = f"""
Você é um especialista em segurança de redes e detecção de anomalias.
Analise o relatório de anomalias abaixo e produza:

1. Identificação dos tipos de anomalias detectadas
2. Possíveis causas (ataque, falha de sistema, comportamento legítimo incomum)
3. Nível de risco de cada anomalia (baixo/médio/alto/crítico)
4. Indicadores de comprometimento (IoCs)
5. Ações imediatas recomendadas
6. Regras de firewall sugeridas (iptables / ufw)
7. Sugestões de monitoramento contínuo

Relatório:
{texto_relatorio}
"""

    comando = [
        r"C:\Users\Bernardo\AppData\Local\Programs\Ollama\ollama.exe",
        "run",
        "mistral"
    ]

    processo = subprocess.Popen(
        comando,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8',
        errors='replace'
    )

    saida, erro = processo.communicate(prompt)

    if erro:
        print("Aviso do modelo:", erro)

    return saida if saida else "Não foi possível gerar análise."
