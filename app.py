import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from utils import PALETA_AZUL, ESTILIZACAO1, SIDE_STYLE, SIDE_FOOTER
from graficos import fig_ipca, fig_bovespa
from dataloader import selic, data_selic, ipca, data_ipca, selic_fmt, ipca_fmt

st.set_page_config(
    page_title="Dashboard Financeiro",
    page_icon="📊",
    layout="wide"
)

# CSS
# =========================================================
st.markdown(ESTILIZACAO1, unsafe_allow_html=True)

# Fundo lilás do card de Renda Variável (mantém o visual original)
st.markdown(
    """
    <style>
    .st-key-card_renda {
        background: #F5F0FF;
        border-radius: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# SIDEBAR
# =========================================================
with st.sidebar:
    st.markdown(SIDE_STYLE,
        unsafe_allow_html=True
    )

    st.page_link(
        "app.py",
        label="Início",
        icon="🏠"
    )

    st.page_link(
        "pages/1_Juros.py",
        label="Juros",
        icon="💹"
    )

    st.page_link(
        "pages/2_IPCA.py",
        label="IPCA",
        icon="📈"
    )

    st.page_link(
        "pages/3_Renda_Variavel.py",
        label="Renda Variável",
        icon="📊"
    )

    st.markdown(
        SIDE_FOOTER,
        unsafe_allow_html=True
    )


# =========================================================
# CABEÇALHO PRINCIPAL
# =========================================================

col_titulo, col_citacao = st.columns(
    [1.35, 0.85],
    gap="large",
    vertical_alignment="center"
)

with col_titulo:
    st.markdown(
        """
        <div class="boas-vindas">
            <h1>Bem-vindo ao seu<br>Dashboard Financeiro</h1>
            <div class="subtitulo">
                Acompanhe os principais indicadores econômicos
                e o desempenho dos seus investimentos.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_citacao:
    st.markdown(
        """
        <div class="cartao-citacao">
            <div class="icone">🎯</div>
            <div class="frase">
                “Planejamento financeiro é a chave para um
                futuro mais seguro.”
                <div style="
                    margin-top: 0.8rem;
                    width: 48px;
                    border-bottom: 3px solid #1976D2;
                "></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")


# =========================================================
# CARTÕES DE NAVEGAÇÃO
# =========================================================
# Os três cards seguem a MESMA estrutura:
#   container com borda -> cabeçalho -> métrica -> legenda -> botão
# Assim ficam com a mesma altura e os botões alinhados.

def cartao(icone, classe_icone, titulo, rotulo, valor, legenda,
           texto_botao, chave_botao, pagina, chave_container=None):
    with st.container(border=True, key=chave_container):
        st.markdown(
            f"""
            <div class="cartao-topo">
                <div class="icone-cartao {classe_icone}">{icone}</div>
                <div class="titulo-cartao">{titulo}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.metric(
            label=rotulo,
            value=valor,
            label_visibility="collapsed"
        )

        st.caption(legenda)

        if st.button(
            texto_botao,
            key=chave_botao,
            use_container_width=True
        ):
            st.switch_page(pagina)


col_juros, col_ipca, col_renda = st.columns(
    3,
    gap="medium"
)

with col_juros:
    cartao(
        icone="%",
        classe_icone="icone-juros",
        titulo="Taxa Selic",
        rotulo="Taxa Selic",
        valor=f"{selic_fmt}% a.a.",
        legenda=(
            "Taxa básica de juros da economia brasileira. "
            f"Referência: {data_selic.strftime('%d/%m/%Y')}"
        ),
        texto_botao="Explorar juros →",
        chave_botao="btn_juros",
        pagina="pages/1_Juros.py",
    )

with col_ipca:
    cartao(
        icone="▤",
        classe_icone="icone-ipca",
        titulo="IPCA mensal",
        rotulo="IPCA mensal",
        valor=f"{ipca_fmt}%",
        legenda=(
            "Variação mensal da inflação oficial do Brasil. "
            f"Referência: {data_ipca.strftime('%m/%Y')}"
        ),
        texto_botao="Explorar IPCA →",
        chave_botao="btn_ipca",
        pagina="pages/2_IPCA.py",
    )

with col_renda:
    cartao(
        icone="↗",
        classe_icone="icone-renda",
        titulo="Renda Variável",
        rotulo="Renda Variável",
        valor="Ibovespa",
        legenda="Acompanhe o desempenho da bolsa e seus ativos. Fonte: B3",
        texto_botao="Explorar investimentos →",
        chave_botao="btn_renda",
        pagina="pages/3_Renda_Variavel.py",
        chave_container="card_renda",
    )


# =========================================================
# ÁREAS RESERVADAS PARA GRÁFICOS
# =========================================================

st.write("")

col_ipca_grafico, col_ibovespa = st.columns(
    [1.45, 1],
    gap="medium"
)

with col_ipca_grafico:
    with st.container(border=True):
        st.markdown(
            '<div class="titulo-secao">Evolução do IPCA '
            '<span style="font-weight:400; font-size:0.9rem;">'
            '(últimos 12 meses)</span></div>',
            unsafe_allow_html=True
        )

        st.caption("Área reservada para o gráfico de inflação.")

        st.markdown(
            '<div class="titulo-secao">Evolução do IPCA '
            '<span style="font-weight:400; font-size:0.9rem;">'
            '(últimos 12 meses)</span></div>',
            unsafe_allow_html=True
        )

        st.plotly_chart(
            fig_ipca,
            use_container_width=True
        )

with col_ibovespa:
    with st.container(border=True):
        st.markdown(
            '<div class="titulo-secao">'
            'Desempenho da Bolsa (Ibovespa)</div>',
            unsafe_allow_html=True
        )

        st.caption("Área reservada para o acompanhamento do índice.")

        st.markdown(
            """
            <div class="titulo-secao">
                Desempenho da Bolsa (Ibovespa)
                <span style="font-weight:400; font-size:0.9rem;">
                    (últimos 12 meses)
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.plotly_chart(
            fig_bovespa,
            use_container_width=True
        )


# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
    """
    <div class="rodape">
        Dashboard Financeiro &nbsp; • &nbsp;
        Indicadores econômicos e de investimentos
        <span style="float:right;">
            Construído com Streamlit
        </span>
    </div>
    """,
    unsafe_allow_html=True
)