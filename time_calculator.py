def add_time(start, duration, day = None):
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

  start = start.split(' ')
  modifier = start[1]

  start = start[0].split(':')
  hour = int(start[0])
  minute = int(start[1])

  if modifier == 'PM':
    hour += 12

  duration = duration.split(':')
  durHour = int(duration[0])
  durMinute = int(duration[1])

  hour += durHour
  minute += durMinute
  n = 0

  if minute > 60:
    minute -= 60
    hour += 1

  if minute < 10:
    minute = '0' + str(minute)

  if hour > 24:
    n = hour // 24
    hour = hour % 24  

  if hour >= 12:
    newModifier = 'PM'
    hour -= 12
  else:
    newModifier = 'AM'

  if hour == 0:
    hour = 12

  result = str(hour) + ':' + str(minute) + ' ' + newModifier

  if day:
    day = day.capitalize()
    if day not in days:
      return 'Error: Day input not valid.'
    i = days.index(day)
    newDay = days[(i+n)%7]
    result += ', ' + newDay

  if n == 1:
    result += ' (next day)'
  elif n > 1:
    result += ' (' + str(n) + ' days later)'
  
  return result