##Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.
##
##The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination
##of years, days, hours, minutes and seconds.
##
##It is much easier to understand with an example:
##
##* For seconds = 62, your function should return 
##    "1 minute and 2 seconds"
##* For seconds = 3662, your function should return
##    "1 hour, 1 minute and 2 seconds"
##For the purpose of this Kata, a year is 365 days and a day is 24 hours.
##
##Note that spaces are important.
##
##Detailed rules
##The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units
##of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.
##
##The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be
##written in English.
##
##A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year
##and 1 second is.
##
##Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.
##
##A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.
##
##A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead.
##Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

def format_duration(seconds):
    if seconds == 0:
        return "now"
    if seconds < 60:
        if seconds > 1:
            return "{0} seconds".format(seconds)
        else:
            return "{0} second".format(seconds)
    years = get_years(seconds)
    seconds = seconds - 3600*24*365*years
    days = get_days(seconds)
    seconds = seconds - 3600*24*days
    hours = get_hours(seconds)
    seconds = seconds - 3600*hours
    minutes = get_minutes(seconds)
    seconds = seconds - 60*minutes
    dic = {"years":years,
           "days":days,
           "hours":hours,
           "minutes":minutes,
           "seconds":seconds}
    lst_val = [v for v in list(dic.values()) if v>0]
    lst_key = [k if dic[k]>1 else k[:-1] for k in list(dic.keys()) if dic[k]>0]
    string = ""
    for key, val in zip(lst_key, lst_val):
        if lst_key.index(key) == len(lst_key)-1:
            if len(lst_key) > 1:
                string += "and {0} {1}".format(val, key)
            else:
                string += "{0} {1}".format(val, key)
        elif lst_key.index(key) == len(lst_key)-2:
            string += "{0} {1} ".format(val, key)
        else:
            string += "{0} {1}, ".format(val, key)
    return string
def get_years(seconds):
    years = 0
    while True:
        seconds = seconds - 3600*24*365
        if seconds >= 0:
            years += 1
        else:
            break
    return years
def get_days(seconds):
    days = 0
    while True:
        seconds = seconds - 3600*24
        if seconds >= 0:
            days += 1
        else:
            break
    return days
def get_hours(seconds):
    hours = 0
    while True:
        seconds = seconds - 3600
        if seconds >= 0:
            hours += 1
        else:
            break
    return hours
def get_minutes(seconds):
    minutes = 0
    while True:
        seconds = seconds - 60
        if seconds >= 0:
            minutes += 1
        else:
            break
    return minutes
