import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='lahari',
    database='youtube_data_analysis'
)
cursor = conn.cursor()

create_table = """
create table youtube_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    channel_name varchar(255),
    youtuber_name varchar(255),
    total_videos int,
    best_video varchar(255),
    avg_video_length float,
    total_subscribers bigint,
    members_count int,
    ai_generated_content float,
    neural_interface_compatible boolean,
    metaverse_integration_level varchar(255),
    quantum_computing_topics int,
    holographic_content_rating varchar(255),
    engagement_score float,
    content_value_index float
);
"""
cursor.execute(create_table)
conn.commit()
print("Table Created")