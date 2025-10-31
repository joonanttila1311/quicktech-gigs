import os, shutil
from pathlib import Path

target_folder = Path.cwd()
print(f"📁 Organizing folder: {target_folder}")

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


print("🎉 Done!")
input("Press Enter to exit...")
