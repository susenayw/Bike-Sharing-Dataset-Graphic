import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set Page Configuration
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Helper function untuk load data
def load_data():
    df = pd.read_csv("main_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

day_df = load_data()

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.title("Filter Data")
    
    # Filter Rentang Tanggal
    min_date = day_df['dteday'].min()
    max_date = day_df['dteday'].max()
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter Dataframe berdasarkan input sidebar
main_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & 
                 (day_df['dteday'] <= pd.to_datetime(end_date))]

# --- MAIN PAGE ---
st.title("🚲 Bike Sharing Data Analytics Dashboard")
st.markdown(f"Menampilkan data dari **{start_date}** hingga **{end_date}**")

# --- METRICS ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan", value=f"{main_df['cnt'].sum():,}")
with col2:
    st.metric("Pengguna Registered", value=f"{main_df['registered'].sum():,}")
with col3:
    st.metric("Pengguna Casual", value=f"{main_df['casual'].sum():,}")

st.divider()

# --- PERTANYAAN 1: TREN BULANAN ---
st.subheader("1. Tren Penyewaan Bulanan")
monthly_df = main_df.resample(rule='ME', on='dteday').agg({"cnt": "sum"}).reset_index()

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(monthly_df["dteday"], monthly_df["cnt"], marker='o', linewidth=3, color="#3498db")
ax.set_title("Jumlah Penyewaan Sepeda per Bulan", fontsize=20)
st.pyplot(fig)

with st.expander("Lihat Insight Tren"):
    st.write("""
    * **Temuan**: Penyewaan mencapai puncak pada kuartal 3 namun turun drastis di akhir tahun.
    * **Strategi**: Lakukan pemeliharaan armada di bulan Desember saat permintaan rendah.
    """)

# --- PERTANYAAN 2: CUACA VS TIPE PENGGUNA ---
st.subheader("2. Performa Penyewaan berdasarkan Kondisi Cuaca")
weather_user_df = main_df.groupby('weathersit_label').agg({
    'casual': 'mean',
    'registered': 'mean'
}).reset_index().melt(id_vars='weathersit_label')

fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(data=weather_user_df, x='weathersit_label', y='value', hue='variable', palette='viridis', ax=ax)
ax.set_title("Rata-rata Penyewaan: Casual vs Registered", fontsize=20)
st.pyplot(fig)

with st.expander("Lihat Insight Cuaca"):
    st.write("""
    * **Temuan**: Pengguna Casual sangat sensitif terhadap cuaca (anjlok saat hujan).
    * **Strategi**: Berikan promo khusus cuaca cerah untuk pengguna Casual untuk memaksimalkan profit.
    """)

# --- ANALISIS LANJUTAN: CLUSTERING ---
st.subheader("3. Clustering Intensitas Penyewaan")
fig, ax = plt.subplots(figsize=(16, 8))
sns.countplot(data=main_df, x='weathersit_label', hue='rental_intensity', 
              hue_order=['Low', 'Medium', 'High', 'Very High'], palette='magma', ax=ax)
ax.set_title("Distribusi Intensitas (Cluster) berdasarkan Cuaca", fontsize=20)
st.pyplot(fig)

st.info("""
**Rekomendasi Operasional:**
Pastikan ketersediaan sepeda 100% saat prediksi cuaca 'Clear' (Cluster Very High) dan efisiensi kru lapangan saat cuaca 'Light Snow/Rain' (Cluster Low).
""")
