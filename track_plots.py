import numpy as np
import matplotlib.pyplot as plt

def print_fft_naff(scripts, fft_x_list, naff_x_list, fft_y_list, naff_y_list):
    plt.close('all')
    plt.figure(1, figsize=(10,10))
    plt.plot(scripts, fft_x_list, 'y')
    plt.title('Prominent frequency (FFT-x plane)')
    plt.xlabel('Number of turns')
    plt.ylabel('Frequency')
    plt.grid(True)

    plt.figure(2, figsize=(10,10))
    plt.plot(scripts, naff_x_list, 'm')
    plt.title('Prominent frequency (NAFF-x plane)')
    plt.xlabel('Number of turns')
    plt.ylabel('Frequency')
    plt.grid(True)

    plt.figure(3, figsize=(10,10))
    plt.plot(scripts, fft_y_list, 'r')
    plt.title('Prominent frequency (FFT-y plane)')
    plt.xlabel('Number of turns')
    plt.ylabel('Frequency')
    plt.grid(True)

    plt.figure(4, figsize=(10,10))
    plt.plot(scripts, naff_y_list, 'g')
    plt.title('Prominent frequency (NAFF-y plane)')
    plt.xlabel('Number of turns')
    plt.ylabel('Frequency')
    plt.grid(True)

    plt.show()

#All the below are called by transformations.py
#plot (X,PX), (Y,PY), (T,PT) and also X,Y,T,PX,PY,PT over time
def track_all (X, Y, T, PX, PY, PT, N_part = 10):
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    #plot coordinates 
    plt.close('all')
    plt.figure(1, figsize = (8,8))
    sp1 = plt.subplot(3,1,1)
    plt.title(r'$Tracking (X)$')                                    #(X,PX)
    plt.xlabel(r'$X$')
    plt.ylabel(r'$PX$')
    plt.grid(True)

    sp2 = plt.subplot(3,1,2, sharex=sp1)
    plt.title(r'$Tracking (Y)$')                                    #(Y,PY)
    plt.xlabel(r'$Y$')
    plt.ylabel(r'$PY$')
    plt.grid(True)

    sp3 = plt.subplot(3,1,3)
    plt.title(r'$Tracking (T)$')                                    #(T,PT)
    plt.xlabel(r'$T$')
    plt.ylabel(r'$T$')
    plt.grid(True)

    plt.subplots_adjust( hspace=0.5, wspace=0.9)
    #coordinates vs time
    plt.figure(2, figsize = (8,8))

    spt1 = plt.subplot(3,1,1)
    plt.title(r'$X$')                                               #(X,t)
    plt.ylabel(r'$X$')
    plt.xlabel(r'$t$')
    spt2 = plt.subplot(3,1,2, sharex=spt1)
    plt.title(r'$Y$')                                               #(Y,t)
    plt.ylabel(r'Y')
    plt.xlabel(r't')
    spt3 = plt.subplot(3,1,3, sharex=spt1)
    plt.title(r'$T$')                                               #(T,t)
    plt.ylabel(r'$T$')
    plt.xlabel(r'$t$')
    plt.subplots_adjust( hspace=0.5, wspace=0.9)

    plt.figure(3, figsize = (8,8))
    spp1 = plt.subplot(3,1,1)
    plt.title(r'$PX$')                                              #(PX,t)
    plt.ylabel(r'$PX$')
    plt.xlabel(r'$t$')
    spp2 = plt.subplot(3,1,2, sharex=spt1)
    plt.title(r'$PY$')                                              #(PY,t)                                             
    plt.ylabel(r'$PY$')
    plt.xlabel(r'$t$')
    spp3 = plt.subplot(3,1,3, sharex=spt1)
    plt.title(r'$PT$')                                              #(PT,t)
    plt.ylabel(r'$PT$')
    plt.xlabel(r'$t$')

    plt.subplots_adjust( hspace=0.5, wspace=0.9)

    for i_part in range(N_part):

        thicolor = plt.cm.rainbow(float(i_part)/float(N_part))

        sp1.plot(X[i_part], PX[i_part], '.', color = thicolor)
        sp2.plot(Y[i_part], PY[i_part], '.', color = thicolor)
        sp3.plot(T[i_part], PT[i_part], '.', color = thicolor)

        spt1.plot(X[i_part])
        spt2.plot(Y[i_part])
        spt3.plot(T[i_part])

        spp1.plot(PX[i_part])
        spp2.plot(PY[i_part])
        spp3.plot(PT[i_part])


    plt.show()

