'''
Phases of the Moon
Task: Write a function that calculate the phase of the moon for a given date.

From Programming Praxis (http://programmingpraxis.com/2010/01/22/phases-of-the-moon/):
* 'The moon circles the earth every 29.530588853 days'
* 'A new moon occurred at julian date 2451550.1 (January 6, 2000).'
* 'There are eight generally recognized phases of the moon: new, waxing crescent, first quarter, waxing gibbous, full, waning gibbous, last quarter, and waning crescent. To calculate the phase of the moon simply divide the days since the last new moon by eight and select the appropriate phase.'
'''

from datetime import date
import math

def current_moon(indate):
	#Define Constants
	LUNAR_MONTH = float(29.530588853)
	EPOCH = date(2000,1,6)
	LUNAR_PHASES = ["New", "Waxing crescent", "First quarter", "Waxing gibbous", "Full", "Waning gibbous", "Last quarter", "Waning crescent"]

	#Calculate days since epoch
	days_since = (indate-EPOCH).days

	#Calculate days since new moon
	last_new = days_since % LUNAR_MONTH

	#Determine phase
	phase = math.floor(8*last_new/LUNAR_MONTH) % 7
	return LUNAR_PHASES[int(phase)]

today = date.today()
print "Today's moon is " + current_moon(today) 
