
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="lahari",
    database="youtube_data_analysis1"
)
cursor = conn.cursor()

# total number of videos
cursor.execute("SELECT SUM(total_videos) FROM youtube_data1")
total_videos = cursor.fetchone()[0]
print("Total number of videos:", total_videos)

# most subscribed channel
cursor.execute("""
SELECT channel_name, youtuber_name, total_subscribers
FROM youtube_data1
ORDER BY total_subscribers DESC
LIMIT 1
""")
result = cursor.fetchone()
print("Most Subscribed Channel:", result)

# average engagement score
cursor.execute("SELECT AVG(engagement_score) FROM youtube_data1")
avg_engagement = cursor.fetchone()[0]
print("Average Engagement Score:", round(avg_engagement, 2))

# average content value index
cursor.execute("SELECT AVG(content_value_index) FROM youtube_data1")
avg_value = cursor.fetchone()[0]
print("Average Content Value Index:", round(avg_value, 2))

# top 5 youtubers by ai-generated content
cursor.execute("""
SELECT youtuber_name, ai_generated_content
FROM youtube_data1
ORDER BY ai_generated_content DESC
LIMIT 5
""")
top_ai = cursor.fetchall()
print("Top 5 Youtubers by AI-Generated Content:")
for row in top_ai:
    print(row)

#total videos by metaverse integration level
cursor.execute("""
SELECT metaverse_integration_level, SUM(total_videos)
FROM youtube_data1
GROUP BY metaverse_integration_level
""")
metaverse_videos = cursor.fetchall()
print("\nTotal Videos by Metaverse Level:")
for row in metaverse_videos:
    print(row)

# average engagement score by channel
cursor.execute("""
SELECT channel_name, AVG(engagement_score) AS avg_engagement
FROM youtube_data1
GROUP BY channel_name
ORDER BY avg_engagement DESC
LIMIT 5
""")
engagement_top = cursor.fetchall()
print("\nTop 5 Channels by Average Engagement:")
for row in engagement_top:
    print(row)

#top 5 channels by quantum topics
cursor.execute("""
SELECT channel_name, quantum_computing_topics
FROM youtube_data1
ORDER BY quantum_computing_topics DESC
LIMIT 5
""")
quantum_top = cursor.fetchall()
print("\nTop 5 Channels by Quantum Topics Covered:")
for row in quantum_top:
    print(row)

#top 5 channels by total videos
cursor.execute("""
SELECT channel_name, total_videos
FROM youtube_data1
ORDER BY total_videos DESC
LIMIT 5
""")
most_videos = cursor.fetchall()
print("\nTop 5 Channels by Total Videos:")
for row in most_videos:
    print(row)


cursor.close()
conn.close()
