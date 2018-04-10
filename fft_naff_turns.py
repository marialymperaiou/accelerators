#for different chromaticities plot the values of fft and naff to make a comparison: output of the transformation (frequency) vs chromaticity.
#to run this script you should have first produced all the tracking files from 'master_lattice.py' (and the produced MADX scripts) for the values of the matrix 'chromaticity'.
import numpy as np
import matplotlib.pyplot as plt
import metaclass as mtc
from fourier import fourier
from naff_transformation import naff_transformation
from plot_compare import *

#you must have produced the combinations with different chromaticities and different number of turns

N_part = 1 												#track one particle. initial MADX script tracks 10 particles.

t = []													#store here the number of tracking turns that you are going to use
f = open('turns.txt','r')
for line in f:
	turn = line.split()
	t.append(float(turn[0]))
#print t

chromaticity = [0]
'''
f = open('chromaticities.txt','r')
for line in f:
    ch=line.split()
    chromaticity.append(float(ch[0]))
#print chromaticity
'''

for i in xrange (len(chromaticity)):
	fft_x_list= []
	naff_x_list = []
	fft_y_list= []
	naff_y_list = []
	for j in xrange (len(t)):
		fname_twiss = 'track%d_master%d.out.obs0001.p0001'%(t[j],chromaticity[i])
		ob = mtc.twiss(fname_twiss)

		#FFT
		maximum_X, fourier_X, freq_X = fourier(ob.X, timestep = 1) 
		fft_x_list.append(abs(maximum_X))

		maximum_Y, fourier_Y, freq_Y = fourier(ob.Y, timestep = 1) 
		fft_y_list.append(abs(maximum_Y))

		#NAFF
		amplitude_X, counter_X, naff_x_list = naff_transformation(len(ob.TURN), np.array (ob.X), naff_x_list)
		amplitude_Y, counter_Y, naff_y_list = naff_transformation(len(ob.TURN), np.array (ob.Y), naff_y_list)

	#use the following plot function when window=signal length
	#if l_turns = len(ob.TURN)
	#you are going to compare the performance of the 2 algorithms
	plot_compare_turns(t, fft_x_list, fft_y_list, naff_x_list, naff_y_list, chromaticity[i])


