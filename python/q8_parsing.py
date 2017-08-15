# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

with open('football.csv') as football:
    football_reader = csv.DictReader(football)
    differentials = []
    for row in football_reader:
        team_name = row['Team']
        abs_diff = abs(int(row['Goals']) - int(row['Goals Allowed']))
        diff = int(row['Goals']) - int(row['Goals Allowed'])
        diff_tuple = (team_name, abs_diff, diff)
        differentials.append(diff_tuple)

sorted_absolute = sorted(differentials, key=lambda diff: diff[1])
sorted_overall = sorted(differentials, key=lambda diff: diff[2])

print(sorted_absolute[0][0] + " had the lowest absolute difference between 'for' and 'against' goals with " + str(sorted_absolute[0][1]))
print(sorted_overall[0][0] + " had the worst goal differential with " + str(sorted_overall[0][2]))