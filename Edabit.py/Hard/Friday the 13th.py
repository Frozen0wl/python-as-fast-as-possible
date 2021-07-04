import datetime

def has_friday_13(month, year):
    x = datetime.datetime(year, month, 13)

    day = x.strftime("%A")

    if day == "Friday":
        return True
    
    return False

print(has_friday_13(3, 2020))