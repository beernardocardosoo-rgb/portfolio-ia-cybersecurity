import subprocess

def analisar_com_llm(texto_relatorio):
    prompt = f"""
Você é um especialista sênior em segurança ofensiva e defensiva.
Analise o relatório de logs abaixo e produza:

1. Identificação de possíveis ataques
2. Indicadores de comprometimento (IoCs)
3. Probabilidade dos ataques (baixa/média/alta)
4. Riscos para o servidor
5. Ações imediatas recomendadas
6. Regras de firewall sugeridas (iptables / ufw)
7. Sugestões adicionais de endurecimento (hardening)

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
