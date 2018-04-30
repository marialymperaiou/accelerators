import numpy as np
import math
from lum import *

# calculate maximum luminosity for given maximum event pile-up
def pileup(xsect, nb, frev, m_tot):
	max_lumi = (m_tot*nb*frev)/xsect					
	#print 'Maximum luminosity: ', max_lumi
	return max_lumi
