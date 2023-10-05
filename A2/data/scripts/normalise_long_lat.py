"""
Running this file just removes all the rows in 'emdat-1960-2023.csv' that don't have 'Latitude' or 'Longitude' values.
This normalised dataset is only used for the proportional symbol map.
"""

import csv

SOURCE_FILE = "A2\\data\\emdat-1960-2023.csv"
DESTINATION_FILE = 'A2\\data\\emdat-normalised-long-lat.csv'

# Latitude = Index 22
# Longitude = Index  23

if __name__ == "__main__":
    with open(SOURCE_FILE, 'r', encoding='utf-8') as source, open(DESTINATION_FILE, 'w', newline='', encoding='utf-8') as destination:
        reader = csv.reader(source, delimiter=',')
        writer = csv.writer(destination, delimiter=',')

        for line in reader:
            if line[22] and line[23]:
                writer.writerow(line)