
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

def definir_cor(variacao):
    if variacao < 0:
        return "red"  # Vermelho para valores abaixo de 0
    elif 0 <= variacao <= 8:
        return "white"  # Branco para valores entre 0 e 8
    elif 10 <= variacao <= 20:
        return "green"  # Verde para valores entre 10 e 20
    elif variacao > 20:
        return "blue"  # Azul para valores acima de 20
    else:
        return "gray"  # Cor padrão para valores fora dos intervalos (caso não esperado)


# Carregar os dados
acoes_filtradasgraf = pd.read_csv('https://drive.google.com/uc?id=1SJFgW5PbFbxwGgx-GG6dBq2-pS58IoSH')
acoes_filtradasgraf['dy'] = (acoes_filtradasgraf['dy'] * 100).round(2)
acoes_filtradasgraf['roe'] = (acoes_filtradasgraf['roe'] * 100).round(2)
acoes_filtradasgraf['variacao52Semanas'] = acoes_filtradasgraf['variacao52Semanas'].fillna(0)
acoes_filtradasgraf['desvioPadrao']=(acoes_filtradasgraf['desvioPadrao']).round(2)
acoes_filtradasgraf['variacao52Semanas']=(acoes_filtradasgraf['variacao52Semanas']*100).round(2)
acoes_filtradasgraf['cor_variacao']=acoes_filtradasgraf['variacao52Semanas'].apply(definir_cor)

# Função para obter dados históricos
def obter_dados_historicos(ticker):
    try:
        data_fim = datetime.today()
        data_inicio = data_fim - timedelta(days=365)
        dados = yf.download(ticker, start=data_inicio.strftime("%Y-%m-%d"), end=data_fim.strftime("%Y-%m-%d"))
        dados['Variação %'] = ((dados['Close'] / dados['Close'].iloc[0] - 1) * 100).round(2)
        dados['Média 20 dias'] = dados['Variação %'].rolling(window=20).mean()
        dados['Média 50 dias'] = dados['Variação %'].rolling(window=50).mean()
        return dados
    except Exception as e:
        st.error(f"Erro ao obter dados para {ticker}: {e}")
        return None





# Interface do Streamlit
def main():
    st.title("Gráfico de Bolhas: Valor Patrimonial vs. Desvio Padrão Variação % (Tamanho: Dividend Yield)")

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
            y='desvioPadrao',
            size='dy',
            color='variacao52Semanas',
            color_continuous_scale=[
                [0, "red"],    # Vermelho para valores baixos
                [0.2, "white"], # Branco para valores entre 0 e 8
                [0.6, "green"], # Verde para valores entre 10 e 20
                [1, "blue"]    # Azul para valores altos
            ],
            text='tickeryf',
            title=f"Ações do Setor: {setor_selecionado}",
            labels={
                'pvp': 'Preço sobre Valor Patrimonial',
                'desvioPadrao': 'Desvio padrão variação % 365 dias',
                'dy': 'Dividend Yield (%)',
                'variacao52Semanas': 'Varição das 52 semanas'
            },

        )

        fig.update_traces(textposition='top center')
        fig.update_layout(
            xaxis_title='Preço sobre Valor Patrimonial',
            yaxis_title='Desvio padrão variação % de 365 dias',
            template='plotly_dark'

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
                    y=['Variação %', 'Média 20 dias', 'Média 50 dias'],
                    title=f"Variação Percentual e Médias Móveis ({ticker_selecionado}) - {acoes_filtradasgraf[acoes_filtradasgraf['tickeryf']==ticker_selecionado]['Empresa'].values[0]}",
                    labels={'value': 'Percentual (%)', 'Date': 'Data'},
                    color_discrete_map={
                        'Variação %': 'blue',
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
    
