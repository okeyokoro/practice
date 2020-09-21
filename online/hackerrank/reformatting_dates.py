import datetime

def reformatDate(dates):
    new_dates = []
    for date in dates:
        t = datetime.datetime.strptime(date, f"%d{ len(date) == 12 and date[1:3] or date[2:4] } %b %Y")
        new_dates.append(t.strftime("%Y-%m-%d"))
    return new_dates

###############################################
### From this point down is the test suite  ###
###############################################
