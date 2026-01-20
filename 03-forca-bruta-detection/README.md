# 🔐 Detecção de Força Bruta com Machine Learning

Projeto de **Inteligência Artificial** para identificar e classificar tentativas de ataque de força bruta em tempo real, usando análise estatística e modelos de machine learning.

---

## 📋 Descrição

Este projeto simula um ambiente real de autenticação com múltiplos tipos de tentativas de login:

- ✅ **Logins legítimos** — usuários normais acessando o sistema
- ⚠️ **Falhas acidentais** — erros de digitação, senhas esquecidas
- 🚨 **Ataques de força bruta** — tentativas automatizadas para quebrar senhas

O modelo de IA **detecta e classifica** esses padrões com alta precisão, permitindo:

- Identificação de IPs suspeitos
- Alertas em tempo real
- Relatórios de segurança detalhados
- Visualizações dos ataques detectados

---

## 🎯 Objetivos

1. **Gerar dataset realista** com 10.000+ eventos de login
2. **Treinar modelo de IA** para detectar força bruta
3. **Avaliar performance** com métricas estatísticas
4. **Gerar alertas e relatórios** automáticos
5. **Visualizar padrões** de ataque

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** — manipulação de dados
- **Scikit-learn** — machine learning
- **NumPy** — operações numéricas
- **Matplotlib & Seaborn** — visualizações
- **Joblib** — serialização de modelos

---

## 📂 Estrutura do Projeto

03-forca-bruta-detection/ ├── dados/ │ └── logins_gerados.csv # Dataset simulado ├── modelos/ │ └── modelo_deteccao.pkl # Modelo treinado ├── resultados/ │ ├── alertas.txt # Alertas gerados │ ├── relatorio.txt # Relatório detalhado │ └── graficos/ # Visualizações ├── gerar_logs.py # Script para gerar dados ├── detector_forca_bruta.py # Modelo e detecção ├── requirements.txt # Dependências ├── README.md # Este arquivo ├── LICENSE # Licença MIT └── .gitignore # Arquivos ignorados

---

## 🚀 Como Usar

### 1. Instalar dependências

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-hiigkqjpg" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>pip </span><span class="token" style="color:#7c00aa">install</span><span> </span><span class="token" style="color:#005a8e">-r</span><span> requirements.txt
</span></code></pre></div>

### 2. Gerar dados simulados

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-uyzumhasb" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>python gerar_logs.py
</span></code></pre></div>

Isso cria `dados/logins_gerados.csv` com 10.000 eventos.

### 3. Treinar o modelo e detectar ataques

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-14zquolx8" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>python detector_forca_bruta.py
</span></code></pre></div>

Isso:
- Treina o modelo de IA
- Detecta ataques de força bruta
- Gera alertas em `resultados/alertas.txt`
- Cria gráficos em `resultados/`

---

## 📊 Dataset

O arquivo `logins_gerados.csv` contém:

| Coluna | Descrição |
|--------|-----------|
| `timestamp` | Data e hora do login |
| `ip` | Endereço IP da tentativa |
| `usuario` | Nome do usuário |
| `sucesso` | 1 = sucesso, 0 = falha |
| `localizacao` | País/região da origem |
| `tentativas_intervalo` | Tentativas no último minuto |
| `origem_confiavel` | 1 = confiável, 0 = suspeita |

---

## 🤖 Modelo de IA

Usamos **Isolation Forest** para detectar anomalias:

- ✅ Identifica padrões anormais
- ✅ Funciona bem com dados desbalanceados
- ✅ Rápido e eficiente
- ✅ Interpretável

---

## 📈 Resultados Esperados

Após rodar o detector, você terá:

1. **Alertas de força bruta** — IPs e horários dos ataques
2. **Relatório de segurança** — estatísticas e análise
3. **Gráficos** — visualização dos padrões
4. **Modelo salvo** — para usar em produção

---

## 📝 Exemplo de Saída
[ALERTA] Força Bruta Detectada! IP: 192.168.1.100 Tentativas: 1000 em 5 minutos Usuários alvo: admin, root, user Confiança: 99.2% Ação recomendada: Bloquear IP imediatamente

---

## 📚 Conceitos Abordados

- ✅ Análise estatística de dados
- ✅ Machine Learning para detecção de anomalias
- ✅ Tratamento de dados desbalanceados
- ✅ Validação cruzada e métricas
- ✅ Visualização de dados
- ✅ Segurança cibernética

---

## 🔒 Segurança

Este projeto é **educacional** e demonstra técnicas reais de detecção de ataques. Use responsavelmente!

---

## 📄 Licença

MIT License — veja o arquivo `LICENSE` para detalhes.

---

## 👤 Autor

**Bernardo Cardoso**

- GitHub: [github.com/beernardocardosoo-rgb](https://github.com/beernardocardosoo-rgb)
- LinkedIn: [linkedin.com/in/bernardo-cardoso-31384734b](https://www.linkedin.com/in/bernardo-cardoso-31384734b/)

---

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Abra uma issue ou pull request.

---

**Desenvolvido com ❤️ para segurança cibernética**