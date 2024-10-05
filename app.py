import streamlit as st
from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt


symbol=st.sidebar.text_input("Hisse Senedi Sembolü",value="ASELS")
st.title(symbol+" Hisse Senedi Grafiği")

start_date=st.sidebar.date_input("Başlangıç Tarihi",value=datetime(2023,1,1))
end_date=st.sidebar.date_input("Bitiş Tarihi",value=datetime.now())

df=yf.download(symbol + ".IS",start=start_date,end=end_date)
st.subheader("Hisse Senedi Trend GRafiği")
st.line_chart(df["Close"])
st.subheader("Hisse Senedi Fiyatlar Tablosu")
st.write(df)
