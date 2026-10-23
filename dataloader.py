from bcb import sgs
import streamlit as st

@st.cache_data(ttl=3600)
def obter_indicadores():
    # Taxa Selic vigente (% ao ano)
    df_selic = sgs.get({'Selic': 432}, last=1)

    # IPCA mensal (%)
    df_ipca = sgs.get({'IPCA': 433}, last=1)

    selic = float(df_selic['Selic'].iloc[-1])
    data_selic = df_selic.index[-1]

    ipca = float(df_ipca['IPCA'].iloc[-1])
    data_ipca = df_ipca.index[-1]

    return selic, data_selic, ipca, data_ipca


selic, data_selic, ipca, data_ipca = obter_indicadores()
selic_fmt = f"{selic:.2f}".replace(".", ",")
ipca_fmt = f"{ipca:.2f}".replace(".", ",")