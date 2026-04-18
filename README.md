# 🚲 Proyek Analisis Data: Bike Sharing Dataset

Proyek ini merupakan bagian dari tugas akhir untuk kelas "	Belajar Fundamental Analisis Data" di Dicoding. Fokus utama proyek ini adalah melakukan proses analisis data secara lengkap mulai dari pembersihan data, eksplorasi, hingga pembuatan dashboard interaktif yang memberikan wawasan strategis berdasarkan dataset penyewaan sepeda.

---

## 📊 Hasil Analisis (Ringkasan)
- **Optimalisasi Strategis**: Mengidentifikasi pola penurunan penyewaan pada kuartal akhir 2012 untuk merencanakan jadwal pemeliharaan armada dan promo musiman.
- **Pengaruh Kondisi Cuaca**: Menganalisis bagaimana perbedaan cuaca memengaruhi perilaku segmen pengguna Casual dan Registered guna menentukan strategi pemasaran yang dipersonalisasi.

---

## 📂 Struktur Direktori
- `dashboard/`: Berisi file utama dashboard (`dashboard.py`) dan dataset hasil pembersihan (`main_data.csv`).
- `data/`: Berisi dataset mentah asli (`day.csv` dan `hour.csv`).
- `notebook.ipynb`: Dokumentasi lengkap proses analisis data mulai dari Wrangling hingga Explanatory Analysis.
- `requirements.txt`: Daftar pustaka (library) Python yang dibutuhkan untuk menjalankan proyek.
- `README.md`: Panduan lengkap pengaturan lingkungan dan penggunaan proyek.
- `url.txt`: Tautan menuju dashboard yang telah di-deploy.

---

## ⚙️ Pengaturan Lingkungan (Setting Environment)

Sangat disarankan untuk menggunakan lingkungan virtual (*virtual environment*) guna menghindari konflik versi pustaka antar proyek.

### **Opsi 1: Menggunakan Virtual Environment (venv)**
1.  **Buka Terminal** dan masuk ke direktori proyek Anda:
    ```bash
    cd nama-folder-proyek
    ```
2.  **Buat virtual environment**:
    ```bash
    python -m venv venv
    ```
3.  **Aktifkan virtual environment**:
    - **Windows**:
      ```bash
      .\venv\Scripts\activate
      ```
    - **Mac/Linux**:
      ```bash
      source venv/bin/activate
      ```
4.  **Instalasi dependensi**:
    ```bash
    pip install -r requirements.txt
    ```

### **Opsi 2: Menggunakan Anaconda (Conda)**
1.  **Buat environment baru**:
    
```bash
    conda create --name bike-sharing-ds python=3.9
    ```
2.  **Aktifkan environment**:
    
```bash
    conda activate bike-sharing-ds
    ```
3.  **Instalasi dependensi**:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Cara Menjalankan Dashboard

Setelah pengaturan lingkungan selesai, Anda dapat menjalankan dashboard interaktif dengan perintah berikut:
```bash
streamlit run dashboard/dashboard.py
