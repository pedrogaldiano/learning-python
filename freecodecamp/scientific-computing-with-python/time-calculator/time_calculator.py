def add_time(start, duration, day_week=''):

# Convert the inputs in lists of strings/int
    start = str(start.replace(':', ' ')).split()
    duration = duration.split(':')

# Set up the essential variable 
# (I have to define it because it will be nedded in all scenarios)
    sum_hour = add = new_days = 0
    new_symbol = start[2]
    day_week = day_week.lower()
    new_day_week = ''

# Sum the minutes from the start and duration
    new_minutes = int(start[1]) + int(duration[1])
    if new_symbol == 'PM': add = 12
    
# Convert minutes in hours if needed    
    if new_minutes > 59:
        sum_hour = new_minutes // 60
        new_minutes = new_minutes % 60
    
# Sum the hours
    new_hours = sum_hour + int(start[0]) + int(duration[0]) + add
    
# How many days has passed?
    if new_hours > 24:
        new_days = new_hours // 24
        new_hours = new_hours % 24
    
# It's PM or AM? Until now the new_hours was in 24 hours, now it's in 12 hours
    if new_hours >= 12:
        new_hours = new_hours - 12
        new_symbol = 'PM'
        if new_hours == 0: new_hours = 12
    elif new_hours < 12: 
        new_symbol = 'AM'
        if new_hours == 0: new_hours = 12

# What day of the week it's going to be?
    days_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']   
    if day_week in days_week:
        index = days_week.index(day_week)
        print(index)
        new_day_week = ', ' + days_week[(index + new_days) % 7].capitalize()

# It's the same day, the 'next day' or 'x days later'?
    if new_days == 0: new_days = ''
    elif new_days == 1: new_days = ' (next day)'
    elif new_days > 1: new_days = f' ({new_days} days later)'
    
    return (f'{new_hours}:{"{:02d}".format(new_minutes)} {new_symbol}{new_day_week}{new_days}')