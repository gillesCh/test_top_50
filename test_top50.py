# -*- coding: utf-8 -*-
"""test_top50.ipynb
"""

#import libraries
import os
from collections import defaultdict
from datetime import datetime, timedelta

# Constants
LOGS_FOLDER = "/content/"  # Path to the folder containing log files
OUTPUT_FOLDER = "/content/"  # Path to the output folder
DAYS_TO_CONSIDER = 7
TOP_SONGS_COUNT = 50  # Number of top songs to include in the output

def generate_top50_file(counts, output_file):
    with open(output_file, "w") as file:
        for key, value in counts.items():
            # Sort the songs by count and get the top 50
            top50_songs = sorted(value.items(), key=lambda x: x[1], reverse=True)[:TOP_SONGS_COUNT]
            # Format the top songs as "song:count"
            song_list = ",".join([f"{song}:{count}" for song, count in top50_songs])
            file.write(f"{key}|{song_list}\n")

def process_logs():
    # Aggregate data for country top 50
    country_counts = defaultdict(lambda: defaultdict(int))

    # Aggregate data for user top 50
    user_counts = defaultdict(lambda: defaultdict(int))

    # Process log files for the last 7 days
    for day in range(DAYS_TO_CONSIDER, 0, -1):
        # Get the date for the log file
        date = (datetime.now() - timedelta(days=day)).strftime("%Y%m%d")
        # Construct the path to the log file
        log_file_path = os.path.join(LOGS_FOLDER, f"listen-{date}.log")

        if not os.path.isfile(log_file_path):
            continue
        # Read each line in the log file
        with open(log_file_path, "r") as log_file:
            for line in log_file:
                try:
                    sng_id, user_id, country = line.strip().split("|")
                    country_counts[country][sng_id] += 1
                    user_counts[user_id][sng_id] += 1
                except:
                    continue

    # Generate country top 50 file
    country_top50_file_path = os.path.join(OUTPUT_FOLDER, f"country_top50_{date}.txt")  # Construct the path for the output file
    generate_top50_file(country_counts, country_top50_file_path)

    # Generate user top 50 file (optional)
    user_top50_file_path = os.path.join(OUTPUT_FOLDER, f"user_top50_{date}.txt")  # Construct the path for the output file
    generate_top50_file(user_counts, user_top50_file_path)




# Execute the process
process_logs()
