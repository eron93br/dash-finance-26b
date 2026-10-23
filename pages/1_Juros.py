import pandas as pd
import streamlit as st
import plotly.express as px
from bcb import sgs

from utils import ESTILIZACAO1, SIDE_STYLE, SIDE_FOOTER

st.set_page_config(
    page_title="Taxa de Juros",
    page_icon="💹",
    layout="wide"
)

st.markdown(ESTILIZACAO1, unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

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


# =========================================================
# CONSULTA SELIC
# =========================================================

@st.cache_data(ttl=3600, show_spinner=False)
def obter_selic(data_inicio, data_fim):
    df = sgs.get(
        {"Selic": 432},
        start=data_inicio,
        end=data_fim
    )

    df = df.reset_index()
    df.columns = ["Data", "Selic"]

    df["Data"] = pd.to_datetime(df["Data"])
    df["Selic"] = pd.to_numeric(df["Selic"], errors="coerce")

    return df.dropna().sort_values("Data")


# =========================================================
# CABEÇALHO
# =========================================================

st.title("💹 Taxa de Juros — Brasil")

st.write(
    "Consulte a evolução da taxa Selic e selecione "
    "o período que deseja analisar."
)

# =========================================================
# FILTROS
# =========================================================

col_inicio, col_fim = st.columns(2)

with col_inicio:
    data_inicio = st.date_input(
        "Data inicial",
        value=pd.Timestamp.today().date().replace(
            year=pd.Timestamp.today().year - 1
        ),
        format="DD/MM/YYYY",
        key="selic_inicio"
    )

with col_fim:
    data_fim = st.date_input(
        "Data final",
        value=pd.Timestamp.today().date(),
        format="DD/MM/YYYY",
        key="selic_fim"
    )

if data_inicio > data_fim:
    st.error("A data inicial deve ser anterior à data final.")
    st.stop()

# =========================================================
# GRÁFICO
# =========================================================

if st.button("Consultar Selic", type="primary"):
    st.session_state["consultar_selic"] = True

if st.session_state.get("consultar_selic", False):

    try:
        with st.spinner("Consultando dados do Banco Central..."):
            df = obter_selic(data_inicio, data_fim)

        if df.empty:
            st.warning("Nenhum dado encontrado para esse período.")

        else:
            fig_juros = px.line(
                df,
                x="Data",
                y="Selic",
                title="Evolução da Taxa Selic",
                labels={
                    "Data": "Data",
                    "Selic": "Taxa Selic (% a.a.)"
                },
                color_discrete_sequence=["#10408D"]
            )

            fig_juros.update_layout(
                template="plotly_white",
                title_x=0,
                height=430,
                margin=dict(l=20, r=20, t=60, b=20),
                hovermode="x unified",
                showlegend=False,
                xaxis=dict(showgrid=False),
                yaxis=dict(
                    ticksuffix="%",
                    gridcolor="#E2EFF6",
                    title="Taxa (% a.a.)"
                )
            )

            fig_juros.update_traces(line=dict(width=2.5))

            st.plotly_chart(
                fig_juros,
                use_container_width=True
            )

            st.caption(
                "Fonte: Banco Central do Brasil — SGS, série 432."
            )

    except Exception as erro:
        st.error(
            "Não foi possível consultar a Selic. "
            "Verifique sua conexão ou tente novamente."
        )
        st.exception(erro)

