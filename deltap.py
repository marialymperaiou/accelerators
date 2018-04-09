import numpy as np
import matplotlib.pyplot as plt
from naff_transformation import naff_transformation

#Calculate deltap over the number of turns with respect to different chromaticities

def deltap(pt, turn, trns, color):
	plt.rc('text', usetex=True)
	plt.rc('font', family='serif')
	d_list = []
	
	amp, c, d_list = naff_transformation(len(turn), np.array (pt), d_list)
	print 'Deltap frequency', d_list[0]
	print 'Mean', np.mean(pt)
	print 'Maximum', max(pt)
	print 'Minimum', min(pt)

	plt.plot(pt, color, label = r'$Chromaticity$ %d' %(trns))
	plt.title(r'$\Delta$p $vs$ $Number$ $of$ $turns$')
	ax = plt.gca()
	plt.xlabel(r'$N$')
	plt.ylabel(r'$\Delta$p')
	ax.ticklabel_format(useOffset=False)
	# Put a legend to the right of the current axis
	ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
	
	plt.subplots_adjust(left=0.15, right = 0.8)
	
	return d_list[0]