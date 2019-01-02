import datetime


def getlastday(year, month):
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return 29
        else:
            return 28

    monthdict = {
        1: 31,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    return monthdict.get(month)

datesum = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if datetime.datetime(year, month, 1).weekday() == 6:
            datesum += 1

print(datesum)
