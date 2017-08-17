import re
import csv


def find_degrees(faculty_list):
    degrees = {}
    for prof in faculty_list:
        if prof[' degree'] != '0':
            prof_degrees = prof[' degree'].split()
            for item in prof_degrees:
                degree = re.sub(r'\W+','',item)
                if degree in degrees:
                    degrees[degree] = degrees[degree] + 1
                else:
                    degrees[degree] = 1
    return(degrees)

def find_titles(faculty_list):
    titles = {}
    for prof in faculty_list:
        title = prof[' title'][:-17]
        if title in titles:
            titles[title] = titles[title] + 1
        else:
            titles[title] = 1
    return(titles)

def find_emails(faculty_list):
    emails = []
    for prof in faculty_list:
        email = prof[' email']
        emails.append(email)
    return(emails)

def find_domains(faculty_list):
    domains = set()
    for prof in faculty_list:
        at_pos = prof[' email'].find('@')
        domain = prof[' email'][(at_pos+1):]
        domains.add(domain)
    return list(domains)

with open('faculty.csv') as faculty:
    data = list(csv.DictReader(faculty))
    upenn_faculty = [dict(x) for x in data]

print('Degrees and their distribution: ' + str(find_degrees(upenn_faculty)))
print('Titles and their distribution: ' + str(find_titles(upenn_faculty)))
print('List of emails: ' + str(find_emails(upenn_faculty)))
print('List of domains: ' + str(find_domains(upenn_faculty)))
