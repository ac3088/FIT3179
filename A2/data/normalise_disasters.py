import csv

SOURCE_FILE = "FIT3179\\A2\\data\\emdat-1960-2023.csv"
DESTINATION_FILE = 'FIT3179\\A2\\data\\emdat-1960-2023-normalised.csv'

# Latitude = Index 22
# Longitude = Index  23

if __name__ == "__main__":
    with open(SOURCE_FILE, 'r', encoding='utf-8') as source, open(DESTINATION_FILE, 'w', newline='', encoding='utf-8') as destination:
        reader = csv.reader(source, delimiter=',')
        writer = csv.writer(destination, delimiter=',')

        for line in reader:
            if line[22] and line[23]:
                writer.writerow(line)