#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
Author: "Walid Hasan Ansary"
Semester: "Summer 2026"

The python code in this file (assignment1.py) is original work written by
"Walid Hasan Ansary". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    lyear = year % 4
    if lyear == 0:
        is_leap = True
    else:
        is_leap = False

    lyear = year % 100
    if lyear == 0:
        is_leap = False

    lyear = year % 400
    if lyear == 0:
        is_leap = True

    return is_leap

def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    if leap_year(year):
        feb_max = 29
    else:
        feb_max = 28
        
    mon_dict = {1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return mon_dict[month]

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    tmp_day = day + 1

    max_days = mon_max(month, year)

    if tmp_day > max_days:
        to_day = tmp_day % max_days 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date

def usage():
    "Print a usage message to the user and exit"
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    parts = date.split('-')
    if len(parts) != 3:
        return False
        
    str_year, str_month, str_day = parts
    
    if len(str_year) != 4 or len(str_month) != 2 or len(str_day) != 2:
        return False
        
    try:
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
    except ValueError:
        return False
        
    if month < 1 or month > 12:
        return False
        
    if day < 1 or day > mon_max(month, year):
        return False
        
    return True

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    weekend_count = 0
    current_date = start_date
    
    while True:
        str_year, str_month, str_day = current_date.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        
        dow = day_of_week(year, month, day)
        if dow == 'sat' or dow == 'sun':
            weekend_count += 1
            
        if current_date == stop_date:
            break
            
        current_date = after(current_date)
        
    return weekend_count

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    
    if not valid_date(arg1) or not valid_date(arg2):
        usage()
        
    if arg1 > arg2:
        start_date = arg2
        end_date = arg1
    else:
        start_date = arg1
        end_date = arg2
        
    weekends = day_count(start_date, end_date)
    
    print(f"The period between {start_date} and {end_date} includes {weekends} weekend days.")
