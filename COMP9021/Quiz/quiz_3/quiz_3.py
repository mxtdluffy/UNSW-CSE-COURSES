# Uses Global Temperature Time Series, avalaible at
# http://data.okfn.org/data/core/global-temp, stored in the file monthly_csv.csv,
# assumed to be stored in the working directory.
# Prompts the user for the source, a year or a range of years, and a month.
# - The source is either GCAG or GISTEMP.
# - The range of years is of the form xxxx -- xxxx (with any number of spaces,
#   possibly none, around --) and both years can be the same,
#   or the first year can be anterior to the second year,
#   or the first year can be posterior to the first year.
# We assume that the input is correct and the data for the requested month
# exist for all years in the requested range.
# Then outputs:
# - The average of the values for that source, for this month, for those years.
# - The list of years (in increasing order) for which the value is larger than that average.
# 
# Written by Jingyun Shen and Eric Martin for COMP9021


import sys
import os
import csv


filename = 'monthly_csv.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

source = input('Enter the source (GCAG or GISTEMP): ')
year_or_range_of_years = input('Enter a year or a range of years in the form XXXX -- XXXX: ')
month = input('Enter a month: ')
average = 0
years_above_average = []

# REPLACE THIS COMMENT WITH YOUR CODE
data = []
year_month = []
month_transfer = {'January':'01', 'February':'02', 'March':'03', 'April': '04',\
        'May':'05', 'June':'06', 'July':'07', 'August':'08', 'September':'09',\
        'October':'10', 'November':'11', 'December':'12'}
month_nb = month_transfer[month]

year_list = list(filter(None, year_or_range_of_years.split('--')))
if len(year_list) == 1:
    year_list[0] = int(year_list[0])
    year_list.append(year_list[0])
else:
    for i in range(2):
        year_list[i] = int(year_list[i])
year_list = sorted(year_list)

with open(filename) as open_file:
    for line in open_file:
        if line.startswith('Source'):
            continue
        each_line = line.split(',')
        cur_date = each_line[1].split('-')
        data.append((each_line[0], float(each_line[2][:-1])))
        year_month.append((int(cur_date[0]), cur_date[1], cur_date[2]))

all_value = []
sum_of_value = 0
for i in range(len(data)):
    if year_month[i][0] >= year_list[0] and year_month[i][0] <= year_list[1] \
       and year_month[i][1] == month_nb and data[i][0] == source:
        all_value.append((year_month[i][0], data[i][1]))
        sum_of_value += data[i][1]

average = sum_of_value / len(all_value)

for i in range(len(all_value)):
    if all_value[i][1] > average:
        years_above_average.append(all_value[i][0])

years_above_average = sorted(years_above_average)


print(f'The average anomaly for {month} in this range of years is: {average:.2f}.')
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)
