import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Helper function untuk memuat data
def load_data():
    df = pd.read_csv("main_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

day_df = load_data()

# --- SIDEBAR: Filter Interaktif ---
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.title("Filter Data")
    
    # Filter Rentang Waktu
    min_date = day_df['dteday'].min()
    max_date = day_df['dteday'].max()
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter dataframe berdasarkan input sidebar
main_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & 
                 (day_df['dteday'] <= pd.to_datetime(end_date))]

# --- HEADER ---
st.title("🚲 Dashboard Analisis Data: Bike Sharing Dataset")
st.markdown(f"Menampilkan wawasan strategis dari periode **{start_date}** sampai **{end_date}**")

# --- METRIKS UTAMA ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan", value=f"{main_df['cnt'].sum():,}")
with col2:
    st.metric("Pengguna Registered", value=f"{main_df['registered'].sum():,}")
with col3:
    st.metric("Pengguna Casual", value=f"{main_df['casual'].sum():,}")

st.divider()

# --- PERTANYAAN 1: TREN STRATEGIS 2012 ---
st.subheader("1. Strategi Optimalisasi Berdasarkan Tren Bulanan")
# Resample bulanan (menggunakan 'ME' untuk kompatibilitas versi terbaru)
monthly_df = main_df.resample(rule='ME', on='dteday').agg({"cnt": "sum"}).reset_index()

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(monthly_df["dteday"], monthly_df["cnt"], marker='o', linewidth=3, color="#2E86C1")
ax.set_title("Tren Total Penyewaan Sepeda per Bulan", fontsize=20)
ax.set_xlabel("Bulan", fontsize=15)
ax.set_ylabel("Total Unit", fontsize=15)
st.pyplot(fig)

# Insight setara Notebook
with st.expander("Lihat Analisis Strategis Tren"):
    st.markdown("""
    1. **Temuan Data**: Terdapat lonjakan permintaan signifikan pada kuartal 3 (puncak di September), namun menurun drastis hingga 40% saat memasuki Desember seiring datangnya musim dingin.
    2. **Analisis Strategis**: Penurunan ini bersifat musiman yang dapat diprediksi, menyebabkan rendahnya produktivitas armada di akhir tahun.
    3. **Rekomendasi (Actionable)**:
        * **Golden Maintenance**: Manfaatkan Desember untuk pemeliharaan besar-besaran agar armada prima saat musim semi tiba.
        * **Winter Membership**: Tawarkan paket langganan murah di Oktober-November untuk menahan laju penurunan pengguna komuter.
    """)

st.divider()

# --- PERTANYAAN 2: PERILAKU SEGMEN & CUACA ---
st.subheader("2. Pengaruh Cuaca Terhadap Segmen Casual vs Registered")

weather_user_df = main_df.groupby('weathersit').agg({
    'casual': 'mean',
    'registered': 'mean'
}).reset_index().melt(id_vars='weathersit')

fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(data=weather_user_df, x='weathersit', y='value', hue='variable', palette='viridis', ax=ax)
ax.set_title("Rata-rata Penyewaan: Casual vs Registered Berdasarkan Cuaca", fontsize=20)
ax.set_xlabel("Kondisi Cuaca", fontsize=15)
ax.set_ylabel("Rata-rata Penyewaan", fontsize=15)
st.pyplot(fig)

# Insight setara Notebook
with st.expander("Lihat Analisis Strategis Segmen & Cuaca"):
    st.markdown("""
    1. **Temuan Data**: Pengguna **Casual** sangat sensitif (anjlok 70% saat cuaca buruk), sedangkan pengguna **Registered** jauh lebih stabil karena kebutuhan komuter harian.
    2. **Analisis Strategis**: Pengguna Registered adalah pilar stabilitas pendapatan, sementara Casual adalah potensi pendapatan tambahan saat cuaca cerah.
    3. **Rekomendasi (Actionable)**:
        * **Weather-Based Marketing**: Kirim notifikasi promo otomatis untuk segmen Casual saat ramalan cuaca besok diprediksi cerah.
        * **Loyalty Program**: Berikan poin ekstra bagi pengguna Registered yang tetap bersepeda di cuaca mendung/hujan ringan.
    """)

st.divider()

# --- ANALISIS LANJUTAN: CLUSTERING INTENSITAS ---
st.subheader("3. Analisis Lanjutan: Clustering Intensitas Penyewaan")

fig, ax = plt.subplots(figsize=(16, 8))
# Menampilkan distribusi cluster terhadap cuaca
sns.countplot(data=main_df, x='weathersit', hue='rental_intensity', 
              hue_order=['Low', 'Medium', 'High', 'Very High'], palette='magma', ax=ax)
ax.set_title("Distribusi Intensitas (Cluster) Berdasarkan Cuaca", fontsize=20)
st.pyplot(fig)

# Insight setara Notebook
st.info("""
**Rekomendasi Operasional Berdasarkan Clustering:**
1. **Optimasi Stok**: Pastikan ketersediaan unit 100% di stasiun utama saat cuaca 'Clear' (Cluster High/Very High).
2. **Efisiensi Biaya**: Kurangi shift kru lapangan saat cuaca 'Light Snow/Rain' karena permintaan diprediksi masuk kategori 'Low'.
3. **Stimulus Pemasaran**: Luncurkan promo pada kondisi 'Misty/Cloudy' untuk mendorong intensitas dari Medium ke High.
""")
