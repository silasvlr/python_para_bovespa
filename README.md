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
  - Eixo Y: Desvio Padrão da Variação Percentual nos últimos 365 dias.
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






