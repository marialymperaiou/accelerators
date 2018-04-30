import numpy as np
import matplotlib.pyplot as plt

def print_lumi(Lum, N_part):
	plt.rc('text', usetex=True)
	plt.rc('font', family='serif')

	plt.figure()
	plt.plot(Lum)
	plt.title(r'$Luminosity$ $evolution$')
	plt.ylabel('Luminosity')
	plt.xlabel('t')
	plt.show()

	plt.figure()
	plt.plot(N_part, 'r')
	plt.title(r'$Particle$ $decay$ $dN/dt$')
	plt.ylabel('Number of particles')
	plt.xlabel('t')
	plt.show()

def print_int(L, N):
	plt.rc('text', usetex=True)
	plt.rc('font', family='serif')

	plt.figure()
	plt.plot(L,'m')
	plt.title(r'$Integrated$ $Luminosity$')
	plt.ylabel('Luminosity')
	plt.xlabel('t')
	plt.show()

	plt.figure()
	plt.plot(N, 'g')
	plt.title(r'$Integrated$ $Intensity$ ')
	plt.ylabel('Number of particles')
	plt.xlabel('t')
	plt.show()