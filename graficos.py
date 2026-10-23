import plotly.express as px
from plotly.subplots import make_subplots
from bcb import Expectativas
# IPCA
from bcb import sgs
import yfinance as yf
import pandas as pd

# Consulta ao Banco Central: IPCA mensal (série SGS 433)
df = sgs.get({'IPCA': 433}, last=12)

df = df.reset_index()
df.columns = ['Data', 'IPCA']

# Gráfico de linhas
fig_ipca = px.line(
    df,
    x='Data',
    y='IPCA',
    title='IPCA mensal — Brasil (últimos 12 meses)',
    labels={
        'Data': 'Mês',
        'IPCA': 'Variação mensal (%)'
    },
    markers=True,
    color_discrete_sequence=['#10408D']
)

fig_ipca.update_layout(
    template='plotly_white',
    title_x=0,
    height=400,
    margin=dict(l=20, r=20, t=60, b=20),
    xaxis=dict(
        showgrid=False
    ),
    yaxis=dict(
        ticksuffix='%',
        showgrid=True,
        gridcolor='#E2EFF6',
        zeroline=False
    ),
    hovermode='x unified'
)

def obter_bovespa():
    df = yf.download(
        "^BVSP",
        period="1y",
        interval="1mo",
        auto_adjust=True,
        progress=False
    )

    if df.empty:
        raise ValueError("Não foi possível obter os dados do Ibovespa.")

    df = df.reset_index()

    # Trata as colunas caso o yfinance retorne MultiIndex
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df[["Date", "Close"]].dropna()
    df.columns = ["Data", "Ibovespa"]

    # Mantém os últimos 12 registros disponíveis
    return df.tail(12)


df_bovespa = obter_bovespa()

fig_bovespa = px.line(
    df_bovespa,
    x="Data",
    y="Ibovespa",
    title="Desempenho da Bolsa (Ibovespa)",
    labels={
        "Data": "",
        "Ibovespa": "Pontos"
    },
    markers=False,
    color_discrete_sequence=["#0BA678"]
)

fig_bovespa.update_layout(
    template="plotly_white",
    title_x=0,
    height=350,
    margin=dict(l=10, r=10, t=55, b=10),
    hovermode="x unified",
    showlegend=False,
    xaxis=dict(showgrid=False),
    yaxis=dict(
        showgrid=True,
        gridcolor="#E2EFF6",
        zeroline=False,
        tickformat=",.0f"
    )
)

fig_bovespa.update_traces(
    line=dict(width=2.5)
)