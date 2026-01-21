# 🔐 Detecção de Força Bruta com Machine Learning + IA

Projeto de **Inteligência Artificial** para identificar e classificar tentativas de ataque de força bruta em tempo real, usando **Machine Learning** (Isolation Forest) e **IA Generativa** (Mistral via Ollama).

Combina **análise estatística**, **detecção de anomalias** e **análise avançada com IA** para identificar padrões de ataque sofisticados.

---

## 🎯 Objetivo

Demonstrar como usar **Machine Learning + IA Generativa** para detectar automaticamente:

• Ataques de força bruta rápidos (alta velocidade)  
• Ataques de força bruta lentos (stealth)  
• Tentativas distribuídas de múltiplos IPs  
• Padrões anormais de autenticação  
• Análise avançada com IA (causas, riscos, recomendações)  

---

## 📊 Como Funciona

### 1. Geração de Dados Simulados

• 95% de tráfego **normal** (logins legítimos)  
• 2% de **ataques rápidos** (50-200 tentativas/segundo)  
• 3% de **ataques lentos** (10-30 tentativas espaçadas)  
• Total: 10.000+ eventos de login  

### 2. Treinamento do Modelo

• Algoritmo: **Isolation Forest** (detecção de anomalias)  
• Normalização com **StandardScaler**  
• Features: tentativas, origem, sucesso, hora, dia, IP, usuário, localização  

### 3. Detecção de Ataques

• Cada evento recebe um **score de anomalia**  
• Scores negativos = ataque detectado  
• Scores positivos = comportamento normal  

### 4. Análise Avançada com IA

• Relatório executivo em TXT  
• Análise com **Mistral (Ollama)** para interpretação inteligente  
• Identificação de causas, riscos, IoCs e recomendações  

### 5. Alertas e Relatórios

• Alertas automáticos para IPs suspeitos  
• Relatórios detalhados com estatísticas  
• Gráficos profissionais de análise  

---

## 🛠 Tecnologias Utilizadas

Python 3.12 — Linguagem principal  
Pandas — Manipulação de dados  
NumPy — Operações numéricas  
Scikit-learn — Machine Learning (Isolation Forest)  
Matplotlib — Visualizações estáticas  
Seaborn — Gráficos avançados  
Joblib — Serialização de modelos  
Ollama + Mistral — IA generativa local para análise avançada  

---

## 📁 Estrutura do Projeto

03-forca-bruta-detection/ ├── dados/ │ └── logins_gerados.csv # Dataset simulado ├── modelos/ │ ├── modelo_deteccao.pkl # Modelo treinado │ └── scaler.pkl # Normalizador ├── resultados/ │ ├── alertas.txt # Alertas de segurança │ ├── relatorio.txt # Relatório executivo │ ├── relatorio_ia_avancado.txt # Análise com IA (Mistral) │ ├── analise_deteccao.png # Gráfico 1 (4 subgráficos) │ └── analise_ips.png # Gráfico 2 (análise por IP) ├── gerar_logs.py # Gerador de dados ├── detector_forca_bruta.py # Script principal ├── ia_brute_force.py # Integração com Ollama + Mistral ├── requirements.txt # Dependências ├── .gitignore ├── LICENSE └── README.md

---

## 🚀 Como Usar

### 1. Instalar dependências

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-sw79x5jcz" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>pip </span><span class="token" style="color:#7c00aa">install</span><span> </span><span class="token" style="color:#005a8e">-r</span><span> requirements.txt
</span></code></pre></div>

### 2. Instalar e configurar o Ollama

Ollama deve estar instalado no seu sistema.  
Os modelos devem estar armazenados no disco D (após configuração da variável OLLAMA_MODELS).

### 3. Baixar o modelo Mistral

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-nyawzplko" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>ollama pull mistral
</span></code></pre></div>

### 4. Gerar dados simulados

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-7wpznrxu4" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>python gerar_logs.py
</span></code></pre></div>

