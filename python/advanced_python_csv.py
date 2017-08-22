import csv

#From Q1
def find_emails(faculty_list):
    emails = []
    for prof in faculty_list:
        email = prof[' email']
        emails.append(email)
    return(emails)

with open('faculty.csv') as faculty:
    data = list(csv.DictReader(faculty))
    upenn_faculty = [dict(x) for x in data]

email_list = find_emails(upenn_faculty)

with open('emails.csv', 'w', newline='') as csvfile:
    emails = csv.writer(csvfile, delimiter=' ')
    for email in email_list:
        emails.writerow(email)