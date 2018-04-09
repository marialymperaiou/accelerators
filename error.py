#compute the difference between 2 values and their rate of change
import numpy as np

def error (v1, v2):
	e = abs(v1-v2)
	try:
		percentage = (e/v1)*100
	except ZeroDivisionError:
		print "Division by 0!!!"
		return 
	return e, percentage
	