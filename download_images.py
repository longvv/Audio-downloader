import pandas as pd
from bing_image_downloader import downloader
import os

# Function to download image using bing-image-downloader
def fetch_image(query, output_dir):
    try:
        downloader.download(query, limit=1, output_dir=output_dir, adult_filter_off=True, force_replace=False, timeout=60)
        print(f"Downloaded image for {query}")
    except Exception as e:
        print(f"Could not download image for {query}: {e}")

# Read the CSV file
csv_file_path = 'words.csv'  # Replace with your CSV file path
output_dir = 'image_files'   # Directory to save image files

# Create the directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read CSV into DataFrame
df = pd.read_csv(csv_file_path)

# Assuming the words are in a column named 'word'
for index, row in df.iterrows():
    word = row['word']
    fetch_image(word, output_dir)

print("All images have been downloaded.")
