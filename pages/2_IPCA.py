import streamlit as st
import pandas as pd
import plotly.express as px
from bcb import sgs

from utils import PALETA_AZUL, ESTILIZACAO1, SIDE_STYLE, SIDE_FOOTER


# --------------------------------------------------
# Configuração da página
# --------------------------------------------------
st.set_page_config(
    page_title="IPCA Mensal",
    page_icon="📈",
    layout="wide"
)

st.markdown(ESTILIZACAO1, unsafe_allow_html=True)

with st.sidebar:
    st.markdown(SIDE_STYLE, unsafe_allow_html=True)
    st.page_link("app.py", label="Início", icon="🏠")
    st.page_link("pages/1_Juros.py", label="Juros", icon="💹")
    st.page_link("pages/2_IPCA.py", label="IPCA", icon="📈")
    st.page_link(
        "pages/3_Renda_Variavel.py",
        label="Renda Variável",
        icon="📊"
    )
    st.markdown(SIDE_FOOTER, unsafe_allow_html=True)


# --------------------------------------------------
# Consulta ao Banco Central
# Série SGS 433: IPCA mensal (%)
# --------------------------------------------------
@st.cache_data(ttl=3600, show_spinner=False)
def obter_ipca(data_inicio, data_fim):
    df = sgs.get(
        {"IPCA": 433},
        start=data_inicio,
        end=data_fim
    )

    df = df.reset_index()
    df.columns = ["Data", "IPCA"]

    df["Data"] = pd.to_datetime(df["Data"])
    df["IPCA"] = pd.to_numeric(df["IPCA"], errors="coerce")

    return (
        df.dropna()
        .sort_values("Data")
        .reset_index(drop=True)
    )


# --------------------------------------------------
# Conteúdo da página
# --------------------------------------------------
st.title("📈 IPCA — Inflação mensal")
st.markdown(
    """
    Consulte a variação mensal do **Índice Nacional de Preços ao
    Consumidor Amplo (IPCA)**, indicador oficial da inflação no Brasil.
    """
)

hoje = pd.Timestamp.today().date()
inicio_padrao = hoje.replace(year=hoje.year - 1)

col1, col2 = st.columns(2)

with col1:
    data_inicio = st.date_input(
        "Data inicial",
        value=inicio_padrao
    )

with col2:
    data_fim = st.date_input(
        "Data final",
        value=hoje
    )

if data_inicio > data_fim:
    st.error("A data inicial deve ser anterior à data final.")
    st.stop()

if st.button("Consultar IPCA", type="primary"):
    st.session_state["consultar_ipca"] = True

if st.session_state.get("consultar_ipca", False):
    try:
        with st.spinner("Consultando dados do Banco Central..."):
            df = obter_ipca(data_inicio, data_fim)

        if df.empty:
            st.warning(
                "Não foram encontrados dados para o período selecionado."
            )
            st.stop()

        # Indicadores resumidos
        ultimo = df.iloc[-1]
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Último IPCA mensal",
                f"{ultimo['IPCA']:.2f}%"
            )

        with col2:
            st.metric(
                "Média mensal no período",
                f"{df['IPCA'].mean():.2f}%"
            )

        with col3:
            st.metric(
                "Meses consultados",
                f"{len(df)}"
            )

        # Gráfico mensal
        fig_ipca = px.bar(
            df,
            x="Data",
            y="IPCA",
            title="Variação mensal do IPCA (%)",
            labels={
                "Data": "Mês",
                "IPCA": "IPCA (%)"
            },
            color_discrete_sequence=["#10408D"],
            hover_data={
                "Data": "|%m/%Y",
                "IPCA": ":.2f"
            }
        )

        fig_ipca.update_layout(
            template="plotly_white",
            xaxis_title="Mês/Ano",
            yaxis_title="Variação mensal (%)",
            title_x=0.02,
            margin=dict(l=20, r=20, t=60, b=20)
        )

        fig_ipca.update_xaxes(
            dtick="M1",
            tickformat="%m/%Y",
            tickangle=-45
        )

        fig_ipca.update_yaxes(
            ticksuffix="%",
            zeroline=True
        )

        st.plotly_chart(
            fig_ipca,
            use_container_width=True
        )

        # Tabela de dados
        with st.expander("Visualizar dados mensais"):
            df_exibicao = df.copy()
            df_exibicao["Data"] = df_exibicao["Data"].dt.strftime("%m/%Y")
            df_exibicao["IPCA"] = df_exibicao["IPCA"].map(
                lambda valor: f"{valor:.2f}%"
            )

            st.dataframe(
                df_exibicao,
                use_container_width=True,
                hide_index=True
            )

            st.download_button(
                "Baixar dados em CSV",
                data=df.to_csv(index=False).encode("utf-8-sig"),
                file_name="ipca_mensal.csv",
                mime="text/csv"
            )

    except Exception as erro:
        st.error("Não foi possível consultar os dados do IPCA.")
        st.exception(erro)