import csv

SOURCE_FILE = "A2\data\\natural-disasters.csv"
DESTINATION_FILE = 'A2\data\\1960-2020-dtype-impact.csv'

cols = [1, 2, 6, 9, 15, 17, 22, 41, 43, 48, 54, 56, 61, 67, 69, 74, 80, 82, 87, 93, 
        95, 100, 106, 108, 113, 119, 121, 126, 132, 134, 139, 145, 147, 152]
col_titles = ['year',
              'drought_deaths',
              'n_affected_drought',
              'drought_costs',
              'eq_deaths',
              'n_affected_eq',
              'eq_costs',
              'volc_deaths',
              'n_affected_volc',
              'volc_costs',
              'flood_deaths',
              'n_affected_flood',
              'flood_costs',
              'mass_movement_deaths',
              'n_affected_mass_movement',
              'mass_movement_costs',
              'storm_deaths',
              'n_affected_storm',
              'storm_costs',
              'landslide_deaths',
              'n_affected_landslide',
              'landslide_costs',
              'fog_deaths',
              'n_affected_fog',
              'fog_costs',
              'wildfire_deaths',
              'n_affected_wildfire',
              'wildfire_costs',
              'ext_temp_deaths',
              'n_affected_ext_temp',
              'ext_temp_costs',
              'glacial_outburst_deaths',
              'n_affected_glacial_outburst',
              'glacial_outburst_costs',]

years = set()
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
                    years.add(line[1]) # add year to set
                    current_row = [line[i] for i in cols]
                    if line[1] not in rows_dict:
                        rows_dict[line[1]] = current_row
                    else:
                        sum_row = rows_dict[line[1]]
                        new_row = merge_rows(current_row, sum_row)
                        rows_dict[line[1]] = new_row
        
        # Writing dataset
        years_sorted = sorted(list(years))
        writer.writerow(col_titles)

        for y in years_sorted:
            writer.writerow(rows_dict[y])

# Year = 1
# num deaths from drought = 2
# num affected by drought = 6
# cost of drought = 9

# eq deaths = 15
# num affected by eq = 17
# cost of eq = 22

# deaths from volcano = 41
# num affeacted by volcano = 43
# cost of volcano = 48

# flood deaths = 54
# num affected by floods = 56
# cost of floods = 61

# mass movement deaths = 67
# num affected by mass movements = 69
# cost of mass movements = 74

# storm deaths = 80
# num affected by storms = 82
# cost of storms = 87

# landslide deaths = 93
# num affected by landslides = 95
# cost of landslides = 100

# fog deaths = 106
# affected by fog = 108
# cost of fog = 113

# wildfire deaths = 119
# num affected by wildfire = 121
# cost of wildfires = 126

# extreme temp deaths = 132
# num affected by extreme temp = 134
# cost of extreme temp = 139

# glacial lake outburst deaths = 145
# num affected by glacial lake outburst = 147
# 152 = cost of glacial lake outbursts

