🌐 Análise de Logs de Servidor Linux
📊 Projeto de Segurança + Análise de Dados

Este projeto realiza análise exploratória de logs de servidores Linux, identificando falhas de login, IPs suspeitos, padrões de horário, e comportamentos que podem indicar atividade maliciosa.


🎯 Objetivos do Projeto
🔍 Analisar logs reais de servidores Linux
📉 Detectar padrões e horários suspeitos
🚫 Identificar tentativas de ataque
📊 Gerar gráficos e relatórios
🧠 Servir de base para integração com IA (anomalias / NLP)
🛠 Tecnologias Utilizadas
Tecnologia	Uso
🐍 Python 3.12	Linguagem principal
📚 Pandas	Manipulação de dados
📈 Matplotlib	Visualizações
🔎 Regex	Leitura estruturada dos logs
💾 Git + GitHub	Versionamento
Exportar
Copiar
📂 Estrutura do Projeto
01-analise-logs-linux/
├── analise_logs.py          # Script principal
├── logs_exemplo.txt         # Logs usados no teste
├── figures/
│   ├── logs_por_hora.png
│   └── falhas_login.png
├── summary.txt              # Resumo gerado automaticamente
├── requirements.txt         # Dependências
└── README.md

▶️ Como Executar
1. Clonar o repositório
git clone https://github.com/beernardocardosoo-rgb/01-analise-logs-linux.git
cd 01-analise-logs-linux

2. Instalar dependências
pip install -r requirements.txt

3. Rodar a análise
python analise_logs.py logs_exemplo.txt

📊 Resultados Visuais
🕒 Distribuição de Logs por Hora

Mostra horários com maior volume de eventos. Pode indicar rotinas agendadas ou ataques focados.

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