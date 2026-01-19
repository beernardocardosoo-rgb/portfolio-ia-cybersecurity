# 🤖 Detector de Anomalias em Logs com Machine Learning

Projeto de **detecção de anomalias** em logs de servidor usando **Machine Learning** (Isolation Forest).

Combina **Inteligência Artificial** e **CyberSecurity** para identificar padrões suspeitos em dados de segurança.

---

## 🎯 Objetivo

Demonstrar como usar **Machine Learning** para detectar automaticamente:
- ✅ Tentativas de login suspeitas
- ✅ Picos anormais de requisições HTTP
- ✅ Transferências de dados fora do padrão
- ✅ Tempos de resposta anormais

---

## 📊 Como funciona

### 1. **Geração de Dados**
- 800 registros de comportamento **normal**
- 50 registros de comportamento **anômalo** (simulando ataques)
- Total: 850 registros de logs

### 2. **Treinamento do Modelo**
- Algoritmo: **Isolation Forest** (excelente para detecção de anomalias)
- Normalização dos dados com StandardScaler
- Treinamento não-supervisionado

### 3. **Detecção de Anomalias**
- Cada registro recebe um **score de anomalia**
- Registros com score baixo = anomalia
- Registros com score alto = comportamento normal

### 4. **Visualizações**
- Gráficos de dispersão mostrando anomalias detectadas
- Histograma de distribuição de anomaly scores
- Análise visual de cada métrica

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|-----------|-----|
| **Python** | Linguagem principal |
| **Pandas** | Manipulação de dados |
| **NumPy** | Operações numéricas |
| **Scikit-learn** | Machine Learning (Isolation Forest) |
| **Matplotlib** | Visualizações estáticas |
| **Seaborn** | Gráficos avançados |

---

## 📁 Estrutura do Projeto

02-detector-anomalias-ml/ ├── README.md # Este arquivo ├── requirements.txt # Dependências do projeto ├── detector_anomalias.py # Script principal ├── visualizacoes_anomalias.png # Gráfico 1 (4 subgráficos) ├── distribuicao_anomalias.png # Gráfico 2 (distribuição) └── dados/ ├── logs_exemplo.csv # Dados originais └── logs_com_anomalias.csv # Dados com predições

---

## 🚀 Como Usar

### 1. **Clonar o repositório**
<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-ln03yuq4r" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span class="token" style="color:#7c00aa">git</span><span> clone https://github.com/beernardocardosoo-rgb/portfolio-ia-cybersecurity.git
</span><span></span><span class="token" style="color:#005a8e">cd</span><span> portfolio-ia-cybersecurity/02-detector-anomalias-ml
</span></code></pre></div>

### 2. **Instalar dependências**
<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-ealjo5ld7" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>pip </span><span class="token" style="color:#7c00aa">install</span><span> </span><span class="token" style="color:#005a8e">-r</span><span> requirements.txt
</span></code></pre></div>

### 3. **Executar o script**
<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-jl6tadhfl" style="color:#111b27;background:#e3eaf2;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#111b27;background:none;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>python detector_anomalias.py
</span></code></pre></div>

### 4. **Visualizar resultados**
- Abra `visualizacoes_anomalias.png` para ver os 4 gráficos principais
- Abra `distribuicao_anomalias.png` para ver a distribuição de anomalias
- Abra `dados/logs_com_anomalias.csv` para analisar os dados com predições

---

## 📊 Resultados Esperados

Quando você executa o script, você verá:
✅ Dados gerados: 850 registros

Normais: 800
Anômalos: 50
============================================================

📊 RESULTADOS DA DETECÇÃO DE ANOMALIAS
🔍 Anomalias Detectadas: ~48-50 ✅ Acurácia do Modelo: ~98%

🚨 Registros Anômalos Detectados: (lista de registros suspeitos)

💾 Resultados salvos em 'logs_com_anomalias.csv' 📊 Gráficos salvos em PNG

---

## 🧠 Conceitos de Machine Learning Aplicados

### **Isolation Forest**
- Algoritmo não-supervisionado para detecção de anomalias
- Funciona isolando observações anômalas
- Excelente para dados de alta dimensionalidade
- Não precisa de dados rotulados para treinamento

### **Normalização (StandardScaler)**
- Coloca todas as features na mesma escala
- Importante para algoritmos baseados em distância
- Evita que features com valores maiores dominem o modelo

### **Anomaly Score**
- Valor entre -1 e 1
- Scores negativos = anomalias
- Scores positivos = comportamento normal

---

## 📈 Métricas Monitoradas

| Métrica | Descrição |
|---------|-----------|
| **Tentativas de Login** | Número de tentativas de acesso ao sistema |
| **Requisições HTTP** | Volume de requisições web |
| **Bytes Transferidos** | Quantidade de dados trafegando |
| **Tempo de Resposta** | Latência das respostas do servidor |

---

## 🎓 O que você aprende com este projeto

✅ Como gerar dados simulados para ML  
✅ Como treinar modelos de detecção de anomalias  
✅ Como normalizar dados para ML  
✅ Como visualizar resultados de forma profissional  
✅ Como trabalhar com Pandas e Scikit-learn  
✅ Como aplicar ML em problemas reais de segurança  

---

## 🔮 Próximas Melhorias

- [ ] Usar dados reais de logs (Apache, Nginx, etc)
- [ ] Adicionar mais features (IP, porta, protocolo, etc)
- [ ] Comparar com outros algoritmos (LOF, DBSCAN, etc)
- [ ] Criar dashboard interativo com Streamlit
- [ ] Adicionar alertas em tempo real
- [ ] Exportar relatórios em PDF

---

## 📝 Licença

Este projeto está sob a licença **MIT**.

---

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Abra uma **Issue** ou **Pull Request**.

---

**Desenvolvido com ❤️ por Bernardo Cardoso**  
*Projeto de Machine Learning + CyberSecurity*  
*Janeiro de 2026*
