#compute FFT and NAFF for a standard number of , for different chromaticities and for different number of tracked particles
import numpy as np
import matplotlib.pyplot as plt
import metaclass as mtc
from fourier import fourier
from latex_output import write_tex
from naff_transformation import naff_transformation
from error import error
from track_plots import *

N_part = 10
#run MADX script for different number of turns! ob.TURN will change

chromaticities = [0,1,5,10,15,20,25,30,35,40]
'''
chromaticities = []
f = open('chromaticities.txt','r')
for line in f:
    chrom=line.split()
    chromaticities.append(float(chrom[0]))
'''

for j in xrange(len(chromaticities[:1])):           #try for as many chromaticities as you like
    #Fourier lists
    max_X = []                                      #here store the prominent frequency
    max_Y = []
    f_X = []                                        #here store the frequency
    f_Y = []
    fft_X = []                                      #here store the transformation data
    fft_Y = []

    #coordinate lists
    x_objects = []
    y_objects = []
    t_objects = []
    px_objects = []
    py_objects = []
    pt_objects = []
    turn = []                                       #store number of turns needed for tracking (control from MADX)

    #store comparison differences between FFT and NAFF
    error_x_compare = []
    error_y_compare = []

    #NAFF data are stored here
    naff_X = []                                     #prominent frequency by NAFF
    naff_Y = []
    amp_X = []                                      #amplitude of the prominent frequency
    amp_Y = []
    for i_part in range(N_part):
        fname_twiss = 'track_master%d.out.obs0001.p%04d'%(chromaticities[j],i_part+1)
        ob = mtc.twiss(fname_twiss)

        #put coordinates in lists
        turn.append(ob.TURN)
        x_objects.append(ob.X)
        y_objects.append(ob.Y)
        t_objects.append(ob.T)
        px_objects.append(ob.PX)
        py_objects.append(ob.PY)
        pt_objects.append(ob.PT)

        #FFT
        maximum_X, fourier_X, freq_X = fourier(ob.X, timestep = 1) 
        max_X.append(maximum_X)
        f_X.append(freq_X)
        fft_X.append(fourier_X)

        #NAFF
        amplitude_X, counter_X, maximum_X_naff = naff_transformation(ob.TURN, np.array(ob.X))
        naff_X.append(maximum_X_naff)
        amp_X.append(amplitude_X[counter_X-1])

        #see the difference between fourier and naff
        error_X, change_X = error(maximum_X, maximum_X_naff[i_part])
        error_x_compare.append(error_X)                                 

        #FFT
        maximum_Y, fourier_Y, freq_Y = fourier(ob.Y, timestep = 1)
        max_Y.append(maximum_Y)
        f_Y.append(freq_Y)
        fft_Y.append(fourier_Y)

        #NAFF
        amplitude_Y, counter_Y, maximum_Y_naff = naff_transformation(ob.TURN, np.array(ob.Y))
        naff_Y.append(maximum_Y_naff)
        amp_Y.append(amplitude_Y[counter_Y-1])

        error_Y, change_Y = error(maximum_Y, maximum_Y_naff[i_part])
        error_y_compare.append(error_Y)
  

    #tracking results of the 6 coordinates for all particles
    track_all(x_objects,y_objects,t_objects,px_objects,py_objects,pt_objects,N_part)

    #plots X and Y coordinates over the number of turns
    plot_turns(turn, x_objects, y_objects, N_part)

    #plot NAFF spectrum
    plot_naff(naff_X, amp_X, naff_Y, amp_Y)

    #fourier transformation amplitude and phase
    print_fourier(f_X, f_Y, fft_X, fft_Y, N_part)

    write_tex(max_X, max_Y, N_part) 


