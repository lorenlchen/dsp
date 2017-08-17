import re
import csv

with open('faculty.csv') as faculty:
    upenn_faculty = csv.DictReader(faculty)
    degrees = {}

    for prof in upenn_faculty:
        if prof[' degree'] != '0':
            prof_degrees = prof[' degree'].split()
            for item in prof_degrees:
                degree = re.sub(r'\W+','',item)
                if degree in degrees:
                    degrees[degree] = degrees[degree] + 1
                else:
                    degrees[degree] = 1

print(degrees)