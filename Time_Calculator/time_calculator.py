def add_time(start, duration, day = None):
  #PREPARATION
  start = start.replace(":", " ").split()
  duration = duration.replace(":", " ").split()
  end_h = int(start[0]) + int(duration[0])
  end_m = int(start[1]) + int(duration[1])
  #CALCULATION
  while end_m >= 60:
    end_h += 1
    end_m = end_m - 60
  n = 0
  while end_h > 24:
    n += 1
    end_h = end_h - 24
  am_or_pm = start[2]
  while end_h >= 12:    
    if am_or_pm == "PM":
      am_or_pm = am_or_pm.replace("P", "A")
      n += 1
    elif am_or_pm == "AM":
      am_or_pm = am_or_pm.replace("A", "P")
    end_h = end_h - 12
  if end_h == 0:
    end_h = 12
  end_h = str(end_h)
  end_m = str(end_m)
  if len(end_m) == 1:
    end_m = "0" + end_m
  #FINISHING
  new_time = f"{end_h}:{end_m} {am_or_pm}"
  if day != None:
    day = day.lower()
    if day == "monday": day_int = 1
    elif day == "tuesday": day_int = 2
    elif day == "wednesday": day_int = 3
    elif day == "thursday": day_int = 4
    elif day == "friday": day_int = 5
    elif day == "saturday": day_int = 6
    elif day == "sunday": day_int = 0
    day_int = day_int + n
    while day_int > 6:
      day_int = day_int - 7
    if day_int == 1: new_day = "Monday"
    elif day_int == 2: new_day = "Tuesday"
    elif day_int == 3: new_day = "Wednesday"
    elif day_int == 4: new_day = "Thursday"
    elif day_int == 5: new_day = "Friday"
    elif day_int == 6: new_day = "Saturday"
    elif day_int == 0: new_day = "Sunday"
    new_time += f", {new_day}"
  if n == 1:
    new_time += " (next day)"
  elif n > 1:
    new_time += f" ({n} days later)"
  return new_time