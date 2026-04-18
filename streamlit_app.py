import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('Dashboard Penyewaan Sepeda 🚲')

df = pd.read_csv("dashboard/main_data.csv")

st.subheader('Ringkasan Data')
total_rentals = df['cnt'].sum()
st.metric(label="Total Seluruh Penyewaan", value=f"{total_rentals:,}")

st.subheader('Tren Penyewaan Sepeda per Bulan')
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=df, x='dteday', y='cnt', color='skyblue', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)
st.write("Grafik ini menunjukkan bagaimana fluktuasi penyewaan sepeda berubah seiring waktu.")

st.subheader('Jumlah Penyewaan Berdasarkan Kondisi Cuaca')
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=df, x='weathersit', y='cnt', palette='viridis', ax=ax)
st.pyplot(fig)
st.write("Dapat dilihat bahwa kondisi cuaca cerah memiliki jumlah penyewaan paling tinggi dibandingkan cuaca lainnya.")
