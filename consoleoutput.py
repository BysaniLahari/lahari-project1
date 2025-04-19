from sqlalchemy import create_engine
import pandas as pd


engine = create_engine('mysql+mysqlconnector://root:lahari@localhost:3306/youtube_data_analysis')


query = "select * from youtube_data" 
df = pd.read_sql(query, engine)
print(df)


# summary statistics
print("\n summary statistics:")
print(df.describe())

# top trending videos (based on engagement score)
print("\n top trending videos:")
top_videos = df.sort_values(by='engagement_score', ascending=False)[['channel_name', 'best_video', 'engagement_score']].head()
print(top_videos)

# category-wise comparison
print("\n category wise comparisons")
category_group = df.groupby('metaverse_integration_level')[['avg_video_length', 'total_subscribers', 'engagement_score']].mean()
print(category_group)

# channels with high content value index
print("\n Channels with high content value index (>90):")
high_value = df[df['content_value_index'] > 90][['channel_name', 'content_value_index']]
print(high_value)

# count of channels using quantum computing topics
quantum_count = df['quantum_computing_topics'].sum()
print(f"\n Channels discussing Quantum Computing Topics: {quantum_count}")

# channels using ai-generated content > 80%
ai = df[df['ai_generated_content'] > 80][['channel_name', 'ai_generated_content']]
print("\n Channels Heavily Using AI-Generated Content (>80%):")
print(ai)
