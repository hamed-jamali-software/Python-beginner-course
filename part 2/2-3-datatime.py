from datetime import date, timedelta
from datetime import time
from datetime import datetime

today = date.today()
print("Today's date is ", today)

# print out the date's individual components
print("Date Components: ", today.day, today.month, today.year)

# retrieve today's weekday (0=Monday, 6=Sunday)
print("Today's Weekday #: ", today.weekday())
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
print("Which is a " + days[today.weekday()])

## DATETIME OBJECTS
# Get today's date from the datetime class
today = datetime.now()
print("The current date and time is ", today)

# Get the current time
t = datetime.time(datetime.now())
print("The current time is ", t)

now = today

# print today's date one year from now
print ("one year from now it will be: " + str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
print ("in two weeks and 3 days it will be: " + str(now + timedelta(weeks=2, days=3)))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print ("one week ago it was " + s)

### How many days until April Fools' Day?

today = date.today()  # get today's date
afd = date(today.year, 4, 1)  # get April Fool's for the same year
# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print ("April Fool's day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year=today.year + 1)  # if so, get the date for next year

# Now calculate the amount of time until April Fool's Day
time_to_afd = afd - today
print ("It's just", time_to_afd.days, "days until next April Fools' Day!")