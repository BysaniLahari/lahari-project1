import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_youtube_2025.csv")

df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

ai_col = 'ai_generated_content_(%)'
df.rename(columns={ai_col: 'ai_generated_content'}, inplace=True)

# Top 5 Trending Videos
top_videos = df.sort_values(by='engagement_score', ascending=False).head()

plt.figure(figsize=(10, 5))
plt.bar(top_videos['best_video'], top_videos['engagement_score'], color='skyblue')
plt.title('Top 5 Trending Videos by Engagement Score')
plt.xlabel('Best Video')
plt.ylabel('Engagement Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Avg Engagement by Metaverse Level
category_group = df.groupby('metaverse_integration_level')['engagement_score'].mean()

plt.figure(figsize=(8, 5))
category_group.plot(kind='bar', color='lightgreen')
plt.title('Avg Engagement Score by Metaverse Integration Level')
plt.xlabel('Metaverse Integration Level')
plt.ylabel('Engagement Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# AI-Generated Content Distribution
ai_bins = pd.cut(df['ai_generated_content'], bins=[0, 25, 50, 75, 100], labels=['0-25%', '25-50%', '50-75%', '75-100%'])
ai_dist = ai_bins.value_counts().sort_index()

plt.figure(figsize=(6, 6))
plt.pie(ai_dist, labels=ai_dist.index, autopct='%1.1f%%', startangle=140)
plt.title('AI-Generated Content Distribution')
plt.axis('equal')
plt.show()


#Distribution of Quantum Computing Topics Covered.
plt.figure(figsize=(8, 5))
counts = df['quantum_computing_topics'].value_counts().sort_index()
plt.bar(counts.index, counts.values, color='green')
plt.title('Distribution of Quantum Computing Topics Covered')
plt.xlabel('Number of Topics Covered')
plt.ylabel('Number of Channels')
plt.tight_layout()
plt.show()
