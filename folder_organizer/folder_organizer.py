import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import shutil
import socket

__author__ = "Joona Anttila / QuickTech"
__version__ = "1.0.0"
__description__ = (
    "Turvallinen työkalu tiedostojen automaattiseen siirtoon. "
    "Ei yhteyksissä Internetiin tai datan keruuseen. "
    "|| Safe offline file organizer - no internet access or data collection."
)

# Näytetään tiedot käyttäjälle alussa
print("=" * 60)
print(f"📦 {__description__}")
print(f"👤 Tekijä / Author: {__author__}")
print(f"🔢 Versio / Version: {__version__}")
print("=" * 60)

socket.setdefaulttimeout(0.1)

# Avaa kansiovalikko
root = tk.Tk()
root.withdraw()  # piilottaa pääikkunan
folder_selected = filedialog.askdirectory(title="Valitse kansio järjesteltäväksi")

proceed = input("⚠️ Haluatko varmasti järjestää tämän kansion? (k/e) | Are you sure you want to organize this folder? (y/n): ")
if proceed.lower() not in ['y', 'k']:
    print("❌ Peruutettu / Cancelled by user.")
    exit()

if not folder_selected:
    print("❌ Et valinnut kansiota – ohjelma suljetaan.")
    exit()

target_folder = Path(folder_selected)
print(f"📁 Järjestellään kansio: {target_folder}")


category_map = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt"],
    "Data": [".csv", ".xlsx", ".xls", ".json"],
    "Media": [".mp3", ".wav", ".mp4", ".mov", ".mkv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".php", ".c", ".cpp", ".java"],
}

this_script = Path(__file__).resolve()

for file in target_folder.iterdir():
    # Älä siirrä itse ohjelmaa
    if file.resolve() == this_script:
        continue

    if file.is_file():
        ext = file.suffix.lower()
        for category, extensions in category_map.items():
            if ext in extensions:
                dest = target_folder / category
                dest.mkdir(exist_ok=True)
                shutil.move(str(file), dest / file.name)
                print(f"✅ Moved {file.name} → {category}/")
                break
        else:
            # Jos ei kuulu mihinkään yleiseen kategoriaan
            ext_folder = target_folder / ext.replace('.', '').upper()
            ext_folder.mkdir(exist_ok=True)
            shutil.move(str(file), ext_folder / file.name)
            print(f"📦 Moved {file.name} → {ext_folder.name}/")
            print("🎉 Folder organization complete — no files deleted.")


print("🎉 Done!")
input("Press Enter to exit...")
