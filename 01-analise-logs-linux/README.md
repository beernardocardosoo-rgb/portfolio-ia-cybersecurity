🌐 Análise de Logs de Servidor Linux
📊 Projeto de Segurança + Análise de Dados

Este projeto realiza uma análise completa de logs de servidores Linux, com foco em segurança, detecção de comportamento anômalo e identificação de possíveis ataques. Ele combina análise exploratória, visualizações, geração de relatórios executivos e uma etapa adicional de análise avançada utilizando IA local (Mistral via Ollama).


🎯 Objetivos do Projeto
🔍 Analisar logs reais de servidores Linux
📉 Detectar padrões e horários suspeitos
🚫 Identificar tentativas de ataque e acessos indevidos
📊 Gerar gráficos e relatórios automáticos
📊 Produzir um relatório avançado usando IA generativa
🧠 Servir de base para projetos futuros de CyberSecurity + IA
🛠 Tecnologias Utilizadas
Tecnologia	Uso
🐍 Python 3.12	Linguagem principal
📚 Pandas	Manipulação de dados
📈 Matplotlib	Visualizações
🔎 Regex	Leitura estruturada dos logs
🧠 Ollama + Mistral — IA generativa local para análise avançada
💾 Git + GitHub	Versionamento
Exportar
Copiar
📂 Estrutura do Projeto
01-analise-logs-linux/
├── analise_logs.py — Script principal
├── ia_logs.py — Integração com IA (Ollama + Mistral)
├── logs_exemplo.txt — Logs usados nos testes
├── resultados/ — Gráficos e relatórios gerados automaticamente
│ ├── relatorio_completo.csv
│ ├── relatorio_seguranca.txt
│ ├── relatorio_ia_avancado.txt
│ ├── 01_sucessos_vs_falhas.png
│ ├── 02_top_ips_falhas.png
│ ├── 03_top_usuarios_atacados.png
│ └── 04_atividade_por_hora.png
├── requirements.txt
└── README.md

▶️ Como Executar
1. Clonar o repositório
git clone https://github.com/beernardocardosoo-rgb/01-analise-logs-linux.git
cd 01-analise-logs-linux

2. Instalar dependências
pip install -r requirements.txt

3. Instalar e configurar o Ollama
Ollama deve estar instalado.
Os modelos ficam no disco D (após configuração da variável OLLAMA_MODELS).

4. Baixar o modelo Mistral
ollama pull mistral

5. Rodar a análise
python analise_logs.py logs_exemplo.txt

📊 Resultados Visuais
🕒 Distribuição de Logs por Hora
Ajuda a identificar períodos com atividade incomum, como ataques de força bruta durante a madrugada.

Mostra horários com maior volume de eventos. Pode indicar rotinas agendadas ou ataques focados.

Tentativas de Login Falhas
Detecta padrões repetitivos que indicam ataques de brute force.

IPs mais Ativos e Suspeitos
Relatório com os IPs que mais tentaram acessar o servidor.

📉 Relatórios Gerados
• relatorio_completo.csv — Dados tabulares organizados
• relatorio_seguranca.txt — Análise tradicional e objetiva
• relatorio_ia_avancado.txt — Relatório criado por IA generativa
• 4 gráficos PNG com insights visuais

❌ Tentativas de Login Falhas

Útil para detectar força bruta ou acessos indevidos.

🔍 Principais Insights Encontrados
🚨 Picos de erros e falhas entre 02h e 04h
🌍 IPs repetidos com falhas de login → possível ataque
🕵️‍♂️ Mudança de padrão durante madrugada → comportamento anômalo
🔐 Muitos "authentication failure" de um mesmo host → força bruta
🤖 Próximos Passos (IA + CyberSecurity)
⚙️ Implementar Isolation Forest para detecção de anomalias
🧠 Criar classificador de eventos com NLP (BERT/spaCy)
📊 Dashboard interativo com Streamlit
📡 Envio de alertas via Telegram/Slack
🔥 Integrar logs de honeypot real (cowrie, sshd, fail2ban)
📬 Contato

Se quiser acompanhar ou colaborar com futuros projetos:

📧 beernardocardosoo@gmail.com