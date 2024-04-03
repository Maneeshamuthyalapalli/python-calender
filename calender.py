import calendar

def generate_calendar(year):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    for month in range(1, 13):
        month_calendar = cal.formatmonth(year, month)
        print(month_calendar)

year = int(input("Enter the year: "))
generate_calendar(year)
