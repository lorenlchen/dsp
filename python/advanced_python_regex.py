import re
import csv

with open('faculty.csv') as faculty:
    upenn_faculty = csv.DictReader(faculty)
    degrees = set()

    for prof in upenn_faculty:
        if prof[' degree'] != '0':
            prof_degrees = prof[' degree'].split()
            for item in prof_degrees:
                degrees.add(re.sub(r'\W+','',item))

print(degrees)