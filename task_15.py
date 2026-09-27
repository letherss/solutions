def days_in_month(month, year):
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return 29
        else:
            return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31

print(days_in_month(1, 2001))
print(days_in_month(2, 2001))
print(days_in_month(2, 2000))
print(days_in_month(2, 1900))
print(days_in_month(11, 2025))