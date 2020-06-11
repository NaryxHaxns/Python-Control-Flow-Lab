# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

raw_month = input('Enter the month of the year: ')
month = raw_month[0:3]
day = input('Enter the day of the month: ')

if month in ('Jan', 'Feb'):
    season = 'Winter'
    print(f'{month} {day} is in {season}')
elif month in ('Apr', 'May'):
    season = 'Spring'
    print(f'{month} {day} is in {season}')
elif month in ('Jul', 'Aug'):
    season = 'Summer'
    print(f'{month} {day} is in {season}')
elif month in ('Oct', 'Nov'):
    season = 'Fall'
    print(f'{month} {day} is in {season}')
elif month == 'Dec' and int(day) >= 21 or month == 'Mar' and int(day) <= 19:
    season = 'Winter'
    print(f'{month} {day} is in {season}')
elif month == 'Mar' and int(day) >= 20 or month == 'Jun' and int(day) <= 20:
    season = 'Spring'
    print(f'{month} {day} is in {season}')
elif month == 'Jun' and int(day) >= 21 or month == 'Sep' and int(day) <= 21:
    season = 'Summer'
    print(f'{month} {day} is in {season}')
elif month == 'Sep' and int(day) >= 22 or month == 'Dec' and int(day) <= 20:
    season = 'Fall'
    print(f'{month} {day} is in {season}')
