import numpy as np
import matplotlib.pyplot as plt

def plot_tune_change(mean_x_list, mean_y_list, freq_x_list, freq_y_list, turns):
	plt.rc('text', usetex=True)
	plt.rc('font', family='serif')

	plt.figure()
	plt.plot(turns, mean_x_list)
	plt.xlabel(r'$Chromaticities$')
	plt.ylabel(r'$Mean$ $tunes (x)$')
	ax = plt.gca()
	ax.ticklabel_format(useOffset=False)
	plt.show()

	plt.figure()
	plt.plot(turns, mean_y_list)
	plt.xlabel(r'$Chromaticities$')
	plt.ylabel(r'$Mean$ $tunes (y)$')
	ax = plt.gca()
	ax.ticklabel_format(useOffset=False)
	plt.show()

	plt.figure()
	plt.plot(turns, freq_x_list)
	plt.xlabel(r'$Chromaticities$')
	plt.ylabel(r'$Tune$ $frequency (x)$')
	ax = plt.gca()
	ax.ticklabel_format(useOffset=False)
	plt.show()

	plt.figure()
	plt.plot(turns, freq_y_list)
	plt.xlabel(r'$Chromaticities$')
	plt.ylabel(r'$Tune$ $frequency (y)$')
	ax = plt.gca()
	ax.ticklabel_format(useOffset=False)
	plt.show()


def plot_deltap_change(dp_list, turns):
	plt.figure(figsize=(7,7))
	plt.plot(turns, dp_list)
	plt.xlabel(r'$Chromaticities$')
	plt.ylabel(r'$\Delta$p $frequencies (x)$')
	ax = plt.gca()
	ax.ticklabel_format(useOffset=False)
	plt.show()