PALETA_AZUL = [
    "#E2EFF6",
    "#B7D7EA",
    "#8DBEDC",
    "#64A4CE",
    "#4893C6"
]

ESTILIZACAO1 = """
<style>
    /* Configuração geral */
    .stApp {
        background-color: #F5F8FC;
    }

    .block-container {
        max-width: 100%;
        padding: 1.5rem 1.7rem 1rem 1.7rem;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #102C50;
    }

    [data-testid="stSidebar"] * {
        color: #FFFFFF;
    }

    [data-testid="stSidebar"] hr {
        border-color: #4893C6;
    }

    /* Títulos */
    h1, h2, h3 {
        color: #102C50;
    }

    /* Texto auxiliar */
    .subtitulo {
        color: #647FA5;
        font-size: 1.08rem;
        line-height: 1.6;
    }

    /* Cartão de boas-vindas */
    .boas-vindas {
        padding: 0.5rem 0 1rem 0;
    }

    .boas-vindas h1 {
        color: #102C50;
        font-size: 2.45rem;
        font-weight: 750;
        line-height: 1.2;
        margin-bottom: 0.7rem;
    }

    /* Cartão de planejamento */
    .cartao-citacao {
        background: linear-gradient(120deg, #E2EFF6, #F4F8FF);
        border: 1px solid #D6E5F5;
        border-radius: 12px;
        padding: 1.5rem;
        min-height: 145px;
        display: flex;
        align-items: center;
        gap: 1.2rem;
    }

    .cartao-citacao .icone {
        font-size: 2.8rem;
    }

    .cartao-citacao .frase {
        color: #102C50;
        font-size: 1.12rem;
        font-style: italic;
        line-height: 1.6;
    }

    /* Cartões de navegação */
    .cartao {
        border-radius: 12px;
        padding: 1.15rem;
        min-height: 150px;
        border: 1px solid #D6E5F5;
    }

    .cartao-juros {
        background-color: #EDF5FF;
    }

    .cartao-ipca {
        background-color: #EFF9F5;
        border-color: #D0EBE1;
    }

    .cartao-renda {
        background-color: #F5F1FF;
        border-color: #E3D9FC;
    }

    .cartao-topo {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        margin-bottom: 0.8rem;
    }

    .icone-cartao {
        width: 44px;
        height: 44px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.45rem;
        font-weight: bold;
        flex-shrink: 0;
    }

    .icone-juros {
        background-color: #1976D2;
    }

    .icone-ipca {
        background-color: #0BA678;
    }

    .icone-renda {
        background-color: #7856D9;
    }

    .titulo-cartao {
        color: #102C50;
        font-size: 1.12rem;
        font-weight: 700;
    }

    .descricao-cartao {
        color: #425C7F;
        font-size: 0.88rem;
        line-height: 1.5;
    }

    /* Cabeçalhos das seções */
    .titulo-secao {
        color: #102C50;
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }

    /* Espaços dos gráficos */
    .area-grafico {
        background-color: #FFFFFF;
        border: 1px solid #DCE7F4;
        border-radius: 10px;
        padding: 1.2rem;
        min-height: 320px;
    }

    /* Botões */
    .stButton > button {
        border-radius: 8px;
        border: 1px solid #D6E5F5;
        font-weight: 600;
    }

    /* Rodapé */
    .rodape {
        color: #7186A5;
        font-size: 0.82rem;
        border-top: 1px solid #E0E9F4;
        padding-top: 1rem;
        margin-top: 1rem;
    }
</style>
"""

SIDE_STYLE = """
<div style="padding: 1.1rem 0 1.8rem 0;">
    <div style="font-size: 3rem;">📈</div>
    <div style="
        font-size: 1.8rem;
        font-weight: 750;
        line-height: 1.2;
    ">
        Dashboard<br>Financeiro
    </div>
</div>
"""

SIDE_FOOTER = """
<div style="
    margin-top: 3rem;
    border-top: 1px solid #4893C6;
    padding-top: 1.2rem;
    color: #E2EFF6;
    font-size: 0.88rem;
    line-height: 1.6;
">
    <span style="font-size: 1.2rem;">ⓘ</span>
    <br>
    Acompanhe seus investimentos e indicadores econômicos
    em um só lugar.
</div>
"""