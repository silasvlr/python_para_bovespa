
import streamlit as st
import plotly.express as px
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Mensagem de alerta
mensagem='''Alerta!
As informações apresentadas  neste  informativo  têm caráter exclusivamente educacional
e visam promover o aprendizado sobre o mercado financeiro. Este conteúdo  não constitui
recomendação de investimento, oferta  ou solicitação  para compra ou venda de quaisquer
ativos financeiros. Reforçamos que as decisões de  investimento são de responsabilidade
exclusiva do investidor e devem ser  tomadas  com  base em sua análise individual e, se
necessário, com o auxílio de  um profissional  devidamente  registrado  na  Comissão de
Valores Mobiliários (CVM). A rentabilidade passada não é garantia de resultados futuros.'''


st.warning(mensagem)

data_atualizacao = datetime.today().strftime('%d/%m/%Y')  # Data atual formatada

# Exibir a data no topo da página
st.markdown(f"### Dados de preços atualizados em: {data_atualizacao}")


# Carregar os dados
acoes_filtradasgraf = pd.read_csv('https://drive.google.com/uc?id=1SJFgW5PbFbxwGgx-GG6dBq2-pS58IoSH')
acoes_filtradasgraf['dy'] = (acoes_filtradasgraf['dy'] * 100).round(2)
acoes_filtradasgraf['roe'] = (acoes_filtradasgraf['roe'] * 100).round(2)
acoes_filtradasgraf['variacao52Semanas'] = acoes_filtradasgraf['variacao52Semanas'].fillna(0)
acoes_filtradasgraf['desvioPadrao']=(acoes_filtradasgraf['desvioPadrao']).round(2)
acoes_filtradasgraf['variacao52Semanas']=(acoes_filtradasgraf['variacao52Semanas']*100).round(2)

#Calcula a diferença percentual entre o preço atual do ativo e a maior cotação em um ano.
def calcular_distancia_topo(ticker):
    try:
        ativo = yf.Ticker(ticker)
        preco_topo = ativo.fast_info.year_high
        preco_atual = ativo.fast_info.last_price
        return round(((preco_atual - preco_topo) / preco_atual) * 100, 2)
    except Exception as e:
        st.warning(f"Erro ao calcular distância para o topo de {ticker}: {e}")
        return None
#aplicação da função da distância para o maior preço
acoes_filtradasgraf['distanciaTopo'] = acoes_filtradasgraf['tickeryf'].apply(calcular_distancia_topo)


# Função para obter dados históricos
def obter_dados_historicos(ticker):
    try:
        data_fim = datetime.today()
        data_inicio = data_fim - timedelta(days=365)
        dados = yf.download(ticker, start=data_inicio.strftime("%Y-%m-%d"), end=data_fim.strftime("%Y-%m-%d"))
        dados['Fechamento'] = round(dados['Close'], 2)
        dados['Média 20 dias'] = round(dados['Fechamento'].rolling(window=20).mean(), 2)
        dados['Média 50 dias'] = round(dados['Fechamento'].rolling(window=50).mean(), 2)
        return dados
    except Exception as e:
        st.error(f"Erro ao obter dados para {ticker}: {e}")
        return None





# Interface do Streamlit
def main():
    st.markdown(
        "<h2 style='text-align: center; font-size: 20px;'>Gráfico de Bolhas: Valor Patrimonial vs. Distância do preço máximo % (Tamanho: Dividend Yield)</h2>",
        unsafe_allow_html=True
    )

    setor_selecionado = st.selectbox(
        "Selecione o setor:",
        options=acoes_filtradasgraf['Setor'].unique(),
        index=0
    )

    df_filtrado = acoes_filtradasgraf[acoes_filtradasgraf['Setor'] == setor_selecionado]

    if not df_filtrado.empty:
        fig = px.scatter(
            df_filtrado,
            x='pvp',
            y='distanciaTopo',
            size='dy',
            color='variacao52Semanas',
            color_continuous_scale=px.colors.sequential.RdBu, 
            color_continuous_midpoint=0.0,
            text='tickeryf',
            title=f"Ações do Setor: {setor_selecionado}",
            labels={
                'pvp': 'Preço sobre Valor Patrimonial',
                'distanciaTopo': 'Distância para o topo de 365 dias',
                'dy': 'Dividend Yield (%)',
                'variacao52Semanas': 'Variação das 52 semanas',
                'tickeryf':'Ticker'

            }
        )

        fig.update_traces(textposition='top center')

        fig.update_layout(
            xaxis_title='Preço sobre Valor Patrimonial',
            yaxis_title='Distância para o topo de 365 dias',
            template='plotly_dark',
            shapes=[
                dict(type='line', x0=0, x1=1, y0=0, y1=0, xref='paper', yref='y', line=dict(color='red', dash='dash'))
            ]
        )

        st.plotly_chart(fig)

        ticker_selecionado = st.selectbox(
            "Selecione uma ação para visualizar o desempenho:",
            options=df_filtrado['tickeryf'].unique()
        )

        if ticker_selecionado:
            dados_historicos = obter_dados_historicos(ticker_selecionado)
            if dados_historicos is not None:
                fig_variacao = px.line(
                    dados_historicos.reset_index(),
                    x='Date',
                    y=['Fechamento', 'Média 20 dias', 'Média 50 dias'],
                    title=f"Variação Cotação e Médias Móveis ({ticker_selecionado})",
                    labels={'value': 'Fechamento', 'Date': 'Data', 'variable': 'Indicadores'},

                    color_discrete_map={
                        'Fechamento': 'blue',
                        'Média 20 dias': 'green',
                        'Média 50 dias': 'red'
                    }
                )
                fig_variacao.update_traces(selector=dict(name='Variação %'), line=dict(width=1))  # Linha de variação mais espessa
                fig_variacao.update_traces(selector=dict(name='Média 20 dias'), line=dict(width=0.5))  # Linha mais fina
                fig_variacao.update_traces(selector=dict(name='Média 50 dias'), line=dict(width=0.8))  # Linha de espessura intermediária


                st.plotly_chart(fig_variacao)
    else:
        st.warning("Nenhuma ação encontrada para o setor selecionado.")
        
    st.markdown("---")
    st.markdown(
        """
        **Desenvolvido por [SILAS VALÉRIO](https://github.com/silasvlr).**  
        Contato: silas.vlr@gmail.com.
        """
    )


if __name__ == "__main__":
    main()
    
