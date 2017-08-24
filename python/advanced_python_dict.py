import csv

def split_names(faculty_list):
    for prof in faculty_list:
        name = prof['name'].rsplit(' ', 1)
        prof['first_name'] = name[0]
        prof['last_name'] = name[1]
    return faculty_list


#Q6
def create_faculty_dict(faculty_list):
    faculty_dict = {}
    for prof in faculty_list:
        prof_info = [prof[' degree'], prof[' title'][:-17], prof[' email']]
        last_name = prof['last_name']
        if last_name not in faculty_dict:
            faculty_dict[last_name] = [prof_info]
        else:
            faculty_dict[last_name].append(prof_info)
    return faculty_dict

#Q7
def create_professor_dict(faculty_list):
    professor_dict = {}
    for prof in faculty_list:
        name = (prof['first_name'], prof['last_name'])
        info = [prof[' degree'], prof[' title'][:-17], prof[' email']]
        if name not in professor_dict:
            professor_dict[name] = info
    return professor_dict


with open('faculty.csv') as faculty:
    data = list(csv.DictReader(faculty))
    upenn_faculty = [dict(x) for x in data]


faculty_names = split_names(upenn_faculty)
for prof in faculty_names:
    prof[' degree'] = prof[' degree'].lstrip()

faculty_dict = create_faculty_dict(faculty_names)
professor_dict = create_professor_dict(faculty_names)
print("Q6. " + str({x: faculty_dict[x] for x in list(faculty_dict)[:3]}))
print("Q7. " + str({y: professor_dict[y] for y in list(professor_dict)[:3]}))

#Q8
print("Q8. " + str({z: professor_dict[z] for z in sorted(list(professor_dict), key=lambda x: x[1])[:3]}))
