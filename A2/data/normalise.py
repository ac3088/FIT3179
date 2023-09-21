import csv

SOURCE_FILE = "A2\data\\1900_2021_disasters.csv"
DESTINATION_FILE = 'A2\data\\1900_2021_normalised.csv'

def normalise_coord(coord):
    new_coord = coord.replace(" ", "")
    n = len(new_coord)

    if new_coord[n-1] in ['N', 'S', 'E', 'W']:
        new_coord = new_coord[:n-1]
    
    return new_coord

if __name__ == "__main__":
    with open(SOURCE_FILE, 'r', encoding='utf-8') as source, open(DESTINATION_FILE, 'w', encoding='utf-8') as destination:
        reader = csv.reader(source, delimiter=',')
        writer = csv.writer(destination, delimiter=',')
        for line in reader:
            if line[23] and line[24] and line[5]:
                line[23] = normalise_coord(line[23])
                line[24] = normalise_coord(line[24])
                if line[23] != 'Latitude': # this is so bad lmfao (handles the first row)
                    writer.writerow(line)
                else:
                    writer.writerow(line)
