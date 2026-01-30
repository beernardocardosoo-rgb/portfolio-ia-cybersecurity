### 3. Priorização de alertas (03_priorization.ipynb)

Neste notebook eu uso o modelo treinado de Random Forest para transformar as previsões em uma fila de alertas priorizada, simulando o fluxo de trabalho de um analista de SOC.

Passos principais:
- Carrego o dataset de fluxo de rede (`Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv`) e recrio o alvo binário (`target = 1` para DDoS, `0` para BENIGN).
- Reaplico o mesmo pré-processamento da etapa de modelagem: seleção de features numéricas, tratamento de `inf`/NaN e uso do modelo salvo (`random_forest_ddos.pkl`) para calcular a probabilidade de cada fluxo ser DDoS (`ddos_proba`).
- Converto a probabilidade em níveis de prioridade:
  - `ALTA`: probabilidade ≥ 0.95  
  - `MÉDIA`: 0.70 ≤ probabilidade < 0.95  
  - `BAIXA`: probabilidade < 0.70  

Para deixar os resultados mais úteis para um contexto real de segurança, construo uma tabela de “alertas” com as seguintes colunas:
- Identificação do fluxo: `Flow ID`
- Contexto de rede: `Source IP`, `Destination IP`, `Source Port`, `Destination Port`, `Protocol`
- Informações de classificação: `ddos_proba` (probabilidade prevista) e `prioridade` (ALTA / MÉDIA / BAIXA)  
  > No dataset, também mantenho a coluna `Label` (BENIGN ou DDoS) apenas para validação. Em um cenário real, esse rótulo não estaria disponível.

Em seguida, ordeno essa tabela para formar uma fila de alertas:
- Primeiro pela prioridade (ALTA → MÉDIA → BAIXA)
- Depois pela probabilidade de DDoS (da maior para a menor)

Isso simula exatamente como um analista receberia os eventos em um painel de monitoramento: os ataques mais prováveis e mais críticos no topo.

#### Resultados da priorização

No resumo numérico, obtive:

- Distribuição geral por prioridade:
  - **ALTA**: 127.942 fluxos  
  - **MÉDIA**: 74 fluxos  
  - **BAIXA**: 97.729 fluxos  

- Fluxos DDoS reais por prioridade:
  - **ALTA**: 127.942 DDoS  
  - **MÉDIA**: 74 DDoS  
  - **BAIXA**: 11 DDoS  

- Fluxos BENIGN por prioridade:
  - **BAIXA**: 97.718 BENIGN  

- Taxa de acerto na prioridade ALTA:
  - **100%** dos alertas de prioridade ALTA são DDoS reais.  
  - Não há fluxos BENIGN classificados como ALTA.

Em termos de operação de segurança, isso significa que:
- A fila de **prioridade ALTA é extremamente confiável**: tudo que chega como ALTA é de fato ataque.
- O **tráfego benigno fica concentrado em prioridade BAIXA**, reduzindo ruído para o analista.
- A “zona cinza” (prioridade MÉDIA) é pequena e pode ser usada para investigação manual ou regras adicionais.

Esta etapa demonstra como um modelo de detecção de DDoS pode ser integrado a uma visão operacional, entregando não apenas uma classificação binária, mas uma **priorização de alertas** que ajuda o SOC a focar primeiro nos incidentes mais críticos.

### 4. Dashboard de priorização (Streamlit)

Além do notebook, criei um pequeno dashboard em Streamlit para visualizar a fila de alertas priorizados de forma interativa.

O fluxo fica assim:
1. O notebook `03_priorization.ipynb` gera o arquivo `data/ddos_alerts_prioritized.csv` com todos os fluxos, probabilidades e prioridades.
2. O arquivo `dashboard/app.py` carrega esse CSV, aplica filtros e exibe:
   - métricas de topo (total de alertas, quantos em ALTA, MÉDIA e BAIXA),
   - um gráfico com a distribuição por prioridade,
   - a tabela da fila de alertas ordenada por prioridade (ALTA → MÉDIA → BAIXA) e, dentro de cada nível, pela probabilidade de DDoS.

#### Como rodar o dashboard

Dentro da pasta `06-alert-prioritization`:

bash

ativar o ambiente virtual, se ainda não estiver ativo
.venv\Scripts\activate

rodar o dashboard
streamlit run dashboard/app.py

Depois, basta acessar o endereço mostrado no terminal (geralmente `http://localhost:8501`) para ver o painel web com a fila de alertas priorizada.

Esse dashboard simula como um SOC poderia consumir as saídas do modelo: usando o score de DDoS para organizar o trabalho do analista, começando pelos eventos de prioridade ALTA.