import pandas as pd
import mysql.connector
import numpy as np


df = pd.read_csv("cleaned_youtube_2025.csv")


df.replace([np.nan, 'nan', 'NaN', 'NAN'], 0, inplace=True)

conn = mysql.connector.connect(
    host="localhost",
    user="root",            
    password="lahari",
    database="youtube_data_analysis"  
)
cursor = conn.cursor()


query = """
INSERT INTO youtube_data (
    channel_name, youtuber_name, total_videos, best_video, avg_video_length,
    total_subscribers, members_count, ai_generated_content, neural_interface_compatible,
    metaverse_integration_level, quantum_computing_topics, holographic_content_rating,
    engagement_score, content_value_index
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


for idx, row in df.iterrows():
    try:
        cleaned_row = [0 if str(x).lower() == 'nan' else x for x in row]
        cursor.execute(query, tuple(cleaned_row))
    except Exception as e:
        print(f"Error at row {idx + 1}", e)

conn.commit()
print("Data inserted successfully.")
cursor.close()
conn.close()
