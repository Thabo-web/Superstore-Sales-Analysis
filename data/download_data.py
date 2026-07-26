"""
data/download_data.py
Idempotent helper to download the Global Superstore Excel file into data/raw/
Run: python data/download_data.py
"""
from pathlib import Path
import requests

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)
OUT = RAW_DIR / "Global_Superstore.xlsx"
URL = "https://github.com/Christelle-Younan/The-Global-Superstore-Dataset-with-Excel/blob/main/Global%20Superstore.xlsx?raw=true"

if OUT.exists():
    print(f"File already exists at {OUT} — skipping download")
else:
    print(f"Downloading dataset from {URL} -> {OUT}")
    r = requests.get(URL)
    r.raise_for_status()
    OUT.write_bytes(r.content)
    print("Download complete")
