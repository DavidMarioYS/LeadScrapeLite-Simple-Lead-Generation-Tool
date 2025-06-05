

# 🔍 LeadScrapeLite — Simple Lead Generation Tool

**LeadScrapeLite** adalah alat ringan berbasis web untuk *lead generation* (pengumpulan calon pelanggan) yang menggabungkan kekuatan **Google Custom Search API** dan **email scraping** otomatis dari situs web.
Dengan antarmuka interaktif menggunakan **Streamlit**, pengguna cukup mengetikkan kata kunci (misalnya: *startup AI Indonesia*) — aplikasi akan mencari situs yang relevan, mengekstrak email kontak dari halaman utama dan halaman kontak, lalu menyajikan hasilnya secara visual dan dapat diekspor.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" />
  <img src="https://img.shields.io/badge/Streamlit-%E2%9C%85-red" />
  <img src="https://img.shields.io/badge/Scraping-BeautifulSoup-yellow" />
  <img src="https://img.shields.io/badge/API-Google%20CSE-blue" />
</p>

---

## 🚀 Fitur Unggulan

* 🔍 **Integrasi Google Search** via Custom Search API
* 📬 **Ekstraksi email** dari halaman utama dan `/contact`
* 💾 **Penyimpanan otomatis** hasil scraping ke database SQLite
* 🔄 **Progress bar interaktif** selama scraping berlangsung
* 📋 **Tabel hasil yang dapat difilter dan diperluas**
* 📊 **Visualisasi data**: diagram lingkaran, histogram, dan word cloud
* 📤 **Ekspor hasil ke CSV** untuk kebutuhan lanjutan atau CRM

---

## 🧪 Contoh Hasil

### 📋 Tabel Leads

* Menampilkan URL, Judul, Deskripsi, dan Email
* Dapat diperluas untuk melihat seluruh detail
* Tombol untuk membuka situs langsung

### 📈 Analisis Visual

* Pie chart distribusi email berdasarkan domain
* Histogram jumlah email per situs
* Word cloud dari meta description situs hasil pencarian

---

## 🧑‍💻 Demo Langsung (Opsional)

> Coming soon: Notebook interaktif atau versi demo online via Streamlit Cloud / Hugging Face Spaces.

---

## ⚙️ Teknologi yang Digunakan

| Kategori      | Teknologi / Library      |
| ------------- | ------------------------ |
| Web UI        | Streamlit                |
| Web Scraping  | BeautifulSoup, Requests  |
| API Pencarian | Google Custom Search API |
| Visualisasi   | Matplotlib, WordCloud    |
| Data Handling | Pandas, SQLAlchemy       |
| Database      | SQLite (leads.db)        |

---

## 🔧 Cara Instalasi

### 1. Clone repositori ini

```bash
git clone https://github.com/your-username/LeadScrapeLite.git
cd LeadScrapeLite
```

### 2. Buat virtual environment (opsional tapi disarankan)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Instalasi dependencies

```bash
pip install -r requirements.txt
```

### 4. Tambahkan kredensial Google API

Buat file `.env` atau langsung ubah di `app.py`:

```python
api_key = "YOUR_API_KEY"
search_engine_id = "YOUR_CUSTOM_SEARCH_ENGINE_ID"
```

🔑 **Cara mendapatkannya:**

* Masuk ke [Google Cloud Console](https://console.cloud.google.com/)
* Buat proyek baru dan aktifkan **Custom Search API**
* Buat mesin pencari kustom di [Google Programmable Search Engine](https://programmablesearchengine.google.com/)

---

## ▶️ Jalankan Aplikasinya

```bash
streamlit run app.py
```

Akses aplikasi di browser: [http://localhost:8501](http://localhost:8501)

---

## 🗂 Struktur Proyek

```
LeadScrapeLite/
├── app.py               # Streamlit app utama
├── leads.db             # Database SQLite (dibuat otomatis)
├── requirements.txt     # Daftar dependency Python
├── README.md            # Dokumentasi proyek
```

---

## 📦 Dependencies Utama

* **[Streamlit](https://streamlit.io/)** — framework antarmuka pengguna berbasis Python
* **[Requests](https://docs.python-requests.org/)** — HTTP client untuk akses web
* **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)** — parser HTML untuk scraping
* **[Pandas](https://pandas.pydata.org/)** — manipulasi dan analisis data
* **[SQLAlchemy](https://www.sqlalchemy.org/)** — ORM untuk interaksi database
* **[WordCloud](https://amueller.github.io/word_cloud/)** — visualisasi teks berbentuk awan kata
* **[Matplotlib](https://matplotlib.org/)** — grafik dan visualisasi data

---

## ⚠️ Keterbatasan Saat Ini

* ❗ Hanya men-scrape halaman HTML statis (tidak mendukung JS-rendered site)
* ❗ Batas penggunaan Google API tergantung pada **free-tier quota**
* ❗ Belum ada validasi email otomatis (misal: email palsu, disposable, spam)

---

## 🌱 Pengembangan ke Depan

* 🧠 Integrasi model AI (LLM / NER) untuk menyaring email penting (e.g., HR, CEO)
* 📊 Penilaian kualitas domain (domain authority scoring)
* 📁 Ekspor hasil dalam format standar CRM (dengan kategori/tag)
* ☁️ Hosting di platform publik seperti Streamlit Cloud atau Hugging Face Spaces
* 🔐 Tambahkan rate limiter dan retry mechanism untuk scraping

---

## 🙋 Tentang Pengembang

**David Mario Yohanes Samosir**
💼 IT & Digital Services Enthusiast | Python Developer

* 🌐 [LinkedIn](https://www.linkedin.com/in/david-mario-yohanes-samosir/)
* 📧 [davidmario484@gmail.com](mailto:davidmario484@gmail.com)

---

> Jika kamu suka proyek ini, bantu beri ⭐ di GitHub dan bagikan ke sesama praktisi lead gen atau digital marketing!

---
