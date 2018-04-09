import numpy as np

def print_info(naff_list):
	mean = np.mean(naff_list)
	print 'Mean tune', mean
	print 'Maximum tune value', max(naff_list)
	print 'Minimum tune value', min(naff_list)

	return mean