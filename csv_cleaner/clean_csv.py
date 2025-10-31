import pandas as pd
df = pd.read_csv("input.csv", low_memory=False)
df.dropna(how="all", inplace=True)
df.drop_duplicates(inplace=True)
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')
df.to_csv("cleaned_data.csv", index=False)
print("✅ cleaned_data.csv created successfully")
