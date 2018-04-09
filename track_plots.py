import numpy as np
import matplotlib.pyplot as plt

def tracking():
	plt.close('all')
	plt.figure(1, figsize=(10,10))

	#track particles in X and Y plane
	spt1 = plt.subplot(3,1,1)
	plt.title('Tracking (X)')
	plt.xlabel('Number of turns')
	plt.ylabel('X')
	plt.grid(True)

	spt2 = plt.subplot(3,1,2, sharex=spt1)
	plt.title('Tracking (Y)')
	plt.xlabel('Number of turns')
	plt.ylabel('Y')
	plt.grid(True)

	plt.subplots_adjust(top=0.9, bottom=-0.3, right=0.85, hspace=0.5, wspace=0.9)
	return spt1,spt2

def fourier_plots():
	#plot FFTs
	plt.figure(2, figsize=(10,10))
	plt.suptitle('FFT')

	sp1 = plt.subplot(4,2,1)
	plt.title('Amplitude for X')
	plt.xlabel('Frequency')
	plt.ylabel('Amplitude')
	plt.grid(True)

	sp2 = plt.subplot(4,2,2, sharex=sp1)
	plt.title('Phase for X')
	plt.xlabel('Frequency')
	plt.ylabel('Phase')
	plt.grid(True)

	sp3 = plt.subplot(4,2,3)
	plt.title('Amplitude for y')
	plt.xlabel('Frequency')
	plt.ylabel('Amplitude')
	plt.grid(True)

	sp4 = plt.subplot(4,2,4, sharex=sp1)
	plt.title('Phase for y')
	plt.xlabel('Frequency')
	plt.ylabel('Phase')
	plt.grid(True)

	plt.subplots_adjust(top=0.92, bottom=-0.85, right=0.85, hspace=0.5, wspace=0.5)
	return sp1,sp2,sp3,sp4

def plot_coordinates(spt1, spt2, turns, x, y, thiscolor):
	spt1.plot(turns, x, '.', color = thiscolor)
	spt2.plot(turns, y, '.', color = thiscolor)

def fourier_images(thiscolor, sp1, sp2, sp3, sp4, freq_X, fourier_X, freq_Y, fourier_Y):
	sp1.plot(freq_X, abs(fourier_X), color = thiscolor)
	sp2.plot(freq_X, np.angle(fourier_X), color = thiscolor)
	sp3.plot(freq_Y, abs(fourier_Y), color = thiscolor)
	sp4.plot(freq_Y, np.angle(fourier_Y), color = thiscolor)

def track_all (X, Y, T, PX, PY, PT, N_part = 10):
    #plot coordinates 
    plt.close('all')
    plt.figure(1, figsize=(10,10))
    sp1 = plt.subplot(3,1,1)
    plt.title('Tracking (X)')
    plt.xlabel('X')
    plt.ylabel('PX')
    plt.grid(True)

    sp2 = plt.subplot(3,1,2, sharex=sp1)
    plt.title('Tracking (Y)')
    plt.xlabel('Y')
    plt.ylabel('PY')
    plt.grid(True)

    sp3 = plt.subplot(3,1,3)
    plt.title('Tracking (T)')
    plt.xlabel('T')
    plt.ylabel('PT')
    plt.grid(True)

    plt.subplots_adjust( hspace=0.5, wspace=0.9)
    #coordinates vs time
    plt.figure(2, figsize=(10,10))
    spt1 = plt.subplot(3,1,1)
    plt.title('(X)')
    plt.ylabel('X')
    plt.xlabel('t')
    spt2 = plt.subplot(3,1,2, sharex=spt1)
    plt.title('(Y)')
    plt.ylabel('Y')
    plt.xlabel('t')
    spt3 = plt.subplot(3,1,3, sharex=spt1)
    plt.title('(T)')
    plt.ylabel('T')
    plt.xlabel('t')
    plt.subplots_adjust( hspace=0.5, wspace=0.9)

    plt.figure(3, figsize=(10,10))
    spp1 = plt.subplot(3,1,1)
    plt.title('(PX)')
    plt.ylabel('PX')
    plt.xlabel('t')
    spp2 = plt.subplot(3,1,2, sharex=spt1)
    plt.title('(PY)')
    plt.ylabel('PY')
    plt.xlabel('t')
    spp3 = plt.subplot(3,1,3, sharex=spt1)
    plt.title('(PT)')
    plt.ylabel('PT')
    plt.xlabel('t')

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


