# Seleção de Ações da Bovespa com Dados Fundamentalistas

Este projeto auxilia na seleção de ações negociadas na **Bovespa** com base em critérios fundamentalistas, utilizando Python, Streamlit e Google Colab.
O uso da linguagem acelera a análise de dados fundamentalistas, como margem de lucro, endividamento, liquidez, ROE dentre outros.

## ⚠️ Disclaimer

**Este projeto tem caráter estritamente educacional.**  
- As informações apresentadas não constituem recomendação de compra, venda ou manutenção de ativos financeiros.
- **Decisões de investimento são de total responsabilidade do usuário.**  
- Reforçamos a importância de consultar profissionais devidamente certificados, como analistas ou consultores de valores mobiliários registrados na Comissão de Valores Mobiliários (CVM), antes de realizar operações no mercado financeiro.

---


## 🚀 Funcionalidades

- 📈 **Gráfico de Bolhas**:
  - Eixo X: Preço sobre Valor Patrimonial (P/VP).
  - Eixo Y: Distância percentual para o topo (maior cotação) nos últimos 365 dias.
  - Tamanho da Bolha: Dividend Yield (%).
  - Cor: Baseada na Variação Percentual das 52 Semanas.

- 🔍 **Filtragem por Setor**: O usuário pode filtrar as ações por setor.
- 📊 **Gráficos de Variação e Médias Móveis**:
  - Exibe o desempenho percentual de uma ação específica.
  - Inclui Médias Móveis de 20 e 50 dias.
- ⚙️ **Automação de Dados**:
  - Coleta automática de informações do Yahoo Finance.
  - Integração com dados do Google Drive.

## 🛠️ Tecnologias Utilizadas
- **Google Colab**: Para execução do script e desenvolvimento.
- **Python**: Linguagem principal do projeto.
- **Fundamentus**: Biblioteca python com dados fundamentalistas sobre empresas brasileiras negociadas na bolsa
- - **Yahoo Finance API**: Para coleta de dados financeiros.
- **Streamlit**: Para criar a interface web interativa.
- **Plotly**: Para gráficos interativos.


## Filtragem e tratamento de dados - Fundamentus
-O dataframe obtido a partir da biblioteca Fundamentus foi filtrados pelos critérios abaixo, que podem ser utilizados de acordo com o critério próprio:
-**Patrimõnio líquido:**  maior que 0
-**Lucro líquido**: maior que 0
-**Dividend yiedl**: maior que 5% 
-**Retorno sobre patrimônio líquido**: maior que 20%

## Indicadores e informações adicionadas da Yahoo Finance
- Foram adicionados os seguintes indicadores ao dataframe obtido a partir da Fundamentus:
- Variação percentual em 52 semanas: **52WeekChange**
- Setor de atuação da empresa: **sector**
- Crescimento do lucro: **earningsGrowth**
- Lucro por ação: **trailingEps**

## Dados salvos em planilha
- Devido à dificuldade e a velocidade de obtenção de dados da Yahoo Finance, os dados obtidos foram salvos em em formado 'csv' e disponibilizados em pasta pública no Google Drive.
  Dessa forma, a filtragem dos dados fundamentalistas refletem o momento da geração do arquivo (12/2024) e deve ser repetida periodicamente.
  O endereço consta no script.


## 📋 Requisitos

Antes de começar, você precisará das seguintes dependências instaladas:

- `Python >= 3.7`
- Pacotes Python:
  
  - `streamlit`
  - `fundamentus`
  - `plotly`
  - `yfinance`
  - `pandas`
  - `numpy`

Para instalar, use:
```bash
pip install streamlit plotly yfinance pandas numpy pyngrok
pip install git+https://github.com/mv/fundamentus-api






