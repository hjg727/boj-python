weekday, days = map(int, input().split())
blank, delimiters = map(str, input().split())

def weekday_translate(weekday):
    if weekday == 0:
        weekday = 6
    elif weekday == 1:
        weekday = 0
    elif weekday == 2:
        weekday = 1
    elif weekday == 3:
        weekday = 2
    elif weekday == 4:
        weekday = 3
    elif weekday == 5:
        weekday = 4
    elif weekday == 6:
        weekday = 5
    return weekday

def make_calendar(weekday, days, blank, delimiters):

    calendar = [[blank] * 7 for _ in range(6)]

    day = 1
    row, col = 0, weekday_translate(weekday)

    while day <= days:
        calendar[row][col] = str(day)
        col += 1
        day += 1
        
        if col > 6:
            col = 0
            row += 1

        if row >= 6:
            break
        
    for row in calendar:
        print(delimiters.join(row))
    
make_calendar(weekday, days, blank, delimiters)