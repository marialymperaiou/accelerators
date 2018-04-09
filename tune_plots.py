import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt		

#Plot tune oscillation over the number pof turns. This will be done for all tested chromaticities
def tune_plots(turn, start, stop, step, naff_list, mean, color, plot_all):
	plt.rc('text', usetex=True)
	plt.rc('font', family='serif')

	plt.plot(turn[start:stop:step], naff_list, color = color, label = r'$Tunes$')			#naff_list contains the tune oscillation
	plt.suptitle(r'Tune vs Number of turns', fontsize=16)

	ax = plt.gca()
	if not plot_all:
		plt.axhline(y=mean, color='crimson', linestyle='-', label = r'$Mean$ $tune$')
	plt.xlabel(r'$N$')
	plt.ylabel(r'$Q$')
	ax.ticklabel_format(useOffset=False)
	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

	# Put a legend to the right of the current axis
	ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
	#ax.legend(loc=4)
	plt.subplots_adjust(left=0.15, right = 0.8)


	'''
	plt.plot(turn[start:stop], amp[:200])
	plt.xlabel('N')
	plt.ylabel('Amplitude')
	ax = plt.gca()
	ax.ticklabel_format(useOffset=False)
		'''