def add_time(start, duration, day = None):
  hours = int(start[:start.index(":")])
  minutes = int(start[start.index(":")+1: 5])
  hours_to_add = int(duration[:duration.index(":")])
  minutes_to_add = int(duration[duration.index(":")+1:])
  am_or_pm = start[-2:]
  days_difference = 0
  minutes = minutes + minutes_to_add 
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
  future_day = ""
  if day is not None:
    day = day.lower().capitalize()
    index = days.index(day)
  hours += hours_to_add % 12
  if minutes >= 60:
    minutes = minutes - 60
    hours+=1
  if minutes<10:
    minutes = "0"+str(minutes)
  if hours > 12:
    hours -= 12
    am_or_pm = "PM" if am_or_pm == "AM" else "AM"
  if hours == 12:
    am_or_pm = "PM" if am_or_pm == "AM" else "AM"
  if start[-2:] != am_or_pm and start[-2:]!="AM":
    days_difference = hours_to_add//24+1
  else:
    days_difference = hours_to_add//24
  if day:
    try:
      future_day = days[index+ days_difference % len(days)]
    except IndexError:
      future_day = days[index+days_difference%len(days)-len(days)]
  return string_builder(hours,minutes,am_or_pm,days_difference,future_day,day)
  
      
def string_builder(hours,minutes,am_or_pm,days_difference, future_day, day):
  if day:
    if days_difference>1:
      return f"{hours}:{minutes} {am_or_pm}, {future_day} ({days_difference} days later)"
    if days_difference == 1:
      return f"{hours}:{minutes} {am_or_pm}, {future_day} (next day)"
  if days_difference > 1:
      return f"{hours}:{minutes} {am_or_pm} ({days_difference} days later)"
  if days_difference == 1:
      return f"{hours}:{minutes} {am_or_pm} (next day)"
  if future_day:
   return f"{hours}:{minutes} {am_or_pm}, {future_day}"
  return f"{hours}:{minutes} {am_or_pm}"