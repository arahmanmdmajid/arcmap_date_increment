from datetime import date
day=0
todayDateStr = '' 
def autoIncrement(): 
 global day
 global todayDateStr
 pStart = 1
 pInterval = 1
 time_unit = 'days'
 todayDate = date.today()
 if (day == 0):
  todayDateStr = todayDate.strftime('%m/%d/%Y')
  day = pStart
 else:
  day+= pInterval
  todayDate += datetime.timedelta(**{time_unit: day})
  todayDateStr = todayDate.strftime('%m/%d/%Y')
 return todayDateStr
