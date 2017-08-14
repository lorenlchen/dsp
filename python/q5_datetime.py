from datetime import datetime

def find_days_diff(start_date, end_date):
    return (end_date - start_date).days

####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'
start = datetime.strptime(date_start, '%m-%d-%Y')
end = datetime.strptime(date_stop, '%m-%d-%Y')

print('a. ' + str(find_days_diff(start, end)))


####b)
date_start = '12312013'
date_stop = '05282015'
start = datetime.strptime(date_start, '%m%d%Y')
end = datetime.strptime(date_stop, '%m%d%Y')

print('b. ' + str(find_days_diff(start, end)))

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
start = datetime.strptime(date_start, '%d-%b-%Y')
end = datetime.strptime(date_stop, '%d-%b-%Y')

print('c. ' + str(find_days_diff(start, end)))