#Plots x and y coordinates vs the number of turns
def plot_turns(turn, x_objects, y_objects, N_part = 10):
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.close('all')
    plt.figure(1)

    #track particles in X and Y plane
    spt1 = plt.subplot(3,1,1)                                           #(X,N)
    plt.title(r'$Tracking (X)$')
    plt.xlabel(r'$Number$ $of$ $turns$')
    plt.ylabel(r'$X$')
    plt.grid(True)

    spt2 = plt.subplot(3,1,2, sharex=spt1)
    plt.title(r'$Tracking (Y)$')                                        #(Y,N)
    plt.xlabel(r'$Number$ $of$ $turns$')
    plt.ylabel(r'$Y$')
    plt.grid(True)


    plt.subplots_adjust(top=0.9, bottom=-0.3, right=0.85, hspace=0.5, wspace=0.9)

    for i_part in range(N_part):
        thicolor = plt.cm.rainbow(float(i_part)/float(N_part))
        spt1.plot(turn[i_part], x_objects[i_part], '.', color = thicolor)
        spt2.plot(turn[i_part], y_objects[i_part], '.', color = thicolor)

    plt.show()

#plot NAFF spectrum for all particles
def plot_naff(naff_X, amp_X, naff_Y, amp_Y):
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    plt.figure()
    plt.plot(naff_X, amp_X)
    plt.suptitle(r'$NAFF$ $transformation$', fontsize = 16)
    plt.title(r'$Amplitude$ $vs$ $Frequency$')
    plt.xlabel(r'$Frequency$')
    plt.ylabel(r'$Amplitude$')
    plt.grid(True)
    plt.show()
 

#plot spectrum (amplitude and phase) of the FFT for x and y planes
def print_fourier(f_X, f_Y, fft_X, fft_Y, N_part = 10):
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    plt.close('all')

    plt.figure()
    plt.suptitle('FFT')

    #X
    sp1 = plt.subplot(4,2,1)
    plt.title(r'$Amplitude$ $for$ $X$')
    plt.xlabel(r'$Frequency$')
    plt.ylabel(r'$Amplitude$')
    plt.grid(True)

    sp2 = plt.subplot(4,2,2, sharex=sp1)
    plt.title(r'$Phase$ $for$ $X$')
    plt.xlabel(r'$Frequency$')
    plt.ylabel(r'$Phase$')
    plt.grid(True)

    #Y
    sp3 = plt.subplot(4,2,3)
    plt.title(r'$Amplitude$ $for$ $y$')
    plt.xlabel(r'$Frequency$')
    plt.ylabel(r'$Amplitude$')
    plt.grid(True)

    sp4 = plt.subplot(4,2,4, sharex=sp1)
    plt.title(r'$Phase$ $for$ $y$')
    plt.xlabel(r'$Frequency$')
    plt.ylabel(r'$Phase$')
    plt.grid(True)

    plt.subplots_adjust(top=0.92, bottom=-0.85, right=0.85, hspace=0.5, wspace=0.5)

    for i_part in xrange (N_part):
        thicolor = plt.cm.rainbow(float(i_part)/float(N_part))
        sp1.plot(f_X[i_part], abs(fft_X[i_part]), color = thicolor)
        sp2.plot(f_X[i_part], np.angle(fft_X[i_part]), color = thicolor)
        sp3.plot(f_Y[i_part], abs(fft_Y[i_part]), color = thicolor)
        sp4.plot(f_Y[i_part], np.angle(fft_Y[i_part]), color = thicolor)

    plt.show()



