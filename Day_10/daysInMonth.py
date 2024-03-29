def is_leap(year):
    """Gibt 'True' zurück, wenn das aktuelle Jahr ein Schaltjahr ist. Ansonsten 'False'"""
    isLeap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                isLeap = True
            else:
                isLeap = False
        else:
            isLeap = True
    else:
        isLeap = False
    return isLeap
#

def days_in_month(year, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

    isLeap = is_leap(year)
    if isLeap == True and month == 2:
        return 29

    daysOfMonth = month_days[month-1]
    return daysOfMonth

#
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)