import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt	
from pylab import *
from naff_transformation import naff_transformation
from fourier import fourier
from print_info import print_info
from tune_plots import tune_plots


#start is the initial point of the interval in which the transformation is going to be implemented
#stop is the final point of this interval
#width defines the window size
#step defines how much the window is moving
rc('text', usetex=True)

def window(start, stop, step, width, signal, turn, color='m', plot_all = False, chroma = 1, padd = False):
	#if not plot_all:
		#plt.figure(figsize=(10,10))
	amp = []
	frequency = []
	while True:
		
		naff_list = []
		#windowing
		for min_turn in range(start,stop,step):													
			max_turn = min_turn+width

			#print "Turns: ",min_turn,max_turn
			amplitude, counter, naff_list = naff_transformation(width, signal[min_turn:max_turn], naff_list)
			#print 'naff', naff_list
			amp.append(amplitude[counter-1])
		#print amp
		
		mean = print_info(naff_list)

		#use again NAFF to find tune oscillation frequency
		a,c, frequency = naff_transformation(len(naff_list), np.array(naff_list), frequency)
		for cnt in xrange (len(frequency)):
			print 'Tune frequency', frequency[cnt]			#in this case, the prominent frequency is only one, so this array has only one element!

		#plot the tunes over the number of turns to see tune oscillation
		tune_plots(turn, start, stop, step, naff_list, mean, color, plot_all)

		if max_turn>=len(turn)-width:
			break

	return mean, frequency[0]
