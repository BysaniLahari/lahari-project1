import os

try:
    with open("C:\\Users\\Lahari\\Downloads\\youtube\\youtube_2025_dataset_202504061614.csv", 'r') as file:
        lines = file.readlines()
        print(f"Total lines read: {len(lines)}")
        print("First line:")
        print(lines[0])
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
