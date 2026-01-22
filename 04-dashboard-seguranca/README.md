# 🛡️ Dashboard de Segurança  
Plataforma interativa em **Streamlit** para visualização, análise e monitoramento de ameaças usando técnicas de **Machine Learning** aplicadas aos Projetos 01, 02 e 03 do portfólio de IA & CyberSecurity.

O dashboard reúne modelos, análises e dados dos projetos:

- **Projeto 01 — Análise de Logs Linux**
- **Projeto 02 — Detector de Anomalias ML**
- **Projeto 03 — Força Bruta Detection (Isolation Forest)**

---

## 🎯 Objetivo

Oferecer uma visão centralizada e interativa das detecções de segurança geradas pelos projetos, facilitando:

- Análise estatística de logs de sistemas Linux
- Monitoramento de anomalias em logs de rede e sistemas
- Identificação de ataques de força bruta
- Visualização de padrões suspeitos
- Tomada de decisão rápida a partir de alertas e métricas

---

# 📁 Páginas do Dashboard

O dashboard contém **múltiplas páginas**, cada uma dedicada a um tipo de análise.

---

## 🐧 **1 — Análise de Logs Linux (Projeto 01)**  
Análise estatística e visual de logs de sistemas Linux (auth.log, syslog, etc).

### **Funcionalidades**
- Upload de arquivos de log
- Análise automática de padrões
- Identificação de eventos críticos
- Estatísticas de autenticação
- Detecção de IPs suspeitos
- Gráficos de atividade por horário
- Análise de comandos sudo
- Exportação de relatórios

### **Tipos de logs suportados**
- `/var/log/auth.log`
- `/var/log/syslog`
- `/var/log/kern.log`
- Logs customizados

---

## 🤖 **2 — Detector de Anomalias ML (Projeto 02)**  
Análise avançada de anomalias usando dados estatísticos e um score gerado por IA.

### **Funcionalidades**
- Filtros por data, tipo de log e score mínimo  
- Criação automática de anomalias (top 5% do score) caso o dataset não contenha  
- Métricas:
  - Total de logs
  - Total de anomalias
  - Score médio
  - Tipos afetados
- Gráficos interativos:
  - Timeline de anomalias
  - Distribuição de score
  - Anomalias por tipo
  - Heatmap de correlação
- Tabela detalhada dos logs
- Exportação de CSV filtrado

### **Dataset**
Carrega automaticamente:

02-detector-anomalias-ml/dados/logs_com_anomalias.csv

---

## 🔓 **3 — Força Bruta Detection (Projeto 03)**  
Integração com o modelo Isolation Forest do Projeto 03 para detectar tentativas de ataque por força bruta.

### **Funcionalidades**
- Análise em tempo real dos logins gerados
- KPIs de segurança:
  - Total de eventos
  - Ataques detectados
  - Taxa de ataque (%)
  - IPs suspeitos
- Gráficos:
  - Eventos por horário
  - IPs mais suspeitos
  - Localização dos ataques
  - Sucesso vs falha
- Últimos ataques detectados com nível de confiança
- Tabelas detalhadas

### **Integra dados e modelos:**
03-forca-bruta-detection/dados/logins_gerados.csv 03-forca-bruta-detection/modelos/modelo_deteccao.pkl 03-forca-bruta-detection/modelos/scaler.pkl

---

# 🚀 Tecnologias

- **Python 3.12**
- **Streamlit**
- **Plotly**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Joblib**
- **Matplotlib**
- **Seaborn**

---

# 📁 Estrutura do Projeto
04-dashboard-seguranca/ │ ├── pages/ │ ├── 1_🐧Analise_Logs_Linux.py # Página do Projeto 01 │ ├── 2🤖Detector_Anomalias.py # Página do Projeto 02 │ └── 3🔓_Forca_Bruta.py # Página do Projeto 03 │ ├── dados/ (opcional) ├── app.py ├── requirements.txt ├── README.md └── .gitignore

---

## 🔧 Instalação

### 1. Clonar o repositório

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-ukw49hm3j" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span class="token" style="color:#7c00aa">git</span><span> clone https://github.com/beernardocardoso/portfolio-ia-cybersecurity.git
</span><span></span><span class="token" style="color:#005a8e">cd</span><span> 04-dashboard-seguranca
</span></code></pre></div>

### 2. Instalar dependências

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-n8rxpsi4e" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>pip </span><span class="token" style="color:#7c00aa">install</span><span> </span><span class="token" style="color:#005a8e">-r</span><span> requirements.txt
</span></code></pre></div>

### 3. Rodar o Dashboard

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-9wnxzr0y3" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>streamlit run app.py
</span></code></pre></div>

Disponível em:
http://localhost:8501

---

# 📊 Como Funciona

### ✔️ Projeto 01  
Processa arquivos de log Linux, extrai padrões e gera visualizações estatísticas sobre autenticação, comandos e eventos do sistema.

### ✔️ Projeto 02  
Carrega logs e aplica detecção de anomalias baseada em score, incluindo automação de anomalias caso os dados não as contenham.

### ✔️ Projeto 03  
Executa normalização + modelo Isolation Forest para identificar ataques de força bruta.

---

# 🎨 Interface

- Sidebar com filtros inteligentes  
- KPIs em cards estilizados  
- Gráficos dinâmicos (Plotly)  
- Tabelas interativas  
- Upload de arquivos  
- Exportação de CSV e relatórios  
- Visual limpo e responsivo  

---

# 📝 Próximas Melhorias

- [ ] Página de overview unificada (todos os projetos)
- [ ] Relatórios PDF automáticos
- [ ] Sistema de alertas por e-mail
- [ ] Banco de dados em tempo real
- [ ] Deploy em nuvem
- [ ] Autenticação no dashboard
- [ ] Integração com SIEM

---

# 👨‍💻 Autor

**Bernardo Cardoso**

- GitHub: [github.com/beernardocardoso](https://github.com/beernardocardoso)  
- LinkedIn: [linkedin.com/in/bernardocardoso](https://linkedin.com/in/bernardocardoso)  

---

# 🛡️ Licença

Licença MIT — consulte o arquivo `LICENSE`.

---

**Desenvolvido como parte do portfólio de IA & CyberSecurity** 🛡️