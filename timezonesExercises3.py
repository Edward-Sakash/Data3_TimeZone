"""# Task 1
from datetime import datetime
from dateutil import tz

# Set up birthdate with timezone
birthdate = datetime(1972, 7, 11, 10, 0, tzinfo=tz.gettz('Europe/Berlin'))

# Convert to New Zealand time
nz_tz = tz.gettz('Pacific/Auckland')
birthdate_in_newzealand = birthdate.astimezone(nz_tz)

# Print out the times for the meeting with the Moscow team
moscow_tz = tz.gettz('Europe/Moscow')
moscow_time = datetime(2023, 4, 27, 13, 35, tzinfo=moscow_tz)

ireland_tz = tz.gettz('Europe/Dublin')
ireland_time = moscow_time.astimezone(ireland_tz)
print("Meeting time in Ireland:", ireland_time.strftime("%Y-%m-%d %H:%M:%S"))

san_francisco_tz = tz.gettz('America/Los_Angeles')
san_francisco_time = moscow_time.astimezone(san_francisco_tz)
print("Meeting time in San Francisco:", san_francisco_time.strftime("%Y-%m-%d %H:%M:%S"))

berlin_tz = tz.gettz('Europe/Berlin')
berlin_time = moscow_time.astimezone(berlin_tz)
print("Meeting time in Berlin:", berlin_time.strftime("%Y-%m-%d %H:%M:%S"))

johannesburg_tz = tz.gettz('Africa/Johannesburg')
johannesburg_time = moscow_time.astimezone(johannesburg_tz)
print("Meeting time in Johannesburg:", johannesburg_time.strftime("%Y-%m-%d %H:%M:%S"))

# Print out the birthdate in New Zealand time
print("Birthdate in New Zealand:", birthdate_in_newzealand.strftime("%Y-%m-%d %H:%M:%S"))"""


"""# Task 2
import pytz
from datetime import datetime

# define the meeting date and time in Moscow timezone
moscow_tz = pytz.timezone('Europe/Moscow')
meeting_date = datetime(2021, 8, 7, 13, 35, tzinfo=moscow_tz)

# convert to each region's corresponding timezone
dublin_tz = pytz.timezone('Europe/Dublin')
dublin_date = meeting_date.astimezone(dublin_tz)

san_francisco_tz = pytz.timezone('America/Los_Angeles')
san_francisco_date = meeting_date.astimezone(san_francisco_tz)

berlin_tz = pytz.timezone('Europe/Berlin')
berlin_date = meeting_date.astimezone(berlin_tz)

johannesburg_tz = pytz.timezone('Africa/Johannesburg')
johannesburg_date = meeting_date.astimezone(johannesburg_tz)

# print out the meeting time for each region
print("Irish participants will meet at:", dublin_date.strftime('%Y-%m-%d %H:%M:%S%z'))
print("German participants will meet at:", berlin_date.strftime('%Y-%m-%d %H:%M:%S%z'))
print("South African participants will meet at:", johannesburg_date.strftime('%Y-%m-%d %H:%M:%S%z'))
print("American participants will meet at:", san_francisco_date.strftime('%Y-%m-%d %H:%M:%S%z'))"""

"""# Task 3

import datetime

# convert UNIX timestamp to datetime object
timestamp = 1626430738
date = datetime.datetime.fromtimestamp(timestamp)

# format datetime object as readable date string
date_string = date.strftime('%m/%d/%Y, %H:%M:%S')

# print the readable date string
print(date_string)"""
