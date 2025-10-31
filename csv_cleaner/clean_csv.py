import pandas as pd
import numpy as np

input_file = r"C:\Users\jontt\OneDrive\Työpöytä\before.csv"
output_file = r"C:\Users\jontt\OneDrive\Työpöytä\after.csv"

# 1️⃣ Lue CSV turvallisesti
try:
    df = pd.read_csv(input_file, encoding="utf-8-sig")
except UnicodeDecodeError:
    df = pd.read_csv(input_file, encoding="latin1")
except pd.errors.ParserError:
    # jos kentissä on eri määrä sarakkeita → yritetään "engine='python'" ja delimiterin automaattista tunnistusta
    df = pd.read_csv(input_file, engine="python", sep=None)

# 2️⃣ Trim whitespace sarakkeiden nimistä ja arvoista
df.columns = df.columns.astype(str).str.strip()

for col in df.columns:
    if df[col].dtype == "object":
        # Poistaa alusta ja lopusta välilyönnit, korvaa "nan" ja "NaN" tyhjällä
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .replace(["nan", "NaN", "None"], "")
        )

# 3️⃣ Poista tyhjät rivit ja duplikaatit
df = df.drop_duplicates().dropna(how="all")

# 4️⃣ Poista sarakkeet, jotka ovat kokonaan tyhjiä
df = df.dropna(axis=1, how="all")

# 5️⃣ Korvaa jäljelle jääneet NaN-arvot tyhjällä merkkijonolla
df = df.fillna("")

# 6️⃣ Poista näkymättömät unicode-merkit (esim. zero-width space)
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].str.replace("\u200b", "", regex=False)

print(f"✅ Cleaned CSV: {len(df)} rows, {len(df.columns)} columns")
df.to_csv(output_file, index=False, encoding="utf-8-sig")
print(f"💾 Siistitty tiedosto tallennettu: {output_file}")
