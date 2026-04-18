# 🚲 Proyek Analisis Data: Bike Sharing Dataset

Selamat datang di proyek akhir analisis data saya! Proyek ini mengeksplorasi data penyewaan sepeda untuk memahami tren penggunaan berdasarkan waktu dan pengaruh faktor lingkungan seperti cuaca.

---

## 📊 Ringkasan Proyek
Proyek ini bertujuan untuk menjawab beberapa tantangan bisnis:
1.  **Tren Waktu**: Bagaimana fluktuasi jumlah penyewaan sepeda di sepanjang tahun 2012?
2.  **Kondisi Lingkungan**: Sejauh mana kondisi cuaca mempengaruhi minat pengguna (Casual vs Registered) untuk menyewa sepeda?

## 📂 Struktur Direktori
Berikut adalah susunan folder dalam proyek ini:
- `dashboard/`: Berisi file utama untuk dashboard interaktif (`dashboard.py`) dan dataset hasil pembersihan (`main_data.csv`).
- `data/`: Berisi dataset mentah asli (`day.csv` dan `hour.csv`).
- `notebook.ipynb`: Dokumentasi lengkap proses analisis mulai dari *Gathering*, *Cleaning*, *EDA*, hingga *Exploratory Analysis*.
- `requirements.txt`: Daftar pustaka (library) Python yang dibutuhkan.
- `url.txt`: Tautan menuju dashboard yang telah di-deploy (jika ada).

---

## 🛠️ Persiapan Lingkungan (Setup Environment)

Pastikan Anda memiliki Python yang sudah terinstal di sistem Anda. Ikuti langkah berikut:

1.  **Clone atau Unduh Repository ini** ke komputer lokal Anda.
2.  **Buka Terminal atau Command Prompt** di direktori proyek.
3.  **Instalasi Library**:
    
```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Menjalankan Dashboard Streamlit

Untuk melihat visualisasi data secara interaktif, jalankan perintah berikut di terminal:
```bash
streamlit run dashboard/dashboard.py
