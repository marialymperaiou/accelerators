import numpy as np
import matplotlib.pyplot as plt
import metaclass as mtc
from fourier import fourier
from track_plots import *


N_part = 10

#change of x and y over turns
spt1,spt2 = tracking()

#plot FFTs
sp1,sp2,sp3,sp4 = fourier_plots()

for i_part in range(N_part):
    fname_twiss = 'track_master10.out.obs0001.p%04d'%(i_part+1)
    ob = mtc.twiss(fname_twiss)
    thiscolor = plt.cm.rainbow(float(i_part)/float(N_part))

    plot_coordinates(spt1, spt2, ob.TURN, ob.X, ob.Y, thiscolor)

    ############# Fourier for X ############# 
    maximum_X, fourier_X, freq_X = fourier(np.array(ob.X), timestep = 1)
        
    ############# Fourier for Y ############# 
    maximum_Y, fourier_Y, freq_Y = fourier(np.array(ob.Y), timestep = 1)

    ############# FourierImages #############    
    
    fourier_images(thiscolor, sp1, sp2, sp3, sp4, freq_X, fourier_X, freq_Y, fourier_Y)

plt.show()