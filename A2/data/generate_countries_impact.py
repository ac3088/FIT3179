import csv

SOURCE_FILE = "A2\data\\natural-disasters.csv"
DESTINATION_FILE = 'A2\data\\1960-2020-countries-impact.csv'

col_titles = ['country', 'total_num_deaths', 'total_num_affected', 'total_cost']
cols = [0, 28, 30, 35]

countries = set()
rows_dict = dict()

def to_num(s):
    if not s:
        return 0
    return float(s)

def merge_rows(row1, row2):
    res = [row1[0]]

    n = len(row1)
    for i in range(1, n):
        res.append(to_num(row1[i]) + to_num(row2[i]))
    
    return res

if __name__ == "__main__":
    with open(SOURCE_FILE, 'r', encoding='utf-8') as source, open(DESTINATION_FILE, 'w', encoding='utf-8') as destination:
        reader = csv.reader(source, delimiter=',')
        writer = csv.writer(destination, delimiter=',')

        # Reading old dataset
        for line in reader:
            if line[0] != 'Country name':
                if to_num(line[1]) >= 1960:
                    countries.add(line[0]) # add country to set
                    current_row = [line[i] for i in cols]
                    if line[0] not in rows_dict:
                        rows_dict[line[0]] = current_row
                    else:
                        sum_row = rows_dict[line[0]]
                        new_row = merge_rows(current_row, sum_row)
                        rows_dict[line[0]] = new_row
        
        # Writing new dataset
        countries_sorted = sorted(list(countries))
        writer.writerow(col_titles)
        
        for c in countries_sorted:
            writer.writerow(rows_dict[c])

# Country_name = 0
# Total number of deaths = 28
# Total number of people affected = 30
# Total economic damage from disasters = 35

# Year = 1
