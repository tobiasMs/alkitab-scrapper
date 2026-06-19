[English](#english) | [Bahasa Indonesia](#bahasa-indonesia)

---

<a name="english"></a>
## English

# Alkitab Scrapper

A Python-based tool to scrape Bible data from [alkitab.mobi](https://alkitab.mobi). Downloads full Bible versions (TB and Jawa) in JSON and XML formats for offline use.

### Features
- **Multi-Version Support**: Scrapes *Terjemahan Baru (TB)* and *Jawa* versions.
- **Flexible Formats**: Export to JSON, XML, or both.
- **Rate Limiting**: Configurable delay between requests.
- **CLI & Module Ready**: Run as a standalone script or import into your project.

### Prerequisites
- Python 3.6+
- `requests`, `beautifulsoup4`, `lxml`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alkitab-scrapper.git
   cd alkitab-scrapper
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### 1. Command Line
```bash
python scrapper.py --output bible-data --delay 0.5 --format both
```

| Argument | Default | Description |
|---|---|---|
| `--output` | `bible-data` | Output folder |
| `--delay` | `0.3` | Seconds between requests |
| `--format` | `both` | `json`, `xml`, or `both` |

#### 2. Programmatic
```python
from scrapper import scrape_version, scrape_all_versions

# Scrape all versions
scrape_all_versions(output_dir="bible-data", delay=0.5, format_output="json")

# Scrape a specific version only
scrape_version(version="tb", output_dir="bible-data", delay=0.2, format_output="xml")
```

### Output Structure

```
bible-data/
├── books.json
├── tb/
│   ├── bible-tb.json
│   └── bible-tb.xml
└── jawa/
    ├── bible-jawa.json
    └── bible-jawa.xml
```

**JSON format:**
```json
{
  "version": "tb",
  "books": [
    {
      "no": 1,
      "name": "Kejadian",
      "abbr": "kej",
      "total_chapter": 50,
      "chapters": [
        {
          "chapter": 1,
          "verses": [
            {
              "verse": 1,
              "text": "Pada mulanya Allah menciptakan langit dan bumi.",
              "title": "Allah menciptakan langit dan bumi serta isinya"
            },
            {
              "verse": 2,
              "text": "Bumi belum berbentuk dan kosong...",
              "title": null
            }
          ]
        }
      ]
    }
  ]
}
```

> `title` is the section heading. Only the first verse in a section has a title; subsequent verses have `null`.

---

<a name="bahasa-indonesia"></a>
## Bahasa Indonesia

# Alkitab Scrapper

Alat berbasis Python untuk mengambil data Alkitab dari [alkitab.mobi](https://alkitab.mobi). Mengunduh versi Alkitab lengkap (TB dan Jawa) dalam format JSON dan XML untuk penggunaan offline.

### Fitur
- **Dukungan Multi-Versi**: Mengambil versi *Terjemahan Baru (TB)* dan *Jawa*.
- **Format Fleksibel**: Ekspor ke JSON, XML, atau keduanya.
- **Rate Limiting**: Delay antar request yang dapat diatur.
- **Siap CLI & Modul**: Jalankan sebagai skrip mandiri atau impor ke proyek Anda.

### Prasyarat
- Python 3.6+
- `requests`, `beautifulsoup4`, `lxml`

### Instalasi
1. Clone repositori:
   ```bash
   git clone https://github.com/your-username/alkitab-scrapper.git
   cd alkitab-scrapper
   ```
2. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

### Penggunaan

#### 1. Command Line
```bash
python scrapper.py --output bible-data --delay 0.5 --format both
```

| Argumen | Default | Keterangan |
|---|---|---|
| `--output` | `bible-data` | Folder output |
| `--delay` | `0.3` | Jeda antar request (detik) |
| `--format` | `both` | `json`, `xml`, atau `both` |

#### 2. Programmatik
```python
from scrapper import scrape_version, scrape_all_versions

# Scrape semua versi
scrape_all_versions(output_dir="bible-data", delay=0.5, format_output="json")

# Scrape versi tertentu saja
scrape_version(version="tb", output_dir="bible-data", delay=0.2, format_output="xml")
```

### Struktur Output

```
bible-data/
├── books.json
├── tb/
│   ├── bible-tb.json
│   └── bible-tb.xml
└── jawa/
    ├── bible-jawa.json
    └── bible-jawa.xml
```

**Format JSON:**
```json
{
  "version": "tb",
  "books": [
    {
      "no": 1,
      "name": "Kejadian",
      "abbr": "kej",
      "total_chapter": 50,
      "chapters": [
        {
          "chapter": 1,
          "verses": [
            {
              "verse": 1,
              "text": "Pada mulanya Allah menciptakan langit dan bumi.",
              "title": "Allah menciptakan langit dan bumi serta isinya"
            },
            {
              "verse": 2,
              "text": "Bumi belum berbentuk dan kosong...",
              "title": null
            }
          ]
        }
      ]
    }
  ]
}
```

> `title` adalah judul bagian/seksi. Hanya ayat pertama dalam satu seksi yang memiliki title; ayat-ayat berikutnya bernilai `null`.

---

### ⚠️ Disclaimer
Project ini dibuat untuk tujuan edukasi. Pastikan Anda mematuhi kebijakan penggunaan data dari [alkitab.mobi](https://alkitab.mobi) sebelum menggunakan data ini untuk tujuan komersial.
