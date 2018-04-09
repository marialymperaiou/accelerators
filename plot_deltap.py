import numpy as np
import matplotlib.pyplot as plt
from deltap import deltap

#plot deltap oscillation over the number of turns with all the values of chromaticity
def plot_deltap(pt, turn, chromaticities):
	dp_list=[]

	#for every chromaticity different color from this list
	colors = ['b','r','g','m', 'y','c', 'r','g','m','b','r','c']
	plt.figure(figsize = (8,8))

	for i in xrange (len(chromaticities)):
		dp = deltap(pt, turn, chromaticities[i], colors[i])
		dp_list.append(dp)
	plt.show()
	return dp_list