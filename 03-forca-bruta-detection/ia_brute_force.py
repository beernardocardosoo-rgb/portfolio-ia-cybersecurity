import subprocess

def analisar_brute_force_com_llm(texto_relatorio):
    """
    Envia o relatório de força bruta para o Mistral (Ollama) e retorna análise avançada.
    """
    prompt = f"""
Você é um especialista em segurança cibernética e detecção de ataques de força bruta.
Analise o relatório de detecção abaixo e produza:

1. Resumo executivo dos ataques detectados
2. Classificação dos tipos de ataque (rápido, lento, distribuído)
3. Análise de risco de cada IP suspeito (baixo/médio/alto/crítico)
4. Indicadores de comprometimento (IoCs) identificados
5. Possíveis vetores de ataque e motivações
6. Ações imediatas recomendadas (bloqueio, monitoramento, investigação)
7. Regras de firewall sugeridas (iptables/ufw/fail2ban)
8. Recomendações de hardening do sistema de autenticação
9. Sugestões de monitoramento contínuo e alertas

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
        print("⚠️ Aviso do modelo:", erro)

    return saida if saida else "❌ Não foi possível gerar análise com IA."
