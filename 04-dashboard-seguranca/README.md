# 🛡️ Dashboard de Segurança

Dashboard web interativo para monitoramento de ameaças em tempo real, com detecção de força bruta usando Machine Learning.

## 🎯 Objetivo

Visualizar e monitorar tentativas de ataque de força bruta em tempo real, com gráficos dinâmicos, métricas de segurança e alertas automáticos.

## 🚀 Tecnologias

- **Python 3.12**
- **Streamlit** — Framework web para dashboards
- **Plotly** — Gráficos interativos
- **Pandas** — Manipulação de dados
- **Scikit-learn** — Machine Learning (modelo Isolation Forest)
- **Joblib** — Serialização de modelos

## 📋 Funcionalidades

✅ **Métricas em Tempo Real**
- Total de eventos monitorados
- Quantidade de ataques detectados
- Taxa de ataque (%)
- IPs únicos e suspeitos

✅ **Gráficos Interativos**
- Eventos por hora do dia
- Top 10 IPs mais suspeitos
- Distribuição de ataques por localização
- Taxa de sucesso vs falha

✅ **Alertas de Segurança**
- Exibição dos últimos 5 ataques detectados
- Confiança da detecção (%)
- Informações do IP, usuário e localização

✅ **Filtros Interativos**
- Filtro por data inicial e final
- Dados atualizados em tempo real

✅ **Tabelas Detalhadas**
- Últimos 10 eventos anômalos
- Resumo de IPs suspeitos

## 📁 Estrutura do Projeto

04-dashboard-seguranca/ ├── dados/ │ ├── logins_gerados.csv # Dataset de logins │ ├── modelo_deteccao.pkl # Modelo treinado │ └── scaler.pkl # Scaler para normalização ├── static/ ├── templates/ ├── app.py # Aplicação Streamlit ├── requirements.txt # Dependências ├── README.md # Este arquivo └── .gitignore

## 🔧 Instalação

### 1. Clonar o repositório

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-x6q4q692c" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span class="token" style="color:#7c00aa">git</span><span> clone https://github.com/seu-usuario/portfolio-ia-cybersecurity.git
</span><span></span><span class="token" style="color:#005a8e">cd</span><span> 04-dashboard-seguranca
</span></code></pre></div>

### 2. Instalar dependências

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-x6w8mgdmn" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>pip </span><span class="token" style="color:#7c00aa">install</span><span> </span><span class="token" style="color:#005a8e">-r</span><span> requirements.txt
</span></code></pre></div>

### 3. Rodar o dashboard

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-fj2upd1a1" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>streamlit run app.py
</span></code></pre></div>

O dashboard abrirá automaticamente em `http://localhost:8501`

## 📊 Como Funciona

1. **Carregamento de Dados**: O dashboard carrega o dataset de logins (`logins_gerados.csv`)
2. **Carregamento do Modelo**: Usa o modelo treinado (`modelo_deteccao.pkl`) para fazer predições
3. **Processamento**: Normaliza os dados com o scaler e faz predições em tempo real
4. **Visualização**: Exibe gráficos, métricas e alertas de forma interativa
5. **Filtros**: Permite filtrar por data para análise específica

## 🎨 Interface

- **Sidebar**: Filtros de data para análise customizada
- **Métricas**: 4 KPIs principais em cards coloridos
- **Gráficos**: 4 gráficos interativos (Plotly)
- **Alertas**: Exibição visual dos ataques detectados
- **Tabelas**: Dados detalhados em formato tabular

## 🔐 Modelo de Detecção

O dashboard utiliza um modelo **Isolation Forest** treinado no Projeto 03 (Força Bruta Detection) para identificar anomalias:

- **Algoritmo**: Isolation Forest (Scikit-learn)
- **Features**: Tentativas, origem confiável, sucesso, hora, dia da semana, IP, usuário, localização
- **Acurácia**: ~95% na detecção de ataques

## 📈 Métricas Monitoradas

- **Total de Eventos**: Quantidade total de tentativas de login
- **Ataques Detectados**: Número de anomalias identificadas
- **Taxa de Ataque**: Percentual de eventos suspeitos
- **IPs Suspeitos**: Quantidade de IPs únicos com comportamento anômalo

## 🚨 Alertas

O dashboard exibe os últimos 5 ataques detectados com:
- IP de origem
- Localização geográfica
- Usuário alvo
- Número de tentativas
- Timestamp do evento
- Confiança da detecção

## 🔄 Integração com Projeto 03

Este dashboard consome dados e modelos do **Projeto 03 - Força Bruta Detection**:
- Dataset: `../03-forca-bruta-detection/dados/logins_gerados.csv`
- Modelo: `../03-forca-bruta-detection/modelos/modelo_deteccao.pkl`
- Scaler: `../03-forca-bruta-detection/modelos/scaler.pkl`

## 📝 Próximas Melhorias

- [ ] Integração com banco de dados em tempo real
- [ ] Exportação de relatórios (PDF, CSV)
- [ ] Notificações por e-mail para alertas críticos
- [ ] Gráficos de tendências (7 dias, 30 dias)
- [ ] Autenticação de usuários
- [ ] Deploy em servidor (Heroku, AWS)

## 👨‍💻 Autor

**Bernardo Cardoso**  
- GitHub: [github.com/bernardocardosoo](https://github.com/bernardocardosoo)
- LinkedIn: [linkedin.com/in/bernardocardoso](https://linkedin.com/in/bernardocardoso)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

**Desenvolvido como parte do portfólio de IA & CyberSecurity** 🛡️