Isso cria `dados/logins_gerados.csv` com 10.000+ eventos.

### 5. Treinar o modelo e detectar ataques

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-9gjpjukb9" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>python detector_forca_bruta.py
</span></code></pre></div>

---

## 📊 Resultados Gerados

Quando você executa o script, você verá:

✅ Dataset gerado: 10.000+ eventos  
✅ Ataques detectados: ~500-600  
✅ IPs suspeitos identificados  
✅ Alertas de segurança gerados  
✅ Relatório executivo em TXT  
✅ Análise avançada com IA em TXT  
✅ Gráficos profissionais em PNG  

### Arquivos Gerados

• **alertas.txt** — Alertas de segurança para IPs críticos  
• **relatorio.txt** — Resumo executivo com estatísticas  
• **relatorio_ia_avancado.txt** — Análise inteligente com Mistral  
• **analise_deteccao.png** — 4 gráficos de análise  
• **analise_ips.png** — Análise de tentativas por IP  
• **modelo_deteccao.pkl** — Modelo treinado  
• **scaler.pkl** — Normalizador  

---

## 🧠 Conceitos de Machine Learning Aplicados

### Isolation Forest

• Algoritmo não-supervisionado para detecção de anomalias  
• Funciona isolando observações anômalas  
• Excelente para dados de alta dimensionalidade  
• Não precisa de dados rotulados para treinamento  

### Normalização (StandardScaler)

• Coloca todas as features na mesma escala  
• Importante para algoritmos baseados em distância  
• Evita que features com valores maiores dominem o modelo  

### Anomaly Score

• Valor entre -1 e 1  
• Scores negativos = anomalias (ataques)  
• Scores positivos = comportamento normal  

---

## 📈 Features Monitoradas

Tentativas por Intervalo — Número de tentativas no último minuto  
Origem Confiável — IP/localização conhecida ou suspeita  
Sucesso — Login bem-sucedido ou falha  
Hora do Dia — Padrão temporal de acesso  
Dia da Semana — Comportamento semanal  
IP — Endereço de origem  
Usuário — Conta alvo  
Localização — País/região de origem  

---

## 🔗 Integração com Outros Projetos

Este projeto faz parte de um **ecosistema de CyberSecurity + IA**:

• **01-analise-logs-linux** — Análise exploratória de logs reais  
• **02-deteccao-anomalias-ia** — Detecção de anomalias em logs  
• **03-forca-bruta-detection** — Detecção de ataques brute-force (este projeto)  
• **04-dashboard-seguranca** — Dashboard unificado em tempo real  

---

## 🎓 O que Você Aprende

✅ Como gerar datasets realistas para ML  
✅ Como treinar modelos de detecção de anomalias  
✅ Como normalizar dados para ML  
✅ Como visualizar resultados de forma profissional  
✅ Como trabalhar com Pandas e Scikit-learn  
✅ Como integrar IA generativa em projetos de segurança  
✅ Como aplicar ML em problemas reais de CyberSecurity  
✅ Como detectar ataques sofisticados (stealth)  

---

## 🔮 Próximas Melhorias

• Usar dados reais de logs (SSH, FTP, HTTP)  
• Adicionar detecção de ataques distribuídos (DDoS)  
• Comparar com outros algoritmos (LOF, DBSCAN, Autoencoder)  
• Criar dashboard interativo com Streamlit/Plotly  
• Adicionar alertas em tempo real  
• Exportar relatórios em PDF  
• Integração com o Dashboard (Projeto 04)  
• Implementar fail2ban automático  

---

## 📝 Licença

Este projeto está sob a licença **MIT**.

---

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Abra uma **Issue** ou **Pull Request**.

---

**Desenvolvido com ❤️ por Bernardo Cardoso**  
*Machine Learning + CyberSecurity + IA Generativa*  
*Janeiro de 2026*