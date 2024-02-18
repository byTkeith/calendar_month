# programe to print out the calendar
# NYVTEN001
# 11 April 2022
import math

def day_of_week(day, month, year):
    if month == 1 or month == 2:
        year -= 1
        month += 12
    m = (day + math.floor(13*(month+1)/5) + year + math.floor(year/4) - math.floor(year/100) + math.floor(year/400))%7
    return ((m+5)%7)+1


def is_leap(year):
    return year % 400 == 0 and not year % 100 == 0
 
def month_num(month_name):
    month_name = month_name[:1].upper() + month_name[1:].lower()
    if month_name == "January":
        return 1
    elif month_name == "February":
        return 2
    elif month_name == "March":
        return 3
    elif month_name == "April":
        return 4
    elif month_name == "May":
        return 5
    elif month_name == "June":
        return 6
    elif month_name == "July":
        return 7
    elif month_name == "August":
        return 8
    elif month_name == "September":
        return 9
    elif month_name == "October":
        return 10
    elif month_name == "November":
        return 11
    elif month_name == "December":
        return 12
    else:
        return -1

def num_days_in(month_num, year):
    days = ''
    if month_num == 1:
        days = 31
    elif month_num == 2:
        days = 28
        if is_leap(year):
            days = 29
        
            
    elif month_num == 3:
        days = 31
    elif month_num == 4:
        days = 30
    elif month_num == 5:
        days = 31
    elif month_num == 6:
        days = 30
    elif month_num == 7:
        days = 31
    elif month_num == 8:
        days = 31
    elif month_num == 9:
        days = 30
    elif month_num == 10:
        days = 31
    elif month_num == 11:
        days = 30
    elif month_num == 12:
        days = 31
    return days

def num_weeks(month_num, year):
    return math.ceil((num_days_in(month_num, year)+day_of_week(1, month_num, year)-1)/7)

def week(week_num, start_day, days_in_month):
    st = (week_num-1)*7 + 2 - start_day
    results = ''
    if st < 1:
        results = results + '  '
    else:
        results = results + '{:2d}'.format(st)
    for day in range(st+1, st+7):
        results = results + ' '
        if day < 1 or day > days_in_month:
            results = results + '  '
        else:
            results = results + '{:2d}'.format(day)
    return results


def main():
    month = input("Enter month:\n")
    year = int(input("Enter year:\n"))
    
    month_number = month_num(month)
    start_day = day_of_week(1, month_number, year)
    days_in_month = num_days_in(month_number, year)
    print(month + ' '.format(year))
    print("Mo Tu We Th Fr Sa Su")
    
    for week_num in range(1, num_weeks(month_number, year)+1):
        print(week(week_num, start_day, days_in_month))
        
if __name__=='__main__':            
    main()





