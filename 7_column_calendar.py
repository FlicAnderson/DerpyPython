# take as commandline inputs the number of days in a month, the weekday of the 1st of that month, and print out on the screen a 7 column calendar for that month

# month has x days. Enter the number of days from the calendar and what weekday the first of the month is & then output Monday Tuesday

# first input (aside from filename) is a number
# second input (aside from filename) is a string (a weekday) which represents the first of that "month"

import sys

month_length = sys.argv[1]
weekday_of_1st = sys.argv[2]

print "Here's your 'HUMAN' calendar of", str(month_length), "days, starting on", weekday_of_1st, "!"

# dictionary
week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

# print days of week
print week_days

# print range of numbers
print range(1,int(month_length)+1)

# print month_length

#human_week = week_days[week_days.index(weekday_of_1st)]
#print human_week

# number of full weeks
num_whole_weeks = int(month_length) / 7
# number of remainder days at end of week
num_remainder_days = int(month_length) % 7

# questions to answer:
# how many blank days at start of month
# how many weeks (use the divide thing
# how many blank days at the end of the month (modulo thing?)




