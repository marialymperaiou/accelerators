#for different number of turns plot the values of fft and naff to make a comparison: output of the transformation (frequency) vs number of turns.
#to run this script you should have first produced all the tracking files from 'master_lattice.py' (and the produced MADX scripts) for the values of the matrix 'scripts' as values of the variable 'TURNS'.
import numpy as np
import matplotlib.pyplot as plt
import metaclass as mtc
from fourier import fourier
from naff_transformation import naff_transformation
from plot_compare import *
from window import window
from latex_output import *
from plot_tune_change import *
from plot_deltap import plot_deltap

N_part = 1
chromaticities = [0,1,5,10,15,20,25,30,35,40]
'''
chromaticities = []
f = open('chromaticities.txt','r')
for line in f:
    chrom=line.split()
    chromaticities.append(float(chrom[0]))
'''

#x
fft_x_list=[]				#promiment frequencies from FFT
naff_x_list = []			#promiment frequencies from NAFF
mean_x_list=[]				#mean tune for each chromaticity
freq_x_list=[]				#tune oscillation frequency for each chromaticity

#y
fft_y_list=[]
naff_y_list = []
mean_y_list=[]
freq_y_list=[]

for i in xrange (len(chromaticities)):
	fname_twiss = 'track_master%d.out.obs0001.p0001'%(chromaticities[i])
	ob = mtc.twiss(fname_twiss)
	
	#FFT
	maximum_X, fourier_X, freq_X = fourier(ob.X, timestep = 1) 
	fft_x_list.append(abs(maximum_X))

	maximum_Y, fourier_Y, freq_Y = fourier(ob.Y, timestep = 1) 
	fft_y_list.append(abs(maximum_Y))

	#NAFF
	start_x = 0								#beginning of the 'bucket'
	stop_x = 800							#end of the bucket
	step_x = 1                            	#step inside the bucket
	width_x = 200                          	#window width

	start_y = 0							
	stop_y = 800							
	step_y = 1                        
	width_y = 200                       

	#if oute of range, then call NAFF without windowing, and return the prominent frequencies
	if stop_x>(len(ob.TURN)-width_x):
		amplitude_X, counter_X, naff_x_list = naff_transformation(len(ob.TURN), np.array (ob.X), naff_x_list)
	else:
		fig=plt.figure(figsize = (7,5))
		mean_X, frequency_X = window(start_x, stop_x, step_x, width_x, ob.X, ob.TURN)
		plt.title(r'$x - plane$, $Chromaticity = %d$'%chromaticities[i])
		plt.show()
		mean_x_list.append(mean_X)
		freq_x_list.append(frequency_X)

	if stop_y>(len(ob.TURN)-width_y):
		amplitude_Y, counter_Y, naff_y_list = naff_transformation(len(ob.TURN), np.array (ob.Y), naff_y_list)
	else:
		fig=plt.figure(figsize = (7,5))
		mean_Y, frequency_Y = window(start_y, stop_y, step_y, width_y, ob.Y, ob.TURN)
		plt.title(r'$y - plane$, $Chromaticity = %d$'%chromaticities[i])
		plt.show()
		mean_y_list.append(mean_Y)
		freq_y_list.append(frequency_Y)
	

dp_list = plot_deltap(ob.PT, ob.TURN, chromaticities)

#make LaTeX tables
tex_tunes_x(mean_x_list, freq_x_list, chromaticities)
tex_tunes_y(mean_y_list, freq_y_list, chromaticities)
tex_deltap(dp_list,chromaticities)

#mean tune changes qith chromaticity change. Tune oscillation frequency also changes. This function plots those changes.
plot_tune_change(mean_x_list, mean_y_list, freq_x_list, freq_y_list, chromaticities)
#plots deltap change with chromaticity
plot_deltap_change(dp_list, chromaticities)











