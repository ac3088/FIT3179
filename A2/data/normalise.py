import csv

SOURCE_FILE = "FIT3179\\A2\\data\\emdat-1960-2023.csv"
DESTINATION_FILE = 'FIT3179\\A2\\data\\1960-2023-impact-by-country.csv'

def to_num(s):
    if not s:
        return 0
    return float(s)

def merge_rows(row1, row2):
    res = [row1[0]]

    for i in range(1, len(row1)):
        res.append(to_num(row1[i]) + to_num(row2[i]))
    
    return res

countries = dict()
# Start Year = Index 25
# Country = Index 10
# Total deaths = Index 31
# Total Affected = Index 35
# Total Damage Adjusted ('000USD)= Index 41
col_titles = ['Country', 'Total Deaths', 'Total Affected', 'Total Damage Adjusted']
columns = [10, 31, 35, 41]

if __name__ == "__main__":
    with open(SOURCE_FILE, 'r', encoding='utf-8') as source, open(DESTINATION_FILE, 'w', encoding='utf-8') as destination:
        reader = csv.reader(source, delimiter=',')
        writer = csv.writer(destination, delimiter=',')

        for line in reader:
            if line[10] != 'Country':
                country = line[10]
                if country not in countries:
                    countries[country] = [country, to_num(line[31]), to_num(line[35]), to_num(line[41])]
                else:
                    old_row = countries[country]
                    current_row = [line[i] for i in columns]
                    new_row = merge_rows(old_row, current_row)
                    countries[country] = new_row

        countries_sorted = sorted([c for c in countries])
        writer.writerow(col_titles)
        for c in countries_sorted:
            writer.writerow(countries[c])
        