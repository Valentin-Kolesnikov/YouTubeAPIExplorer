from datetime import datetime

def age_calendar(dateBefore=False, dateAfter=False):
    plus_year = False
    now = datetime.now()
    year = input("\nEnter the year: ")

    if year.isdigit() and 2006 <= int(year) <= now.year:
        if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
            plus_year = True
    elif year.isdigit() and 6 <= int(year) <= (now.year - 2000):
        year = str(20) + str(year.zfill(2))
        if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
            plus_year = True
    elif dateAfter:
        year = 2005
    elif dateBefore:
        year = now.year

    month = input("\nEnter the month numerously: ")

    if month.isdigit() and int(month) < 13 and int(month) != 0:
        if int(year) == now.year and int(month) > now.month:
            month = str(now.month).zfill(2)
        month = str(month).zfill(2)
    elif dateAfter:
        month = str(1).zfill(2)
    elif dateBefore:
        month = str(now.month).zfill(2)

    day = input("\nEnter the day numerously: ")

    if day.isdigit() and int(day) != 0 and int(day) < 32:
        if int(year) == now.year and int(month) == now.month and int(day) > now.day:
            day = str(now.day).zfill(2)

        elif month in ['01', '03', '05', '07', '08', '10', '12']:
            day = str(day).zfill(2)

        elif int(day) < 31 and month in ['04', '06', '09', '11']:
            day = str(day).zfill(2)

        elif plus_year == True and month == "02" and int(day) < 30:
            day = str(day).zfill(2)
        
        elif plus_year == False and month == "02" and int(day) < 29:
            day = str(day).zfill(2)
        
        else:
            day = str(1).zfill(2)
    
    elif dateAfter:
        day = str(1).zfill(2)
    elif dateBefore:
        day = str(now.day).zfill(2)
        
    return year, month, day