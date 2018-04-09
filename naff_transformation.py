#Implements NAFF transformation over a given signal
import numpy as np
from NAFF import *
from modules.exp_fit import *

def naff_transformation(N_turns,signal, naff_list=[], turn_list = [], flag=0, remove_coupling = False, flag_frequency_interval = False, min_freq = 0, max_freq = 1,second_half =False):
	#flag defines if a list of frequencies is necessary to be returned. The default value doesn't return the list.
	t = np.arange(0.0,signal.size,1)	

	data = []
	#data2 = []
	for i in range (len(t)):
	 	data.append(signal[i])

	#t,data2 = exp_fit(t,data)
	#print data2

	coord = Vec_cpp()
	zero  = Vec_cpp()
	coord.extend(i for i in data)
	zero.extend((0)*i for i in data)
	naff = NAFF()

	naff.fmax=1
	naff.set_window_parameter(1, 'h')
	#naff.set_interpolation(True)
  	#naff.set_upsampling(True,'spline')
  	#naff.set_merit_function("minimize_RMS_frequency")
	if (flag_frequency_interval==True):
		naff.set_frequency_interval(min_freq,max_freq)
	tune_all=naff.get_f(coord,zero)
	
	counter = 0
	for i in tune_all:
		if (second_half == True):
			tune_all = 1-tune_all
	 	counter += 1
	 	#print "Frequency [",counter,"]= ",i
	 	naff_list.append(i)						#includes all the tunes. i is the tune of every call
	 	turn_list.append(N_turns)
	 	#print naff_x_list
	amplitudes = naff.return_amplitudes()
	#print amplitudes[counter-1]
	if not flag:
		return amplitudes, counter, naff_list
	elif flag:
		return amplitudes, counter, naff_list,turn_list
