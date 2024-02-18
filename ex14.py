import os
import pandas as pd

all_prayer_timings = []

for filename in os.listdir("json_files"):

    # Read the JSON file into a DataFrame
    print(filename)
    df = pd.read_json("json_files/" + filename)

    # Extract the timings data
    timings = df['data']['timings']

    # Extract the required prayer timings
    prayer_timings = {
            'Fajr': timings['Fajr'],
            'Dhuhr': timings['Dhuhr'],
            'Asr': timings['Asr'],
            'Maghrib': timings['Maghrib'],
            'Isha': timings['Isha']
        }

    all_prayer_timings.append(prayer_timings)

combined_df = pd.DataFrame(all_prayer_timings)

print(combined_df)

combined_df.to_csv("adhan.csv")