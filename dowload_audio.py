import pandas as pd
from gtts import gTTS
import os

# Function to convert text to speech and save as mp3
def text_to_speech(word, file_name):
    tts = gTTS(word)
    tts.save(file_name)

# Read the CSV file
csv_file_path = 'words.csv'  # Replace with your CSV file path
output_dir = 'audio_files'   # Directory to save audio files

# Create the directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read CSV into DataFrame
df = pd.read_csv(csv_file_path)

# Assuming the words are in a column named 'word'
for index, row in df.iterrows():
    word = row['word']
    file_name = os.path.join(output_dir, f"{word}.mp3")
    text_to_speech(word, file_name)
    print(f"Saved {word} as {file_name}")

print("All words have been converted to audio files.")
