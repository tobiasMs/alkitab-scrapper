# scrape_bible_sabda.py

import json
import time
import argparse
import requests
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.dom import minidom


BASE_URL = "https://alkitab.sabda.org/api/passage.php"
VERSIONS = ["tb", "jawa"]


BOOKS = [
    {"no": 1, "abbr": "kej", "name": "Kejadian", "chapter": 50},
    {"no": 2, "abbr": "kel", "name": "Keluaran", "chapter": 40},
    {"no": 3, "abbr": "ima", "name": "Imamat", "chapter": 27},
    {"no": 4, "abbr": "bil", "name": "Bilangan", "chapter": 36},
    {"no": 5, "abbr": "ula", "name": "Ulangan", "chapter": 34},
    {"no": 6, "abbr": "yos", "name": "Yosua", "chapter": 24},
    {"no": 7, "abbr": "hak", "name": "Hakim-hakim", "chapter": 21},
    {"no": 8, "abbr": "rut", "name": "Rut", "chapter": 4},
    {"no": 9, "abbr": "1sa", "name": "1 Samuel", "chapter": 31},
    {"no": 10, "abbr": "2sa", "name": "2 Samuel", "chapter": 24},
    {"no": 11, "abbr": "1ra", "name": "1 Raja-raja", "chapter": 22},
    {"no": 12, "abbr": "2ra", "name": "2 Raja-raja", "chapter": 25},
    {"no": 13, "abbr": "1ta", "name": "1 Tawarikh", "chapter": 29},
    {"no": 14, "abbr": "2ta", "name": "2 Tawarikh", "chapter": 36},
    {"no": 15, "abbr": "ezr", "name": "Ezra", "chapter": 10},
    {"no": 16, "abbr": "neh", "name": "Nehemia", "chapter": 13},
    {"no": 17, "abbr": "est", "name": "Ester", "chapter": 10},
    {"no": 18, "abbr": "ayb", "name": "Ayub", "chapter": 42},
    {"no": 19, "abbr": "maz", "name": "Mazmur", "chapter": 150},
    {"no": 20, "abbr": "ams", "name": "Amsal", "chapter": 31},
    {"no": 21, "abbr": "pkh", "name": "Pengkhotbah", "chapter": 12},
    {"no": 22, "abbr": "kda", "name": "Kidung Agung", "chapter": 8},
    {"no": 23, "abbr": "yes", "name": "Yesaya", "chapter": 66},
    {"no": 24, "abbr": "yer", "name": "Yeremia", "chapter": 52},
    {"no": 25, "abbr": "rat", "name": "Ratapan", "chapter": 5},
    {"no": 26, "abbr": "yeh", "name": "Yehezkiel", "chapter": 48},
    {"no": 27, "abbr": "dan", "name": "Daniel", "chapter": 12},
    {"no": 28, "abbr": "hos", "name": "Hosea", "chapter": 14},
    {"no": 29, "abbr": "yoe", "name": "Yoel", "chapter": 3},
    {"no": 30, "abbr": "amo", "name": "Amos", "chapter": 9},
    {"no": 31, "abbr": "oba", "name": "Obaja", "chapter": 1},
    {"no": 32, "abbr": "yun", "name": "Yunus", "chapter": 4},
    {"no": 33, "abbr": "mik", "name": "Mikha", "chapter": 7},
    {"no": 34, "abbr": "nah", "name": "Nahum", "chapter": 3},
    {"no": 35, "abbr": "hab", "name": "Habakuk", "chapter": 3},
    {"no": 36, "abbr": "zef", "name": "Zefanya", "chapter": 3},
    {"no": 37, "abbr": "hag", "name": "Hagai", "chapter": 2},
    {"no": 38, "abbr": "zak", "name": "Zakharia", "chapter": 14},
    {"no": 39, "abbr": "mal", "name": "Maleakhi", "chapter": 4},
    {"no": 40, "abbr": "mat", "name": "Matius", "chapter": 28},
    {"no": 41, "abbr": "mar", "name": "Markus", "chapter": 16},
    {"no": 42, "abbr": "luk", "name": "Lukas", "chapter": 24},
    {"no": 43, "abbr": "yoh", "name": "Yohanes", "chapter": 21},
    {"no": 44, "abbr": "kis", "name": "Kisah Para Rasul", "chapter": 28},
    {"no": 45, "abbr": "rom", "name": "Roma", "chapter": 16},
    {"no": 46, "abbr": "1ko", "name": "1 Korintus", "chapter": 16},
    {"no": 47, "abbr": "2ko", "name": "2 Korintus", "chapter": 13},
    {"no": 48, "abbr": "gal", "name": "Galatia", "chapter": 6},
    {"no": 49, "abbr": "efe", "name": "Efesus", "chapter": 6},
    {"no": 50, "abbr": "fil", "name": "Filipi", "chapter": 4},
    {"no": 51, "abbr": "kol", "name": "Kolose", "chapter": 4},
    {"no": 52, "abbr": "1te", "name": "1 Tesalonika", "chapter": 5},
    {"no": 53, "abbr": "2te", "name": "2 Tesalonika", "chapter": 3},
    {"no": 54, "abbr": "1ti", "name": "1 Timotius", "chapter": 6},
    {"no": 55, "abbr": "2ti", "name": "2 Timotius", "chapter": 4},
    {"no": 56, "abbr": "tit", "name": "Titus", "chapter": 3},
    {"no": 57, "abbr": "flm", "name": "Filemon", "chapter": 1},
    {"no": 58, "abbr": "ibr", "name": "Ibrani", "chapter": 13},
    {"no": 59, "abbr": "yak", "name": "Yakobus", "chapter": 5},
    {"no": 60, "abbr": "1pe", "name": "1 Petrus", "chapter": 5},
    {"no": 61, "abbr": "2pe", "name": "2 Petrus", "chapter": 3},
    {"no": 62, "abbr": "1yo", "name": "1 Yohanes", "chapter": 5},
    {"no": 63, "abbr": "2yo", "name": "2 Yohanes", "chapter": 1},
    {"no": 64, "abbr": "3yo", "name": "3 Yohanes", "chapter": 1},
    {"no": 65, "abbr": "yud", "name": "Yudas", "chapter": 1},
    {"no": 66, "abbr": "wah", "name": "Wahyu", "chapter": 22},
]


