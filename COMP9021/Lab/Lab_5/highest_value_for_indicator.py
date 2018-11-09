# Uses Heath Nutrition and Population statistics, avalaible at
# http://datacatalog.worldbank.org, stored in the file HNP_Data.csv,
# assumed to be stored in the working directory.
# Prompts the user for an Indicator Name. If it exists and is associated with
# a numerical value for some countries or categories, for some the years 1960-2015,
# then finds out the maximum value, and outputs:
# - that value;
# - the years when that value was reached, from oldest to more recents years;
# - for each such year, the countries or categories for which that value was reached,
#   listed in lexicographic order.


import sys
import os
import csv


filename = 'HNP_Data.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

indicator_of_interest = input('Enter an Indicator Name: ')

# Insert your code here
file_array = []
with open(filename) as open_file:
    f_csv = csv.reader(open_file)
    headers = next(f_csv)
    for row in f_csv:
        for i in range(4, 60):
            if not row[i] == '':
                if str(float(row[i])) == row[i]:
                    row[i] = float(row[i])
                else:
                    row[i] = int(row[i])
            else:
                row[i] = 0
        file_array.append(row)
        

#print(file_array)

length = len(file_array)
target = []
for i in range(length):
    if file_array[i][2] == indicator_of_interest:
        target.append(file_array[i])

if len(target) == 0:
    max_value = None
else:
    max_value = max(target[0][4:])
    for i in range(1, len(target)):
        temp_max = max(target[i][4:])
        max_value = max(max_value, temp_max)

countries_for_max_value_per_year = dict()

for i in range(4, 60):
    temp = []
    for j in range(len(target)):
        if target[j][i] == max_value:
            temp.append(target[j][0])
    if len(temp) > 0:
        temp = sorted(temp)
        countries_for_max_value_per_year[i + 1956] = temp
     

if max_value is None:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is:', max_value)
    print('It was reached in these years, for these countries or categories:')
    for year in sorted(countries_for_max_value_per_year):
        print(f'    {year}: {countries_for_max_value_per_year[year]}')
