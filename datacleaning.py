import pandas as pd


df = pd.read_csv("C:\\Users\\Lahari\\Downloads\\youtube\\youtube_2025_dataset_202504061614.csv")

print("Before cleaning:")
print(df.head())

df.drop_duplicates(inplace=True)


df['Total Subscribers'] = df['Total Subscribers'].fillna(0)
df['Members Count'] = df['Members Count'].fillna(0)
df['Avg Video Length (min)'] = df['Avg Video Length (min)'].fillna(df['Avg Video Length (min)'].mean())
df['AI Generated Content (%)'] = df['AI Generated Content (%)'].fillna(0)
df['Quantum Computing Topics'] = df['Quantum Computing Topics'].fillna(0)
df['Engagement Score'] = df['Engagement Score'].fillna(0)
df['Content Value Index'] = df['Content Value Index'].fillna(0)
df['Neural Interface Compatible'] = df['Neural Interface Compatible'].fillna('FALSE')
df['Metaverse Integration Level'] = df['Metaverse Integration Level'].fillna('None')
df['Holographic Content Rating'] = df['Holographic Content Rating'].fillna('Unknown')


df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

print("After cleaning:")
print(df.head())

df.to_csv("cleaned_youtube_2025.csv", index=False)

print("Cleaned data")
