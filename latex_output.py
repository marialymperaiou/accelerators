#print in the form of LATEX table for future use
import numpy as np
import metaclass as mtc

def write_tex(max_X, max_Y, N_part =10):			#try it for different number of tracking turns!
	fname = 'fourier_latex_output.txt'
	with open(fname, 'w') as fid:
		for i in xrange (N_part):
			fid.write('%d'%i)						#number of particles
			fid.write(' & ')
			fid.write('%.13f'%max_X[i])				#frequency of max(X) (prominent)
			fid.write(' & ')
			fid.write('%.13f'%max_Y[i])				#frequency of max(Y) (prominent)
			fid.write(' \\ ')
			fid.write('\n')

def tex_tunes_x(meanx, frequency_x,chromaticities):	
	fname = 'x_tunes_latex_output.txt'
	with open (fname,'w') as fid2:
		for j in xrange (len(chromaticities)):
			fid2.write('%d'%chromaticities[j])		#list of chromaticity values
			fid2.write(' & ')
			fid2.write('%.13f'%meanx[j])			#mean tune for the x - plane
			fid2.write(' & ')
			fid2.write('%.13f'%frequency_x[j])		#oscillation frequency of tune
			fid2.write(' \\ ')
			fid2.write('\n')

#same for the y - plane
def tex_tunes_y(meany, frequency_y, chromaticities):
	fname = 'y_tunes_latex_output.txt'
	with open (fname,'w') as fid3:
		for k in xrange (len(chromaticities)):
			fid3.write('%d'%chromaticities[k])
			fid3.write(' & ')
			fid3.write('%.13f'%meany[k])
			fid3.write(' & ')
			fid3.write('%.13f'%frequency_y[k])
			fid3.write(' \\ ')
			fid3.write('\n')

def tex_deltap(dp, chromaticities):
	fname = 'deltap_latex_output.txt'
	with open (fname,'w') as fid4:
		for k in xrange (len(chromaticities)):
			fid4.write('%d'%chromaticities[k])
			fid4.write(' & ')
			fid4.write('%.13f'%dp[k])			#deltap values for different chromaticities
			fid4.write(' \\ ')
			fid4.write('\n')
