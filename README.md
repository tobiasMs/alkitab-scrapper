[English](#english) | [Bahasa Indonesia](#bahasa-indonesia)

---

<a name="english"></a>
## English

# Alkitab Scrapper (SABDA API)

A Python-based tool to scrape Bible data from the [alkitab.sabda.org](https://alkitab.sabda.org) API. This script allows you to download full Bible versions (currently supporting TB and Jawa) in JSON and XML formats for offline use in your own applications.

### 🌟 Features
- **Multi-Version Support**: Scrapes both *Terjemahan Baru (TB)* and *Jawa* versions.
- **Flexible Formats**: Export data to JSON, XML, or both.
- **Rate Limiting**: Includes a configurable delay between requests to be polite to the SABDA servers.
- **CLI & Module Ready**: Run it as a standalone script or import its functions into your project.

### 📋 Prerequisites
- Python 3.6+
- `requests` library

### 🚀 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alkitab-scrapper.git
   cd alkitab-scrapper
   ```
2. Install dependencies:
   ```bash
   pip install requests
   ```

### 💻 Usage

#### 1. Command Line Interface (CLI)
Run the script directly from your terminal:
```bash
python scrapper.py --output my-data --delay 0.5 --format both
```
**Arguments:**
- `--output`: Folder name for the results (Default: `bible-data`).
- `--delay`: Seconds to wait between chapter requests (Default: `0.3`).
- `--format`: Output format (`json`, `xml`, or `both`).

#### 2. Programmatic Usage (As a Library)
You can import the scraper into your own Python scripts:

```python
from scrapper import scrape_version, scrape_all_versions

# Option A: Scrape everything
scrape_all_versions(output_dir="my_bible", delay=0.5, format_output="json")

# Option B: Scrape a specific version only
scrape_version(version="tb", output_dir="data", delay=0.2, format_output="xml")
```

### 📂 Data Structure
The script generates a structured folder:
- `books.json`: List of all Bible books with their abbreviations and chapter counts.
- `[version]/`: Subfolder containing the full Bible data in your chosen format.

**Example JSON structure:**
```json
{
  "version": "tb",
  "books": [
    {
      "name": "Kejadian",
      "chapters": [
        {
          "chapter": 1,
          "verses": [
            { "verse": 1, "text": "Pada mulanya Allah menciptakan langit dan bumi." }
          ]
        }
      ]
    }
  ]
}
```

---

<a name="bahasa-indonesia"></a>
## Bahasa Indonesia

# Alkitab Scrapper (SABDA API)

Alat berbasis Python untuk mengambil (scrape) data Alkitab dari API [alkitab.sabda.org](https://alkitab.sabda.org). Skrip ini memungkinkan Anda mengunduh versi Alkitab lengkap (saat ini mendukung TB dan Jawa) dalam format JSON dan XML untuk penggunaan offline di aplikasi Anda sendiri.

### 🌟 Fitur
- **Dukungan Multi-Versi**: Mengambil versi *Terjemahan Baru (TB)* dan *Jawa*.
- **Format Fleksibel**: Ekspor data ke JSON, XML, atau keduanya.
- **Pembatasan Laju (Rate Limiting)**: Menyertakan delay yang dapat diatur antar permintaan agar lebih sopan terhadap server SABDA.
- **Siap CLI & Modul**: Jalankan sebagai skrip mandiri atau impor fungsinya ke proyek Anda.

### 📋 Prasyarat
- Python 3.6+
- Pustaka `requests`

### 🚀 Instalasi
1. Klon repositori:
   ```bash
   git clone https://github.com/username-anda/alkitab-scrapper.git
   cd alkitab-scrapper
   ```
2. Instal dependensi:
   ```bash
   pip install requests
   ```

### 💻 Penggunaan

#### 1. Antarmuka Baris Perintah (CLI)
Jalankan skrip langsung dari terminal Anda:
```bash
python scrapper.py --output data-alkitab --delay 0.5 --format both
```
**Argumen:**
- `--output`: Nama folder untuk hasil (Default: `bible-data`).
- `--delay`: Detik untuk menunggu antar permintaan pasal (Default: `0.3`).
- `--format`: Format output (`json`, `xml`, atau `both`).

#### 2. Penggunaan Programmatik (Sebagai Library)
Anda dapat mengimpor scrapper ke dalam skrip Python Anda sendiri:

```python
from scrapper import scrape_version, scrape_all_versions

# Opsi A: Scrape semua versi
scrape_all_versions(output_dir="alkitab_saya", delay=0.5, format_output="json")

# Opsi B: Scrape versi spesifik saja
scrape_version(version="tb", output_dir="data", delay=0.2, format_output="xml")
```

### 📂 Struktur Data
Skrip ini menghasilkan folder terstruktur:
- `books.json`: Daftar semua kitab Alkitab beserta singkatan dan jumlah pasalnya.
- `[versi]/`: Subfolder berisi data Alkitab lengkap dalam format yang Anda pilih.

**Contoh struktur JSON:**
```json
{
  "version": "tb",
  "books": [
    {
      "name": "Kejadian",
      "chapters": [
        {
          "chapter": 1,
          "verses": [
            { "verse": 1, "text": "Pada mulanya Allah menciptakan langit dan bumi." }
          ]
        }
      ]
    }
  ]
}
```

---

### ⚠️ Disclaimer
Project ini dibuat untuk tujuan edukasi. Pastikan Anda mematuhi kebijakan penggunaan data dari [alkitab.sabda.org](https://alkitab.sabda.org) sebelum menggunakan data ini untuk tujuan komersial. 