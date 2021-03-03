import datetime

class calendar:

	def __init__(self, num_days):
		self.days = [{}] * num_days

	def checkFree(self, appointment):
		time = appointment.time()
		day = appointment.date().day
		if time not in self.days[day].keys():
			return True
		return False

	def addAppointment(self, appointment):
		if self.checkFree(appointment):
			self.days[appointment.date().day][appointment.time()] = appointment.description
			print("Your appointment has been added")
		else:
			print("Sorry that time is not availible")


class appointment:

	def __init__(self, datetime, description):
		self.date = datetime.date
		self.time = datetime.time
		self.description = description


month = 0
monthDict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
print("Hi, What month would you like to set your appointments in? (1-12)?")
while(True):
	try:
		month = int(input())
		if month > 0 and month < 13:
			break
		raise(ValueError)
	except ValueError:
		print("Sorry, try again with a month value between 1 - 12")

maxDays = monthDict[month]
ApptCalendar = calendar(maxDays)
print("Great! What date would you like your appointment to be? (1-" + str(maxDays) + ")")
day = 0
while(True):
	try:
		day = int(input())
		if day > 0 and day <= maxDays:
			break
		raise(ValueError)
	except ValueError:
		print("Sorry, try again with a day value between 1 - " + str(maxDays))

print("Got it. What time is your appointment? (HH:MM AM/PM)")




#appt = appointment(datetime.datetime(2021,3,2,10), "Interview with Palantir")
#marchApptCalendar.addAppointment(appt)
