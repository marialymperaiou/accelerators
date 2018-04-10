import numpy as np
import matplotlib.pyplot as plt
import metaclass as mtc
from naff_transformation import naff_transformation
from window import window

#tracking data have been taken for 10 values of chromaticity. Plot the tunes over the tracking number of turns for those chromaticities on the same plot for comparison.
dqx = []								#put chromaticity values in those lists
dqy = []

i=0
f = open('chromaticities.txt','r')

#every tune curve will have a different color from the list below:
colors = ['b','r','g','m', 'y','c', 'r','g','m','b','r','c']

#for sliding window:
start = 0							#beginning of the 'bucket'
stop = 800							#end of the bucket
step = 1                            #step inside the bucket
width = 200							#window width

plt.figure(figsize=(8,8))
for line in f:
	chrom=line.split()
	dqx.append(float(chrom[0]))
	dqy.append(float(chrom[1]))
	fname_twiss = 'track_master%d.out.obs0001.p0001'%(dqx[i])

	#print colors[i]
	ob = mtc.twiss(fname_twiss)

	mean, freq = window(start, stop, step, width, ob.X, ob.TURN, colors[i], plot_all = True, chroma = dqx[i-1])
	i+=1
plt.show()

plt.figure(figsize=(8,8))
i=0
for line in f:
	fname_twiss = 'track_master%d.out.obs0001.p0001'%(dqy[i])
	ob = mtc.twiss(fname_twiss)

	mean, freq = window(start, stop, step, width, ob.Y, ob.TURN, colors[i], plot_all = True, chroma = dqy[i-1])
	i+=1
plt.show()