def parse_sabda_xml(xml_text, book, chapter, version):
    root = ET.fromstring(xml_text)

    verses = []

    for verse in root.findall(".//verse"):
        number = verse.findtext("number")
        text = verse.findtext("text") or ""
        title = verse.findtext("title")

        verses.append({
            "verse": int(number) if number else None,
            "text": text.strip(),
            "title": title.strip() if title else None,
        })

    return {
        "book": book["name"],
        "abbr": book["abbr"],
        "chapter": chapter,
        "version": version,
        "verses": verses,
    }


def fetch_chapter(book, chapter, version, timeout=20):
    passage = f"{book['abbr']} {chapter}"

    response = requests.get(
        BASE_URL,
        params={
            "passage": passage,
            "ver": version,
        },
        timeout=timeout,
    )

    response.raise_for_status()

    return parse_sabda_xml(
        xml_text=response.text,
        book=book,
        chapter=chapter,
        version=version,
    )


def save_json(data, path):
    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def save_xml(data, path):
    path.parent.mkdir(parents=True, exist_ok=True)

    root = ET.Element("bible")
    root.set("version", data["version"])

    for book in data["books"]:
        book_el = ET.SubElement(root, "book")
        book_el.set("no", str(book["no"]))
        book_el.set("name", book["name"])
        book_el.set("abbr", book["abbr"])
        book_el.set("total_chapter", str(book["total_chapter"]))

        for chapter in book["chapters"]:
            chapter_el = ET.SubElement(book_el, "chapter")
            chapter_el.set("number", str(chapter["chapter"]))

            for verse in chapter["verses"]:
                verse_el = ET.SubElement(chapter_el, "verse")
                verse_el.set("number", str(verse["verse"]))

                if verse.get("title"):
                    title_el = ET.SubElement(verse_el, "title")
                    title_el.text = verse["title"]

                text_el = ET.SubElement(verse_el, "text")
                text_el.text = verse["text"]

    raw_xml = ET.tostring(root, encoding="utf-8")
    pretty_xml = minidom.parseString(raw_xml).toprettyxml(indent="  ")

    path.write_text(pretty_xml, encoding="utf-8")


def scrape_version(version, output_dir, delay, format_output):
    output_dir = Path(output_dir)

    bible_data = {
        "version": version,
        "books": [],
    }

    print("=" * 60)
    print(f"SCRAPING VERSION: {version.upper()}")
    print("=" * 60)

    for book in BOOKS:
        print(f"\nScraping {book['name']} ({book['abbr']})")

        book_data = {
            "no": book["no"],
            "name": book["name"],
            "abbr": book["abbr"],
            "total_chapter": book["chapter"],
            "chapters": [],
        }

        for chapter in range(1, book["chapter"] + 1):
            try:
                chapter_data = fetch_chapter(
                    book=book,
                    chapter=chapter,
                    version=version,
                )

                book_data["chapters"].append({
                    "chapter": chapter_data["chapter"],
                    "verses": chapter_data["verses"],
                })

                print(f"  OK {book['abbr']} {chapter}")

                if delay > 0:
                    time.sleep(delay)

            except Exception as e:
                print(f"  FAILED {book['abbr']} {chapter}: {e}")

        bible_data["books"].append(book_data)

    version_dir = output_dir / version

    if format_output in ["json", "both"]:
        save_json(
            bible_data,
            version_dir / f"bible-{version}.json",
        )

    if format_output in ["xml", "both"]:
        save_xml(
            bible_data,
            version_dir / f"bible-{version}.xml",
        )

    print(f"\nDONE VERSION: {version.upper()}")


def scrape_all_versions(output_dir="bible-data", delay=0.3, format_output="both"):
    output_dir = Path(output_dir)

    save_json(
        BOOKS,
        output_dir / "books.json",
    )

    for version in VERSIONS:
        scrape_version(
            version=version,
            output_dir=output_dir,
            delay=delay,
            format_output=format_output,
        )

    print("\n" + "=" * 60)
    print("SEMUA DATA SELESAI DI-SCRAPE")
    print("=" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scrape Alkitab SABDA API ke file lokal JSON/XML untuk versi TB dan Jawa."
    )

    parser.add_argument(
        "--output",
        default="bible-data",
        help="Folder output. Default: bible-data",
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=0.3,
        help="Delay antar request dalam detik. Default: 0.3",
    )

    parser.add_argument(
        "--format",
        default="both",
        choices=["json", "xml", "both"],
        help="Format output: json, xml, atau both. Default: both",
    )

    args = parser.parse_args()

    scrape_all_versions(
        output_dir=args.output,
        delay=args.delay,
        format_output=args.format,
    )