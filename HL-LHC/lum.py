import numpy as np
import math
from print_lumi_decay import *
from pileup import *

# calculate head-on luminosity
def head_on(N1, N2, nb, frev, sx, sy):
	L = (N1*N2*nb*frev)/(4*(math.pi)*sx*sy)				# head-on
	return L

# calculate reduction factor
def reduction(blength, xing, sx):
	S = 1/math.sqrt(1 + math.pow((blength*xing/sx),2))	# luminosity reduction factor for x crossing plane
	return S

# find beam size of colliding bunches
def beam_size(n_em, bx):
	E = 6500									# energy in GeV
	mp =0.938									# proton mass GeV/c2
	gamma = E/mp								# relativistic gamma, beta = 1
	e_geo = n_em/gamma							# geometric emmitance
	#print 'Geometric emmitance: ', e_geo
	sx = math.sqrt(e_geo*bx)					# beam size
	sy = sx
	#print 'Beam size: ', sx, sy
	return sx, sy

# calculate total luminosity
def luminosity(N1, N2, n_em, frev, bx, nb, xing, blength):
	sx, sy = beam_size(n_em, bx)
	L = head_on(N1, N2, nb, frev, sx, sy)
	#print 'L: ', L
	S = reduction(blength, xing, sx)
	#print 'S: ', S
	L_tot = L*S
	return L_tot

def list_sum(l,a,b):
	l.append(a+b)
	a+=b
	return l,a

# luminosity and intensity decay
def decay_rate(xsect, N1, N2, n_em, frev, bx, nb, xing, blength, hours, m_tot, pl = False):
	time = hours*60*60							# 20 hours
	dt = 1										# dt = 1 sec (step)
	n_ip = 2 									#IPs (ATLAS, CMS)
	Lum = []
	N_part = []
	int_lumi = []
	int_N = []
	N_next = N1 								# first loop call for N(i) = N1
	N_prev = N1									# N_prev = N1
	sum_lumi = 0
	sum_N = 0
	for counter in xrange(0,time,dt):
		L = luminosity(N_next, N_next, n_em, frev, bx, nb, xing, blength)
		int_lumi,sum_lumi = list_sum(int_lumi,sum_lumi,L)
		int_N,sum_N = list_sum(int_N,sum_N,N_next)
		#print 'L: ', L
		if pl:
			max_lumi = pileup(xsect, nb, frev, m_tot)					# New luminosity because of pile-up
			if L>max_lumi:
				L = max_lumi
		Lum.append(L)
		dN = n_ip*xsect*L/nb
		#print 'dN: ', dN
		N_next = N_prev - dN 					# N(i) = N(i-1) - dN
		N_prev = N_next 				
		#print 'Number of particles: ', N_next
		N_part.append(N_next)

	# Plot decay
	print_lumi(Lum, N_part)
	# Plot integrated values
	print_int(int_lumi, int_N)

	print 'Integrated luminosity:', int_lumi[time-1]
	
	print 'Integrated intensity: ', int_N[time-1]

	return Lum, N_part




